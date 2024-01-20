# FastenCConfigurator

## Goals
This project was designed to support the projects for compiling with different define (config/macro) sets.
E.g. You can describe 2 different situations (configs) and declare sets for them.
Maybe you would like to compile your project with debug settings AND without debug settings
Please see the "draw" below:

# X             | DEFINE1 | DEFINE2 | DEFINE3
# NAME OF SET   | x       |         | 
# new debug set | x       | x       | x

In this case, wi have "NAME OF SET" config, which requires the DEFINE1
But the "new debug set" requires the all defines (DEFINE1,2,3)

The project will parse the "project_config.md" and export different files for each others, which contains the proper defines.

