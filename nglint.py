#!/usr/bin/env python3
import os
import subprocess
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
    #os.system("npm install")
    cmd = ['npm', 'run', 'lint'] # If no args, run ng lint over the whole project
    print(cmd)
    print(sys.argv[1:])
    #process = subprocess.run(cmd, capture_output=True)
    return 0

if __name__ == '__main__':
    exit(main())
