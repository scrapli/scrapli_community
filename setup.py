#!/usr/bin/env python
"""scrapli_community - scrapli community platforms"""
import setuptools

__author__ = "Carl Montanari"

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

setuptools.setup(
    name="scrapli_community",
    version="2020.08.08",
    author=__author__,
    author_email="carl.r.montanari@gmail.com",
    description="",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/scrapli/scrapli_community",
    packages=setuptools.find_packages(),
    install_requires=["scrapli>=2020.07.12"],
    extras_require={},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.6",
)
