# Project Details


## What is a "Platform"

A scrapli community platform is a collection of arguments/settings that apply to a particular platform (vendor/os
). This includes settings such as privilege levels, timeouts, open/close callables, prompt patterns, and any other
 scrapli arguments. Once a platform exists and scrapli community has been installed, users can simply pass an
  argument "platform" with a value that matches the platform name and the scrapli factory (`Scrapli`) will automatically
   add the appropriate platform arguments to the connection object it returns.  


## Supported Platforms

The following are the currently supported platforms:

| Platform Name         | Vendor          | OS            | Contributor(s)                                             | Last Update | Notes                                                                                 |
|-----------------------|-----------------|---------------|------------------------------------------------------------|-------------|---------------------------------------------------------------------------------------|
| ruckus_fastiron       | Ruckus          | FastIron      | [Brett Canter](https://github.com/wonderbred)              | 2020.08.08  |                                                                                       |
| huawei_vrp            | Huawei          | VRP           | [Alex Lardschneider](https://github.com/AlexLardschneider) | 2020.11.13  | Last update fixed minor prompt pattern issue (missing underscore)<br><br>Might need to manually set `screen-width` or PTY cols, see issue [#18](https://github.com/scrapli/scrapli_community/issues/18) for more details.                  | 
| edgecore_ecs          | Edgecore        | ECS           | [Alex Lardschneider](https://github.com/AlexLardschneider) | 2020.09.19  | For the firmware shipped by Edgecore itself                                           |
| fortinet_wlc          | Fortinet        | WLC           | [Alex Lardschneider](https://github.com/AlexLardschneider) | 2020.11.15  | For the Meru-based OS, not the same as FortiOS                                        |
| aethra_atosnt         | Aethra          | ATOSNT        | [Alex Lardschneider](https://github.com/AlexLardschneider) | 2020.11.15  | Tested on ATOS NT, ranging from 6.3.X up to 6.5.X:                                    |
| mikrotik_routeros     | Mikrotik        | RouterOS      | [Alex Lardschneider](https://github.com/AlexLardschneider) | 2020.11.15  |                                                                                       |
| siemens_roxii         | Siemens         | ROX II        | [Khiem Nguyen](https://github.com/kn-winter)               | 2021.01.30  |                                                                                       |
| hp_comware            | HP              | Comware       | [Julien Corsini](https://github.com/juliencorsini)         | 2021.XX.XX  |                                                                                       |



## Why add a Platform

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
    cls.channel.write(cls.auth_username)
    cls.channel.send_return()
    time.sleep(0.25)
    cls.channel.write(cls.auth_password)
    cls.channel.send_return()


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


## Related Scrapli Libraries

This repo is the "community" platform repository for scrapli, you can find more out about the other scrapli 
libraries, including scrapli "core", below:


- [scrapli](/more_scrapli/scrpali)
- [scrapli_netconf](/more_scrapli/scrapli_netconf)
- [nornir_scrapli](/more_scrapli/nornir_scrapli)
- [scrapli_stubs](/more_scrapli/scrapli_stubs)
