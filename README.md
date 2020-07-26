![](https://github.com/scrapli/scrapli_community/workflows/Weekly%20Build/badge.svg)
[![PyPI version](https://badge.fury.io/py/scrapli.svg)](https://badge.fury.io/py/scrapli)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


scrapli_community
=================

This is the scrapli_community repository for [scrapli](https://github.com/carlmontanari/scrapli).

If you would like to use scrapli, but the platform(s) that you work with are not supported in the "core" scrapli
 platforms, you have come to the right place! This library is intended to be a place for scrapli users to add
  additional platform support to scrapli.
 
Please see the main [scrapli repo](https://github.com/carlmontanari/scrapli) for much more information about the main
 project.


# Table of Contents

- [What it takes to add a Platform](#what-it-takes-to-add-a-platform)


# What it takes to add a Platform

Adding a platform to be supported by scrapli is a fairly straight forward process! Before getting started there are a
 few things to understand about scrapli:

1. scrapli is fairly low level -- this means that it is assumed that the user will deal with most\* platform specific
 things such as saving configurations, copying files, and things like that.
2. scrapli assumes that the ssh channel/session will behave "normally" -- as in look and feel like a typical network
 operating system ssh session (just like all the "core" platforms behave).

\* scrapli *does* however handle privilege levels/escalation/deescalation

Before jumping into how to build a platform, it is best to start off with describing what exactly a platform is! A
 platform is simply a collection of arguments/callables (functions) defined in a dictionary. This `SCRAPLI_PLATFORM
 ` dictionary is loaded up by the scrapli factory classes (`Scrapli` and `AsyncScrapli`) and used to instantiate an
  object built on the `GenericDriver` or `NetworkDriver` classes in scrapli.

The reasoning behind platforms *not* being simply classes that inherit from the `GenericDriver` or `NetworkDriver` as
 the current "core" platforms do, is to keep scrapli core as loosely coupled to the platforms as is possible
 /practical -- this is hugely important to help ensure that scrapli core as as little "cruft" as possible, and stays
  well tested/documented/etc., while still allowing users to adapt scrapli to work with various platforms easily.

A `SCRAPLI_PLATFORM` dictionary (the dictionary defining the platform) is made up of only three main top level keys:

1. `driver_type` -- simply `generic` or `network`, no other options are allowed
2. `defaults` -- a dictionary containing all required arguments to create a connection object (more on this later)
3. `variants` -- a dictionary of dictionaries containing any types of variations to the "defaults" section -- this
 allows users to have different "profiles" for a specific device type; for example there may be a variant that has a
  different "on_open" callable that disables paging differently for newer versions of a platform or something like that

TODO!