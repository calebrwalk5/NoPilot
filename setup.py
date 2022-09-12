#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
with open("README.md") as readme_file:
    README = readme_file.read()

setup(
    name="NoPilot",
    version="0.0.1",
    description="GitHub CoPilot alternative",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/calebrwalk5/NoPilot",
    author="Caleb Walker",
    keywords=["language model"],
    packages=find_packages(),
    install_requires=[],
)
