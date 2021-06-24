# ScareCrow-CobaltStrike script

A Cobalt Strike script for ScareCrow payload generation. Works only for the binary Loader.

## ScareCrow Installation

Setup ScareCrow [https://github.com/optiv/ScareCrow](https://github.com/optiv/ScareCrow)
```bash
git clone https://github.com/optiv/ScareCrow
cd ScareCrow
```
Before you compile ScareCrow, you'll need to install the dependencies. 

To install them, run following commands:

```
go get github.com/fatih/color
go get github.com/yeka/zip
go get github.com/josephspurrier/goversioninfo
```
Make sure that the following are installed on your OS:
```
openssl
osslsigncode
mingw-w64
```

Then build it

```
go build ScareCrow.go
```

## Setup Script Configurations

Edit ScareCrow.cna and replace the variables below.
```
$script_path = "path to ScareCrow Script directory e.g. /home/user/Scare/ScareCrow-CobaltStrike";
$scarecrow_executable = "https://github.com/optiv/ScareCrow path to the compiled ScareCrow executable e.g.  /home/user/ScareCrow/ScareCrow";
$python3 = "/usr/bin/python3";
```

## Add script to Cobalt Strike
Cobalt Strike > Script Manager > Load > Select ScareCrow.cna

You will see the new menu called ScareCrow on the top menu of CS.

### What is generated
```bash
./ScareCrow -I beacon.bin -Loader binary -domain microsoft.com
```
The generated payload is located at the CobaltStrike's main directory.

## More options and work still in progress...
