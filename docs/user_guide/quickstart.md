# Quick Start Guide

## Installation

In most cases installation via pip is the simplest and best way to install scrapli-community.

```
pip install scrapli-community
```


## A Simple Example

```python
from scrapli import Scrapli

my_device = {
    "host": "172.18.0.11",
    "auth_username": "vrnetlab",
    "auth_password": "VR-netlab9",
    "auth_strict_key": False,
    "platform": "ruckus_fastiron"
}

conn = Scrapli(**my_device)
conn.open()
```
