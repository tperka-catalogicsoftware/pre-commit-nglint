#!/usr/bin/env python
import os
import sys


def main(argv=None):
    '''
    Handle various pre-commit config options:
    - args:
        - if set, a bare double-dash is needed to distinguish options from the list of filenames
        - args before '--' are lint options and args after '--' are filenames
    - pass_filenames:
        - if false, ng lint should run over the full project
    '''
    os.system("npm install")
    cmd = ['ng', 'lint'] # If no args, run ng lint over the whole project

    print(cmd)
    os.execvp(cmd[0], cmd)

if __name__ == '__main__':
    exit(main())
