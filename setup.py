import json
import os
import re
from typing import List

import setuptools

changelog_file = 'CHANGELOG.md'
readme_file = 'README.md'
requirements_file = 'requirements.txt'
test_requirements_file = 'requirements-test.txt'
package_info_file = 'package.json'


def get_version() -> str:
    """Parse version from changelog."""
    if not os.path.isfile(changelog_file):
        raise LookupError('No changelog file.')
    with open(changelog_file) as f:
        for line in f:
            # '## [0.0.1] - 2019-11-02'
            match = re.search('^## \[(.*)\] - [\d]{4}-[\d]{2}-[\d]{2}$',
                              line.strip())
            if match:
                return match.group(1).strip()
    raise LookupError('No version found in changelog.')


def get_requirements() -> List[str]:
    """Get package requirements."""
    if not os.path.isfile(requirements_file):
        return []
    with open(requirements_file) as f:
        return f.read().splitlines()


def get_test_requirements() -> List[str]:
    """Get package test requirements."""
    if not os.path.isfile(test_requirements_file):
        return []
    with open(test_requirements_file) as f:
        return f.read().splitlines()


def get_long_description() -> str:
    """Get package long description."""
    if not os.path.isfile(readme_file):
        return ''
    with open(readme_file, 'r') as fh:
        return fh.read()


def get_package_info() -> dict:
    """Get package info from json file."""
    if not package_info_file:
        return {}
    with open(package_info_file) as f:
        return json.load(f)


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


def get_attrs() -> dict:
    """Get attrs for setuptools.setup(**attrs)."""
    default_attrs = {
        'version': get_version(),
        'license': 'MIT',
        'author': 'wbswjc',
        'author_email': 'me@wbswjc.com',
        'install_requires': get_requirements(),
        'tests_require': get_test_requirements(),
        'long_description': get_long_description(),
        'long_description_content_type': 'text/markdown',
        'packages': setuptools.find_packages(),
        'include_package_data': True,
        'zip_safe': False,
    }

    attrs = {**default_attrs, **get_package_info()}

    check_version_consistency(attrs.get('name'), attrs.get('version'))

    return attrs


setuptools.setup(**get_attrs())
