
def format_package_names(packages):
    # convert all to lowercase
    packages = [package.lower() for package in packages]
    return packages

def string_package_names(packages):
    # create string feedable version of list
    packages = ' '.join(packages)
    return packages
