import setuptools

import package

setup_info = package.setup_info

dynamic_info = {
    'version': package.get_version(),
    'install_requires': package.get_requirements(),
    'tests_require': package.get_test_requirements(),
    'long_description': package.get_long_description(),
    'packages': setuptools.find_packages(),
}

attrs = {**setup_info, **dynamic_info}

package.check_version_consistency(attrs.get('name'), attrs.get('version'))

setuptools.setup(**attrs)
