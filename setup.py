import os
import setuptools

base_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(base_dir, "README.md"), "r") as f:
    long_description = f.read()

setuptools.setup(
    name="PyHackMD",
    version="1.0.0",
    author="GoatWang",
    author_email="jeremy4555@yahoo.com.tw",
    description="Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    # package_data={'': ['', '', '']},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
      install_requires=[
        'requests',
      ]
)