from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ndpc/__init__.py
from ndpc import __version__ as version

setup(
	name="ndpc",
	version=version,
	description="Commissioners app",
	author="sam | iyke",
	author_email="samuelwaku1st@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
