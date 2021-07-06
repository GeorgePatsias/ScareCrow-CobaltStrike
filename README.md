# ScareCrow-CobaltStrike script

A Cobalt Strike script for ScareCrow payload generation. Works only with the binary Loader.

#### What is being used for the generated executable
```bash
./ScareCrow -I beacon.bin -Loader binary -domain microsoft.com
```
## Download Project
```bash
git clone https://github.com/GeorgePatsias/ScareCrow-CobaltStrike.git
```

## ScareCrow Installation

Setup ScareCrow [https://github.com/optiv/ScareCrow](https://github.com/optiv/ScareCrow)
```bash
git clone https://github.com/optiv/ScareCrow
cd ScareCrow
go get github.com/fatih/color
go get github.com/yeka/zip
go get github.com/josephspurrier/goversioninfo
```
Make sure that the following packages are installed on your machine:
```
sudo apt-get install openssl osslsigncode mingw-w64 -y;
```

Build ScareCrow project

```
go build ScareCrow.go
```

## Setup CNA Script Configurations

Edit the ScareCrow.cna and replace the variables below accordingly. NOTE! Do not add the final / at the end of the paths!
```
$script_path = "Path of this GitHub project e.g. /home/user/Scare/ScareCrow-CobaltStrike";
$scarecrow_executable = "https://github.com/optiv/ScareCrow path to the compiled ScareCrow go executable e.g.  /home/user/ScareCrow/ScareCrow";
$cs_directory = "CobaltStrike's Installtion directory e.g. /home/kali/cobaltstrike";
$python3 = "/usr/bin/python3";
```

## Add the CNA script to Cobalt Strike
Cobalt Strike > Script Manager > Load > Select ScareCrow.cna

You will see the new menu called ScareCrow on the top menu of CS.

## More options and work still in progress...
