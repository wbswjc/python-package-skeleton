import setuptools

import package

setup_info = package.SetupInfo()
package_info = package.PackageInfo()

dynamic_info = {
    'version': package_info.get_version(),
    'install_requires': package_info.get_requirements(),
    'tests_require': package_info.get_test_requirements(),
    'long_description': package_info.get_long_description(),
    'packages': setuptools.find_packages(),
}

attrs = {**setup_info, **dynamic_info}

package.check_version_consistency(attrs.get('name'), attrs.get('version'))

setuptools.setup(**attrs)
