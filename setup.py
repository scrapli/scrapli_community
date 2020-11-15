#!/usr/bin/env python
"""scrapli_community - scrapli community platforms"""
import setuptools

__author__ = "Carl Montanari"

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

with open("requirements.txt", "r") as f:
    INSTALL_REQUIRES = f.read().splitlines()

setuptools.setup(
    name="scrapli_community",
    version="2020.11.15",
    author=__author__,
    author_email="carl.r.montanari@gmail.com",
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/scrapli/scrapli_community",
    project_urls={
        "Changelog": "https://github.com/scrapli/scrapli_community/blob/master/CHANGELOG.md"
    },
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=INSTALL_REQUIRES,
    extras_require={},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)
