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

- [What is a Platform](#what-is-a-platform)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Supported Platforms](#supported-platforms)
- [Why add a Platform](#why-add-a-platform)
- [Adding a Platform](#adding-a-platform)
  - [Driver Type](#driver-type)
  - [Defaults](#defaults)
  - [Variants](#variants)
  - [Privilege Levels](#privilege-levels)
  - [Sync and Asyncio](#sync-and-asyncio)
  - [Open and Close Callables](#open-and-close-callables)

 
# What is a "Platform"

A scrapli community platform is a collection of arguments/settings that apply to a particular platform (vendor/os
). This includes settings such as privilege levels, timeouts, open/close callables, prompt patterns, and any other
 scrapli arguments. Once a platform exists and scrapli community has been installed, users can simply pass an
  argument "platform" with a value that matches the platform name and the scrapli factory (`Scrapli`) will automatically
   add the appropriate platform arguments to the connection object it returns.  


# Installation

You should be able to pip install scrapli-community "normally":

```
pip install scrapli-community
```

To install from this repositories master branch:

```
pip install git+https://github.com/scrapli/scrapli_community
```

To install from this repositories develop branch:

```
pip install -e git+https://github.com/scrapli/scrapli_community.git@develop#egg=scrapli_community
```

To install from source:

```
git clone https://github.com/scrapli/scrapli_community
cd scrapli_community
python setup.py install
```


# Quick Start

If a scrapli community platform has already been created for your target vendor/os taking advantage of that is quite
 easy! You can simply pass an argument `platform` with the name of the platform as the value to the `Scrapli` or
  `AsyncScrapli` factory classes. Note that the name of the platform should follow the pattern "{vendor}_{os}" -- for
   example `ruckus_fastiron` or for the example platform: `scrapli_networkdriver`.

```
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


# Supported Platforms

The following are the currently supported platforms:

| Platform Name         | Vendor          | OS            | Contributor(s)                                       | Last Update | Notes                                                                                 |
|-----------------------|-----------------|---------------|------------------------------------------------------|-------------|---------------------------------------------------------------------------------------|
| ruckus_fastiron       | Ruckus          | FastIron      | [Brett Canter](https://github.com/wonderbred)        | 2020.08.08  |                                                                                       |
| huawei_vrp            | Huawei          | VRP           |                                                      | 2020.08.08  | Untested, based on [this issue](https://github.com/carlmontanari/scrapli/issues/20)   | 


# Why add a Platform

Why add a platform!? Because you think scrapli is awesome and want to be able to use it with whatever platform
/operating system(s) you are working with of course! Scrapli is intended to be super flexible, and you can almost
 certainly make it work with a platform of your choosing without building a community "platform", for example, you
  can check out the example in scrapli core of connecting to a "non core device" [here](https://github.com/carlmontanari/scrapli/blob/master/examples/non_core_device/wlc.py)
  this example predates scrapli communities existence, and worked just fine! 
  
So, again, why build a platform? Convenience and community mostly! Without a scrapli community platform, you will
 need to pass all of the appropriate arguments to build a connection each time you instantiated a scrapli connection
  object. Sure that is relatively easy (copy/paste!), however its a little cumbersome. Once a scrapli community
   platform is created, you can simply reference the platform type and then provide only the necessary arguments such
    as host and authentication information to your object instantiation. 

For example, (from the non core device example link above) without a scrapli community platform we may have to create
 our device connection like so:

```
def wlc_on_open(cls):
    """Example `on_open` function for use with cisco wlc"""
    # time.sleeps here are just because my test device was a bit sluggish, without these scrapli is
    #  just going to send the username/password right away
    time.sleep(0.25)
    # since the channel isn't fully setup, we access the transport and send the commands directly
    #  note that when accessing the transport directly we need to manually send the return char
    cls.transport.write(cls.transport.auth_username)
    cls.transport.write(cls.channel.comms_return_char)
    time.sleep(0.25)
    cls.transport.write(cls.transport.auth_password)
    cls.transport.write(cls.channel.comms_return_char)


wlc = {
    "host": "1.2.3.4",
    "auth_username": "some_username",
    "auth_password": "some_password",
    "auth_strict_key": False,
    "auth_bypass": True,
    # set a custom "on_open" function to deal with the non-standard login
    "on_open": wlc_on_open,
    # set a custom "comms_prompt_pattern" to deal with the non-standard prompt pattern
    "comms_prompt_pattern": r"^\(Cisco Controller\) >$",
}

conn = GenericDriver(**wlc)
```

With a community platform created our connection creation may end up being as simple as:

```
wlc = {
    "host": "1.2.3.4",
    "auth_username": "some_username",
    "auth_password": "some_password",
    "auth_strict_key": False,
    "platform": "cisco_wlc"
}

conn = Scrapli(**wlc)
``` 


# Adding a Platform

Adding a platform to be supported by scrapli is a fairly straight forward process! Before getting started there are a
 few things to understand about scrapli:

1. scrapli is fairly low level -- this means that it is assumed that the user will deal with most\* platform specific
 things such as saving configurations, copying files, and things like that.
2. scrapli assumes that the ssh channel/session will behave "normally" -- as in look and feel like a typical network
 operating system ssh session (just like all the "core" platforms behave).

\* scrapli *does* however handle privilege levels/escalation/deescalation

Before jumping into how to build a platform, it is best to start off with rehashing what exactly a platform is! A
 platform is simply a collection of arguments/callables (functions) defined in a dictionary. This `SCRAPLI_PLATFORM`
 dictionary is loaded up by the scrapli factory classes (`Scrapli` and `AsyncScrapli`) and used to instantiate an
  object built on the `GenericDriver` or `NetworkDriver` classes in scrapli.

The reasoning behind platforms *not* being simply classes that inherit from the `GenericDriver` or `NetworkDriver` as
 the current "core" platforms do, is to keep scrapli core as loosely coupled to the platforms as is possible
 /practical -- this is hugely important to help ensure that scrapli core as as little "cruft" as possible, and stays
  well tested/documented/etc., while still allowing users to adapt scrapli to work with various platforms easily.

A `SCRAPLI_PLATFORM` dictionary (the dictionary defining the platform) is made up of only three main top level keys:

1. `driver_type` -- simply `generic` or `network`, no other options are allowed
2. `defaults` -- a dictionary containing all required arguments to create a connection object
3. `variants` -- a dictionary of dictionaries containing any types of variations to the "defaults" section -- this
 allows users to have different "profiles" for a specific device type; for example there may be a variant that has a
  different "on_open" callable that disables paging differently for newer versions of a platform or something like that

Before jumping into details about what these all mean/do, here is an example platform dictionary:

```python
SCRAPLI_PLATFORM = {
    "driver_type": "network",
    "defaults": {
        "privilege_levels": DEFAULT_PRIVILEGE_LEVELS,
        "default_desired_privilege_level": "privilege_exec",
        "sync_on_open": default_sync_on_open,
        "async_on_open": default_async_on_open,
        "sync_on_close": default_sync_on_close,
        "async_on_close": default_async_on_close,
        "failed_when_contains": [
            "% Ambiguous command",
            "% Incomplete command",
            "% Invalid input detected",
            "% Unknown command",
        ],
        "textfsm_platform": "cisco_iosxe",
        "genie_platform": "iosxe",
    },
    "variants": {
        # not useful, just an example
        "test_variant1": {"default_desired_privilege_level": "configuration"}
    },
}
```

The following sections will outline each of these values and what they mean/how they are used.


## Driver Type

As mentioned above, there are only two permissible values for the `driver_type` argument, this can be either "generic
" or "network" and indicates which base driver class to use in scrapli core. If your device platform has the concept
 of different privilege levels then you should select "network", otherwise "generic". Most network specific platforms
  will likely be built with the "network" option selected (probably).

Note that depending on the type selected for `driver_type` there will be slightly different required arguments
 -- please see the example/test generic and network drivers in the [scrapli vendor directory](scrapli_community/scrapli)
 directory. Note that the docs here in the README will focus on the "network" type as that is likely going to be more
  common and is slightly more involved.

## Defaults

The "defaults" section contains all of the most "normal" or common arguments/settings for a given platform. All
 scrapli `NetworkDriver` or `GenericDriver` (depending on the platform you selected) arguments are valid here. Here
  are the most commonly needed arguments, see the scrapli core docs for all available options.

| Argument                          | Type                      | Required | Purpose                                   |
|-----------------------------------|---------------------------|------------------------------------------------------|
| privilege_levels                  | Dict[str, PrivilegeLevel] | True     | dictionary defining device priv levels    |
| default_desired_privilege_level   | str                       | True     | string of desired default priv level      |
| sync_on_open                      | Callable                  | False    | callable to run "on open"                 |
| async_on_open                     | Callable                  | False    | asyncio callable to run "on open"         |
| sync_on_close                     | Callable                  | False    | callable to run "on close"                |
| async_on_close                    | Callable                  | False    | asyncio callable to run "on close"        |
| failed_when_contains              | List[str]                 | False    | list of strings indicating command failure|
| textfsm_platform                  | str                       | False    | platform name for textfms/ntc parser      |
| genie_platform                    | str                       | False    | platform name for genie parser            |


Any arguments provided here in the "defaults" section are simply passed to the `NetworkDriver` or `GenericDriver
`. The reason this section is called "defaults" is that the arguments set here should apply to the broadest number of
 devices of a given platform. That said, it is of course possible that there are sometimes variations within even a
  single platform type (i.e. Cisco IOSXE) that may cause some of the default arguments to fail. That is where
   variants come in! 


## Variants

The "variants" section is nearly identical to the "defaults" section in that it provides arguments that will be
 passed to the underlying scrapli driver. There are two big differences for this section though; firstly, there is
  one extra level of nesting here -- "variants" is a dict of dicts with the top level keys of those dicts being the
   name of the variant, and the values of that dict being the actual values for the driver arguments. Here is an
    example:
    
```python
    "variants": {
        "test_variant1": {
            "comms_prompt_pattern": r"^\(BLAH\) >$"
        }
    },
```

The next thing you may notice is that there are many fewer arguments here! The reason being is that the "variants
" are merged with the arguments in the "defaults" section. The idea here is that there may be some vendor "Acme" that
 has an operating system called "Tacocat", but that os "Tacocat" has a few different options for login prompts for
  example. In most cases the "Acme Tacocat" operating system has a "normal" login process that just prompts for
   authentication and then lets you onto the router as per usual, but there may be a "variant"(!) that has a banner
    or some kind of prompt that the user must enter "OK" or "I ACCEPT" or something like that before being able to
     log on. This is what the "variant" is designed to handle -- nothing needs to change for this variant to work
      other than passing a new `on_open` method that is designed to deal with this different logon prompt.


## Privilege Levels

Privilege levels are critically important for any platform using the `network` driver_type -- this dictionary of
 `PrivilegeLevel` objects tells scrapli about the different "modes"/privilege levels of the platform, and how to get
  into and out of each of them. Below is an example taken from the `scrapli_networkdriver` example/test platform:
  
```
    "configuration": (
        PrivilegeLevel(
            pattern=r"^[a-z0-9.\-_@/:]{1,63}\(conf[a-z0-9.\-@/:\+]{0,32}\)#$",
            name="configuration",
            previous_priv="privilege_exec",
            deescalate="end",
            escalate="configure terminal",
            escalate_auth=False,
            escalate_prompt="",
        )
    ),
```

The key of the dictionary is "configuration" (the name of the privilege level), and the value is a `PrivilegeLevel
` object. You can read more about privilege levels in the main scrapli README [here](https://github.com/carlmontanari/scrapli#driver-privilege-levels).

The main takeaway is that it is vitally important to get the privilege levels correct, so take care to ensure these
 are very accurate -- especially the `pattern` argument -- it is very easy to miss a character/symbol that is valid
  for a prompt pattern, and this will cause scrapli to fail!


## Sync and Asyncio

Regardless of your requirements of sync vs asyncio, all community platforms must include both synchronous and aysncio
 support or they will not be merged. Even if you have never done anything with asyncio, this is a pretty small and
  straight forward requirement to satisfy. At the moment the only place that requires any special attention to sync
   and asyncio differences is for the "on open" and "on close" callables, please see the following section for details.


## Open and Close Callables

Scrapli provides the option for users to pass in their own callables to be executed after authentication and prior to
 closing the connection, you can read more about these in the README of the main scrapli repo [here](https://github.com/carlmontanari/scrapli#on-open).
 
In order to create a new scrapli-community platform, you almost certainly will need to provide these callables -- and
 if they are required are required in both sync and asyncio form. In general the on open callable needs to acquire
  the default desired privilege level (ex: "privilege exec" in IOSXE terms) and disable any kind of width/height
   settings on the terminal (disable pagination). Some other platforms may have differing requirements here such as
    handling login prompts/banners, performing additional authentication, or disabling other terminal behavior such
     as "complete on space" in Junos. 

The on close callable is much less important, but is nice to have to ensure that connections are "cleanly" closed
 -- this callable should generally handle the graceful exit/logout only.
 
If you have never written asyncio code and are interested in submitting a platform, please see the example platform
 code, the asycnio needed for creating these callables is very minimal and is essentially just using `async def
 ` instead of `def` for function definitions and adding the `await` keyword to any inputs/output commands.
