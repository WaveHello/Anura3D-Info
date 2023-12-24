# Information on setting up vs-code fortran

[Repo page](https://github.com/fortran-lang/vscode-fortran-support?tab=readme-ov-file)

## Requirement
1) A python distribution with pip
2) VS code

The package should be able to work from the VS code add on center but if it doesn't than here's some steps to fix it
The steps were written by gnikit (The author of the repo) [Link to steps](https://fortran-lang.discourse.group/t/had-trouble-installing-fortls-please-install-manually-how-to-install-manually-without-pip/6721/8)
```
Pip is the python package manager included in all supported python installations; it’s a command line tool.

We can’t move away from Python (i.e. download an executable) what we can do is fix the user experience and make it to “just work” for the majority of our users.

The breakdown of the problem in Windows is:

python and hence pip might not be reachable via PATH
the folder in which pip installs applications is not by default reachable by PATH
if not in PATH VSCode cannot find the applications
Not being able to find fortls.exe raises the message you see.
It’s easy to enter into an infinite loop if step 1. works but not 2., i.e. you can install fortls but can’t reach via a terminal.

The manual solution I usually give is:

install python via the App store (or any other way you prefer)
in a new terminal Run python -m pip install fortls --user
in a terminal run python -m pip show fortls and make note of the Location
the fortls.exe should be located in a folder at the same level as <your prefix root>/lib/<other stuff> in a folder called Scripts
in VSCode’s global settings set the option
 "fortran.fortls.path": "<your prefix root>/Scripts/fortls.exe"
There is an active work package for this so if I don’t complete it myself in my free time it’s very likely I will post it as a GSoC project for next year.
```

Make sure you don't have
1) fortran-language-server
2) fprettify
3) findent
