"""Create virtual environment in specific path."""


def main(g: callable, *args, **kwargs):
    import os
    from subprocess import Popen

    venv_path = os.path.join(g('root_path'), g('venv_dir'))

    if os.path.isdir(venv_path):
        raise FileExistsError('"{}" is a directory.'.format(venv_path))

    Popen(['python', '-m', 'venv', venv_path]).wait()

    Popen([os.path.join(venv_path, 'bin', 'pip'), 'install',
           '--upgrade', 'pip']).wait()
