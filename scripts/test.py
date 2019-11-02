#!python

import os
from subprocess import Popen

root = os.path.abspath(os.path.join(__file__, '../..'))

venv_path = os.path.join(root, 'venv')

Popen([os.path.join(venv_path, 'bin', 'pytest'),
       '--cov', os.path.join(root, 'skeleton'), '--cov-report', 'term-missing',
       os.path.join(root, 'tests')]).wait()
