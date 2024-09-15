from setuptools import setup, find_packages

def get_requirements(file_name):
    """Read the requirements.txt file and return a list of packages."""
    with open(file_name) as f:
        return f.read().splitlines()

setup(
    name='mlproject',
    version='0.0.1',
    author='Varshini',
    author_email='sathiyavarshiniofficial@gmail.com',
    packages=find_packages(where="src"),  # This ensures 'src' folder is searched for packages
    package_dir={'': 'src'},  # Tells where to find the root package
    install_requires=get_requirements('requirements.txt'),  # Install dependencies
)
