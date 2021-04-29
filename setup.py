import setuptools
from os.path import join, dirname
from os import path

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

install_requires = []
fileRequirements = join(dirname(__file__), 'requirements.txt')
if path.exists(fileRequirements):
	with open(fileRequirements, 'r', encoding = 'utf-8') as f:
		pkgs = f.read()
		print('pkgs', pkgs)
		install_requires = pkgs.split('\n')

github = 'https://github.com/mzaini30/warna'

setuptools.setup(
	name="warna",
	version="1.1.2",
	author="Zen",
	author_email="muhzaini30@gmail.com",
	description="Menambahkan warna di Terminal",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url=github,
	project_urls={
		"Bug Tracker": github + "/issues",
	},
	install_requires = install_requires,
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	packages=['src']
)