#!python
import sys
from subprocess import Popen

Popen(['python', 'setup.py', 'sdist', 'bdist_wheel']).wait()

if len(sys.argv) > 1 and sys.argv[1] == '--upload':
    Popen(['python', '-m', 'twine', 'upload', 'dist/*']).wait()
