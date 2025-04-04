from setuptools import find_packages,setup

setup(
    name = 'Generative AI Project',
    version = '0.0.0'
    author = 'Shruti Mandaokar'
    author_email = 'shrutimandaokar.connect@gmail.com',
    packages = find_packages(),
    install_requires = []
)

from setuptools import setup, find_packages

setup(
    name="your_project_name",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)