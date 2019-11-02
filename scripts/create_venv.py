#!python

import os
from subprocess import Popen

here = os.path.abspath(os.path.join(__file__, '../..'))

path = os.path.join(here, 'venv')

if os.path.isdir(path):
    raise FileExistsError('"{}" is a directory.'.format(path))

Popen(['python', '-m', 'venv', path]).wait()

Popen([os.path.join(path, 'bin', 'pip'), 'install', '--upgrade', 'pip']).wait()
