#!python

import os
from subprocess import Popen

root = os.path.abspath(os.path.join(__file__, '../..'))

venv_path = os.path.join(root, 'venv')

if os.path.isdir(venv_path):
    raise FileExistsError('"{}" is a directory.'.format(venv_path))

Popen(['python', '-m', 'venv', venv_path]).wait()

Popen([os.path.join(venv_path, 'bin', 'pip'), 'install',
       '--upgrade', 'pip']).wait()
