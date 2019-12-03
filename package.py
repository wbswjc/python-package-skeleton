"""
Provide information about this package.
"""
import json
import os
import re
from typing import List

root_path = os.path.dirname(os.path.abspath(__file__))

setup_json_file = 'setup.json'
package_json_file = 'package.json'

default_setup_info = {
    'license': 'MIT',
    'author': 'wbswjc',
    'author_email': 'me@wbswjc.com',
    'long_description_content_type': 'text/markdown',
    'include_package_data': True,
    'zip_safe': False,
}

default_package_info = {
    'changelog_file': 'CHANGELOG.md',
    'package_json_file': package_json_file,
    'readme_file': 'README.md',
    'requirements_file': 'requirements.txt',
    'root_path': root_path,
    'scripts_dir': 'scripts',
    'setup_json_file': setup_json_file,
    'test_requirements_file': 'requirements-test.txt',
    'dev_requirements_file': 'requirements-dev.txt',
    'tests_dir': 'tests',
    'venv_dir': 'venv',
}


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class SetupInfo:
    def __init__(self):
        # Get setup info from json file.
        setup_info = default_setup_info
        if os.path.isfile(resource_path(setup_json_file)):
            with open(resource_path(setup_json_file)) as f:
                data = json.load(f)
            if isinstance(data, dict):
                for k in data:
                    setup_info[k] = data[k]
        self.setup_info = setup_info

    def get(self, key: str, default=None):
        """Entrance to get setup information"""
        return self.setup_info.get(key, default)

    def __iter__(self):
        return iter(self.setup_info)

    def __getitem__(self, k):
        return self.setup_info.get(k)


@singleton
class PackageInfo:
    def __init__(self):
        package_info = default_package_info

        setup_info = SetupInfo()
        for k in setup_info:
            package_info[k] = setup_info.get(k)

        if os.path.isfile(resource_path(package_json_file)):
            with open(resource_path(package_json_file)) as f:
                data = json.load(f)
            if isinstance(data, dict):
                for k in data:
                    package_info[k] = data[k]

        self.setup_info = setup_info
        self.package_info = package_info

    def get(self, key: str, default=None):
        """Entrance to get package information"""
        return self.package_info.get(key, default)

    def get_long_description(self) -> str:
        """Get package long description."""
        path = resource_path(self.get('readme_file'))
        if not os.path.isfile(path):
            return ''
        with open(path) as fh:
            return fh.read()

    def get_requirements(self) -> List[str]:
        """Get package requirements."""
        path = resource_path(self.get('requirements_file'))
        if not os.path.isfile(path):
            return []
        with open(path) as f:
            return f.read().splitlines()

    def get_test_requirements(self) -> List[str]:
        """Get package test requirements."""
        path = resource_path(self.get('test_requirements_file'))
        if not os.path.isfile(path):
            return []
        with open(path) as f:
            return f.read().splitlines()

    def get_version(self) -> str:
        """Parse version from changelog."""
        path = resource_path(self.get('changelog_file'))
        if not os.path.isfile(path):
            raise LookupError('No changelog file.')
        with open(path) as f:
            for line in f:
                # '## [0.0.1] - 2019-11-02'
                match = re.search('^## \[(.*)\] - [\d]{4}-[\d]{2}-[\d]{2}$',
                                  line.strip())
                if match:
                    return match.group(1).strip()
        raise LookupError('No version found in changelog.')

    def get_resource_path(self, k) -> str:
        return os.path.join(root_path, self.get(k))

    def __iter__(self):
        return iter(self.package_info)

    def __getitem__(self, k):
        return self.package_info.get(k)


def resource_path(*resource_path) -> str:
    """
    resource_path('package.json')
    resource_path('scripts', 'hello.py')
    """
    return os.path.join(root_path, *resource_path)


def check_version_consistency(name, version):
    """Check version consistency between changelog and source file."""
    if os.path.isfile(name):
        main_file = name
    elif os.path.isdir(name):
        main_file = os.path.join(name, '__init__.py')
    else:
        raise FileNotFoundError('"{}" not exists.'.format(name))

    with open(main_file) as f:
        for line in f:
            match = re.search("^version = '{}'.*$".format(version),
                              line.strip())
            if match:
                return
    raise LookupError('Version {} not set in {}'.format(version, main_file))
