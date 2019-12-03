"""Run pytest in virtual environment."""
import package


def main(package_info: package.PackageInfo, *args, **kwargs):
    import os
    from subprocess import Popen

    Popen([
        os.path.join(package_info.get_resource_path('venv_dir'), 'bin',
                     'pytest'),
        '--cov', package_info.get_resource_path('name'),
        '--cov-report', 'term-missing',
        package_info.get_resource_path('tests_dir'),
    ]).wait()
