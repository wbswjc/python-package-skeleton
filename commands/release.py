"""Build dist with wheel and upload to pypi if '--upload' is appeared."""
import package


def main(package_info: package.PackageInfo, *args, **kwargs):
    from subprocess import Popen

    Popen(['python', 'setup.py', 'sdist', 'bdist_wheel']).wait()

    if '--upload' in args:
        Popen(['python', '-m', 'twine', 'upload', 'dist/*']).wait()
