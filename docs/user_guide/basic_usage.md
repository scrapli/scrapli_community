# Basic Usage

## Adding a Platform

Adding a platform to be supported by scrapli is a fairly straight forward process! Before getting started there are a
 few things to understand about scrapli:

1. scrapli is fairly low level -- this means that the assumption is that the user will deal with most\* platform 
   specific things such as saving configurations, copying files, and things like that.
2. scrapli assumes that the ssh channel/session will behave "normally" -- as in look and feel like a typical network
 operating system ssh session (just like all the "core" platforms behave).

\* scrapli *does* however handle privilege levels/escalation/deescalation

Before jumping into how to build a platform, it is best to start off with rehashing what exactly a platform is! A
 platform is simply a collection of arguments/callables (functions) defined in a dictionary. This `SCRAPLI_PLATFORM`
 dictionary is loaded up by the scrapli factory classes (`Scrapli` and `AsyncScrapli`) and used to instantiate an
  object built on the `GenericDriver` or `NetworkDriver` classes in scrapli.

The reasoning behind platforms *not* being simply classes that inherit from the `GenericDriver` or `NetworkDriver` as
 the current "core" platforms do, is to keep scrapli core as loosely coupled to the platforms as is possible
 /practical -- this is hugely important to help ensure that scrapli core has as little "cruft" as possible, and stays
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

As mentioned above, there are only two primary values for the `driver_type` argument, this can be either "generic"
 or "network" and indicates which base driver class to use in scrapli core. If your device platform has the concept
 of different privilege levels then you should select "network", otherwise "generic". Most network specific platforms
  will likely be built with the "network" option selected (probably).

You can also create your own class (inheriting from either the `NetworkDriver` or `GenericDriver` or their asyncio
 counterparts) if you wish to be able to override any methods of those classes or to implement your own methods.

Note that depending on the type selected for `driver_type` there will be slightly different required arguments
 -- please see the example/test generic and network drivers in the [scrapli vendor directory](https://github.com/scrapli/scrapli_community/tree/master/scrapli_community/scrapli)
 directory. Note that the docs here in the README will focus on the "network" type as that is likely going to be more
  common and is slightly more involved.

## Defaults

The "defaults" section contains all of the most "normal" or common arguments/settings for a given platform. All
 scrapli `NetworkDriver` or `GenericDriver` (depending on the platform you selected) arguments are valid here. Here
  are the most commonly needed arguments, see the scrapli core docs for all available options.

| Argument                          | Type                      | Required | Purpose                                   |
|-----------------------------------|---------------------------|----------|-------------------------------------------|
| privilege_levels                  | Dict [str: PrivilegeLevel]| True     | dictionary defining device priv levels    |
| default_desired_privilege_level   | str                       | True     | string of desired default priv level      |
| sync_on_open                      | Callable                  | False    | callable to run "on open"                 |
| async_on_open                     | Callable                  | False    | asyncio callable to run "on open"         |
| sync_on_close                     | Callable                  | False    | callable to run "on close"                |
| async_on_close                    | Callable                  | False    | asyncio callable to run "on close"        |
| failed_when_contains              | List [str]                | False    | list of strings indicating command failure|
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
` object. You can read more about privilege levels in the scrapli docs [here](https://carlmontanari.github.io/scrapli/user_guide/advanced_usage/#driver-privilege-levels).

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
 closing the connection, you can read more about these in the scrapli docs [here](https://carlmontanari.github.io/scrapli/user_guide/advanced_usage/#on-open).
 
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
