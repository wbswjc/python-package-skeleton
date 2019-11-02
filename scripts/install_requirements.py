#!python

import os
from subprocess import Popen

root = os.path.abspath(os.path.join(__file__, '../..'))

venv_dir = 'venv'
requirements_file = 'requirements.txt'

Popen([os.path.join(root, venv_dir, 'bin', 'pip'), 'install',
       '-r', os.path.join(root, requirements_file)]).wait()
