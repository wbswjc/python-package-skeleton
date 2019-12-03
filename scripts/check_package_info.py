"""Create virtual environment in specific path."""
import package


def main(package_info: package.PackageInfo, *args, **kwargs):
    print("\npackage_info:\n")

    for k in sorted(package_info):
        print("  - {} -> {}".format(k, package_info[k]))

    print("\nsetup_info:\n")

    for k in sorted(package_info.setup_info):
        print("  - {} -> {}".format(k, package_info.setup_info[k]))

    print("")