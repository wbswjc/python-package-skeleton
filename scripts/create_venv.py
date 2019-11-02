#!python

import os
from subprocess import Popen

root = os.path.abspath(os.path.join(__file__, '../..'))

venv_dir = 'venv'
venv_path = os.path.join(root, venv_dir)

if os.path.isdir(venv_path):
    raise FileExistsError('"{}" is a directory.'.format(venv_path))

Popen(['python', '-m', 'venv', venv_path]).wait()

Popen([os.path.join(venv_path, 'bin', 'pip'), 'install',
       '--upgrade', 'pip']).wait()
