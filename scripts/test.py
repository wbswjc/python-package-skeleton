"""Run pytest in virtual environment."""


def main(g: callable, *args, **kwargs):
    import os
    from subprocess import Popen

    root_path = g('root_path')

    Popen([os.path.join(root_path, g('venv_dir'), 'bin', 'pytest'),
           '--cov', os.path.join(root_path, g('name')),
           '--cov-report', 'term-missing',
           os.path.join(root_path, g('tests_dir'))]).wait()
