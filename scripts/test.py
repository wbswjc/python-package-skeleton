#!python

import os
from subprocess import Popen

root = os.path.abspath(os.path.join(__file__, '../..'))

venv_dir = 'venv'
venv_path = os.path.join(root, venv_dir)

Popen([os.path.join(venv_path, 'bin', 'pytest')]).wait()
