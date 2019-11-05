"""Install requirements in virtual environment
 (including test requirements)."""


def main(g: callable, *args, **kwargs):
    import os
    from subprocess import Popen

    root_path = g('root_path')

    Popen([os.path.join(root_path, g('venv_dir'), 'bin', 'pip'), 'install',
           '-r', os.path.join(root_path, g('requirements_file')),
           '-r', os.path.join(root_path, g('test_requirements_file')),
           '-e', root_path]).wait()
