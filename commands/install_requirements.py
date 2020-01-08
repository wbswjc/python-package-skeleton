"""Install requirements in virtual environment"""
import package


def main(package_info: package.PackageInfo, *args, **kwargs):
    import os
    from subprocess import Popen

    Popen([
        os.path.join(package_info.get_resource_path('venv_dir'), 'bin', 'pip'),
        'install',
        '-r', package_info.get_resource_path('requirements_file')
    ]).wait()
