#!/bin/bash
sudo apt-get install openssl osslsigncode mingw-w64 golang -y;
git clone https://github.com/optiv/ScareCrow;
cd ScareCrow;
go get github.com/fatih/color;
go get github.com/yeka/zip;
go get github.com/josephspurrier/goversioninfo;
go build ScareCrow.go

echo ""
echo "[Success] All Done! Please configure the ScareCrow.cna variables now."
