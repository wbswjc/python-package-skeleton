#!python

import os
from subprocess import Popen

root = os.path.abspath(os.path.join(__file__, '..', '..'))

venv_path = os.path.join(root, 'venv')

Popen([os.path.join(venv_path, 'bin', 'pip'), 'install',
       '-r', os.path.join(root, 'requirements.txt'),
       '-r', os.path.join(root, 'requirements-test.txt'),
       '-e', root]).wait()
