import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

github = 'https://github.com/mzaini30/warna'

setuptools.setup(
	name="warna",
	version="1.0.2",
	author="Zen",
	author_email="muhzaini30@gmail.com",
	description="Menambahkan warna di Terminal",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url=github,
	project_urls={
		"Bug Tracker": github + "/issues",
	},
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	package_dir={"": "src"},
	packages=setuptools.find_packages(where="src"),
	python_requires=">=3.6",
)