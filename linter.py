#
#  linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Wu Jian
# Copyright (c) 2014 Wu Jian
#
#  License: MIT
"""This module exports the Pig plugin class."""
import os
import re
import subprocess
import shutil
from SublimeLinter.lint import Linter, util
import sublime
from sys import platform as _platform


# from sys import platform as _platform
if _platform == "linux" or _platform == "linux2":
    # linux
    pass
elif _platform == "darwin":
    # OS X
    p = subprocess.Popen(["/usr/libexec/java_home"], stdout=subprocess.PIPE)
    out, err = p.communicate()
    os.environ["JAVA_HOME"] = out.decode('utf-8').strip()
elif _platform == "win32":
    # Windows...
    pass

debug = False


class Pig(Linter):

    """Provides an interface to pig."""

    syntax = ('pig')
    cmd = 'pig --dryrun @'
    executable = 'pig'
    regex = r'^.+ (?:(?P<error>ERROR)|(?P<warning>WARNING)).*line (?P<line>\d+).*>\s*(?P<message>.+)'
    multiline = False
    line_col_base = (10, 1)
    tempfile_suffix = '.piglint'
    error_stream = util.STREAM_BOTH
    check_version = False
    debug = True
    debug_prefix = 'pigLinter: '
    run_cnt = 0
    inited = False
    tmp_dir = '/tmp/pig_linter'

    def set_pig_tmp_dir(self):
        """Create a temporary directory to store the log file."""

        self.run_cnt += 1

        if os.path.exists(self.tmp_dir) and self.run_cnt == 100:
            shutil.rmtree(self.tmp_dir)

        if not os.path.exists(self.tmp_dir):
            os.mkdir(self.tmp_dir)
        os.chdir(self.tmp_dir)

    def reset_line_col_base(self):
        """Pig will automatically include the content insider the .pigbootup file into current script.

        We need to set the line base so that we could point out the error line number correctly.

        """

        # check the line of the .pig
        pigbootup_line = 0
        pigbootup_path = '~/.pigbootup'
        if os.path.exists(os.path.expanduser(pigbootup_path)):
            if debug:
                print(self.debug_prefix + '.pigbootup exist')
            pigbootup_line = len(list(open(os.path.expanduser(pigbootup_path))))

        if debug:
            print(self.debug_prefix + 'pigbootup:', pigbootup_line)

        # modify the line_col_base
        self.line_col_base = (pigbootup_line + 1, 1)

    def get_pig_param(self, code):
        """Get all the pig parameter out from the code using regex."""

        var_names = re.findall('\$(\w+)', code)
        var_names = set(var_names)
        var_names = [var_name for var_name in var_names if not var_name.isdigit()]
        if debug:
            print(self.debug_prefix + str(var_names))
        return var_names

    def get_cmd_string(self, cmd, var_names):
        """Now we need to parse all the parameter out.

        So that the pig will not preduce the parameter not defined error.

        """

        var_names_with_prefix = ['-p {var_name}=123'.format(var_name=var_name) for var_name in var_names]
        pig_param_string = ' '.join(var_names_with_prefix)
        exe = self.executable_path if self.executable_path is not None else 'pig'
        all_cmd_string = "{exe} --dryrun {pig_param_string} @".format(
            exe=exe, pig_param_string=pig_param_string)
        if debug:
            print(self.debug_prefix + all_cmd_string)

        return all_cmd_string

    def run(self, cmd, code):
        """process the code with cmd."""

        self.set_pig_tmp_dir()

        self.reset_line_col_base()

        if debug:
            print(self.debug_prefix + str(cmd))
        var_names = self.get_pig_param(code)

        all_cmd_string = self.get_cmd_string(cmd, var_names)

        self.cmd = all_cmd_string
        cmd = all_cmd_string.split(' ')
        return super().run(cmd, code)

    @classmethod
    def which(cls, cmd):
        """To get the executable file's path."""

        SETTINGS_FILE = "SublimeLinter-contrib-pig.sublime-settings"
        settings = sublime.load_settings(SETTINGS_FILE)

        if debug:
            print(str(settings))
            print(settings.get("pig_home"), len(settings.get("pig_home")))

        if settings.has("java_home") and len(settings.get("java_home")) != 0:
            os.environ["JAVA_HOME"] = settings.get("java_home")

        if settings.has("pig_home") and len(settings.get("pig_home").strip()) != 0:
            return settings.get("pig_home")

        return None
