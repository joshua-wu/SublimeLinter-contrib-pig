SublimeLinter-contrib-pig
================================
[![Build Status](https://travis-ci.org/knightwu/SublimeLinter-contrib-pig.svg)](https://travis-ci.org/knightwu/SublimeLinter-contrib-pig)
![logo](doc/logo.png)

This linter plugin for [SublimeLinter][docs] provides an interface to [Pig](http://pig.apache.org/). It will be used with files that have the `Pig` syntax.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Pig installation
Before using this plugin, you must ensure that `Pig` is installed on your system. To install `Pig`, do the following:

1. Install download a recent stable release from one of the Apache Download Mirrors (see [Pig Releases](http://hadoop.apache.org/pig/releases.html)).

2. Unpack the downloaded Pig distribution. The Pig executable file is located in the bin directory (/pig-n.n.n/bin/pig).

3. *Optional*. Add /pig-n.n.n/bin to your path. Use export (bash,sh,ksh) or setenv (tcsh,csh). For example:
```
$ export PATH=/<my-path-to-pig>/pig-n.n.n/bin:$PATH
```

### Linter configuration
In order for `Pig` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. You must set the configuration by menu: *"Sublime Text"* -> *"Preferences"*-> *"Package settings"* -> *"PigLinter"* -> *"Settings -User"*, then,  a file will be opened with the following content:
```text
{
    // Set java_home if Pig complains that it cannot find JAVA_HOME 
    "java_home": "",
    
    // Set pig_home if the Pig binary is not in your system path
    "pig_home": ""
}
```
You should set both the java_home and pig_home for safety.
Here is an example:
```text
{
    // Set java_home if Pig complains that it cannot find JAVA_HOME 
    "java_home": "/Library/Java/JavaVirtualMachines/jdk1.7.0_67.jdk/Contents/Home",
    
    // Set pig_home if the Pig binary is not in your system path
    "pig_home": "/Users/jianwu/pig-0.12.0/bin/pig"
}
```
### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

2. When the plugin list appears, type `Pig`. Among the entries you should see `SublimeLinter-contrib-pig`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbrevations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings
