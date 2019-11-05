"""Install requirements in virtual environment
 (including test requirements)."""


def main(*args, **kwargs):
    import os
    from subprocess import Popen

    root_path = kwargs.get('root_path')
    venv_dir = kwargs.get('venv_dir')
    requirements_file = kwargs.get('requirements_file')
    test_requirements_file = kwargs.get('test_requirements_file')

    Popen([os.path.join(root_path, venv_dir, 'bin', 'pip'), 'install',
           '-r', os.path.join(root_path, requirements_file),
           '-r', os.path.join(root_path, test_requirements_file),
           '-e', root_path]).wait()
