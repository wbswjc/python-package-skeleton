"""Create virtual environment in specific path."""
import package


def main(package_info: package.PackageInfo, *args, **kwargs):
    import os
    from subprocess import Popen

    venv_path = package_info.get_resource_path('venv_dir')

    if os.path.isdir(venv_path):
        raise FileExistsError('"{}" is a directory.'.format(venv_path))

    Popen(['python', '-m', 'venv', venv_path]).wait()

    Popen([os.path.join(venv_path, 'bin', 'pip'), 'install',
           '--upgrade', 'pip']).wait()
