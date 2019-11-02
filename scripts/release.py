#!python

from subprocess import Popen

Popen(['python', 'setup.py', 'sdist', 'bdist_wheel']).wait()

Popen(['python', '-m', 'twine', 'upload', 'dist/*']).wait()
