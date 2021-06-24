# ScareCrow-CobaltStrike script

A Cobalt Strike script for ScareCrow payload generation. Works only for the binary Loader.

## Installation

Setup ScareCrow [https://github.com/optiv/ScareCrow](https://github.com/optiv/ScareCrow)

Change the path variables inside ScareCrow.cna

```bash
./ScareCrow -I beacon.bin -Loader binary -domain microsoft.com
```
The generated payload is located at the CobaltStrike's main directory.

## Work in progress...
