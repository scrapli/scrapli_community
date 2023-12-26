[![Supported Versions](https://img.shields.io/pypi/pyversions/scrapli.svg)](https://pypi.org/project/scrapli)
[![PyPI version](https://badge.fury.io/py/scrapli-community.svg)](https://badge.fury.io/py/scrapli-community)
[![Weekly Build](https://github.com/scrapli/scrapli_community/workflows/Weekly%20Build/badge.svg)](https://github.com/scrapli/scrapli_community/actions?query=workflow%3A%22Weekly+Build%22)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-blueviolet.svg)](https://opensource.org/licenses/MIT)

scrapli_community
=================

---

**Documentation**: <a href="https://scrapli.github.io/scrapli_community" target="_blank">https://scrapli.github.io/scrapli_community</a>

**Source Code**: <a href="https://github.com/scrapli/scrapli_community" target="_blank">https://github.com/scrapli/scrapli_community</a>

---


This is the scrapli_community repository for [scrapli](https://github.com/carlmontanari/scrapli).

If you would like to use scrapli, but the platform(s) that you work with are not supported in the "core" scrapli
 platforms, you have come to the right place! This library is intended to be a place for scrapli users to add
  additional platform support to scrapli.
 
Please see the main [scrapli repo](https://github.com/carlmontanari/scrapli) for much more information about the main
 project.


#### Key Features:

- __Easy__: It's easy to get going with scrapli -- check out the documentation and example links above, and you'll be 
  connecting to devices in no time.
- __Fast__: Do you like to go fast? Of course you do! All of scrapli is built with speed in mind, but if you really 
  feel the need for speed, check out the `ssh2` transport plugin to take it to the next level!
- __Great Developer Experience__: scrapli has great editor support thanks to being fully typed; that plus thorough 
  docs make developing with scrapli a breeze.
- __Well Tested__: Perhaps out of paranoia, but regardless of the reason, scrapli has lots of tests! Unit tests 
  cover the basics, regularly ran functional tests connect to virtual routers to ensure that everything works IRL! 
- __Pluggable__: scrapli provides a pluggable transport system -- don't like the currently available transports, 
  simply extend the base classes and add your own! Need additional device support? Create a simple "platform" in 
  [scrapli_community -- this repo!](https://github.com/scrapli/scrapli_community) to easily add new device support!
- __Concurrency on Easy Mode__: [Nornir's](https://github.com/nornir-automation/nornir) 
  [scrapli plugin](https://github.com/scrapli/nornir_scrapli) gives you all the normal benefits of scrapli __plus__ 
  all the great features of Nornir.


## Requirements

MacOS or \*nix<sup>1</sup>, Python 3.7+

<sup>1</sup> Although many parts of scrapli *do* run on Windows, Windows is not officially supported


## Installation

```
pip install scrapli-community
```

See the [docs](https://scrapli.github.io/scrapli_community/user_guide/installation) for other installation methods/details.



## A simple Example

```python
from scrapli import Scrapli

my_device = {
    "host": "172.18.0.11",
    "auth_username": "scrapli",
    "auth_password": "scrapli",
    "auth_strict_key": False,
    "platform": "ruckus_fastiron"
}

conn = Scrapli(**my_device)
conn.open()
```
