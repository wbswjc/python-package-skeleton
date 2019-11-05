"""Create virtual environment in specific path."""


def main(*args, **kwargs):
    import os
    from subprocess import Popen

    root_path = kwargs.get('root_path')
    venv_dir = kwargs.get('venv_dir')

    venv_path = os.path.join(root_path, venv_dir)

    if os.path.isdir(venv_path):
        raise FileExistsError('"{}" is a directory.'.format(venv_path))

    Popen(['python', '-m', 'venv', venv_path]).wait()

    Popen([os.path.join(venv_path, 'bin', 'pip'), 'install',
           '--upgrade', 'pip']).wait()
