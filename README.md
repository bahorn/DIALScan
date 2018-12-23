# reDIAL

Tool to play around with DIAL[1], written in Python 3.

## What does this do?

* Fetch a list of registered DIAL apps from the Google Docs
* Discover every DIAL device on the LAN via UPNP.
* Probe each discovered device to see what apps are available on it.

## Why?

Got a Firestick, ran `nmap` on it and saw port 8009 open. Started probing it
and found out about DIAL because of this.

You can do some fun stuff with this, so I wrote this to let me experiment with
that.

## Usage

```
$ python3 src
Name: Mark's Fire TV Stick
Manufacturer: Amazon
Model: AFTT
Found: {'Netflix': True}
```

## Dependencies

* Requests https://github.com/requests/requests

## Licence

MIT, see `LICENSE`.

Dan Krause's SSDP implementation is used, with some changes to port it to
Python3: https://gist.github.com/dankrause/6000248
(Under Apache 2.0)

## References

```
[1] http://www.dial-multiscreen.org/
```
