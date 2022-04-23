<h1 align="center">
<br>
<img src=image.png>
<br>
Cobalt Strike ⇌ ScareCrow
<br>
(EDR/AV evasion)
</h1>

<h4 align="center">EDR unhooking, Syscall loading, ETW/AMSI patch, Process Injection, Signed Loader, AES encrypt</h4>

<div align="center">
    
![GitHub stars](https://img.shields.io/github/stars/GeorgePatsias/ScareCrow-CobaltStrike)
![GitHub forks](https://img.shields.io/github/forks/GeorgePatsias/ScareCrow-CobaltStrike)
![GitHub size](https://img.shields.io/github/languages/code-size/GeorgePatsias/ScareCrow-CobaltStrike)
![GitHub lastcommit](https://img.shields.io/github/last-commit/GeorgePatsias/ScareCrow-CobaltStrike)
<br>
<a href="https://twitter.com/intent/follow?screen_name=GeorgePatsias1">
![Github twitter](https://img.shields.io/twitter/follow/GeorgePatsias1?label=Follow%20%40%20Twitter&style=social)
</a>
</div>

### 💣 ScareCrow Options
```bash
-I string
    Path to the raw 64-bit shellcode.
-Loader string
    Sets the type of process that will sideload the malicious payload:
    [*] binary - Generates a binary based payload. (This type does not benefit from any sideloading)
    [*] control - Loads a hidden control applet - the process name would be rundll32 if -O is specified. A JScript loader will be generated.
    [*] dll - Generates just a DLL file. Can be executed with commands such as rundll32 or regsvr32 with DllRegisterServer, DllGetClassObject as export functions.
    [*] excel - Loads into a hidden Excel process using a JScript loader.
    [*] msiexec - Loads into MSIexec process using a JScript loader.
    [*] wscript - Loads into WScript process using a JScript loader.
-O string
    Name of output file (e.g. loader.js or loader.hta). If Loader is set to dll or binary this option is not required.
-domain string
    The domain name to use for creating a fake code signing cert. (e.g. www.acme.com) 
-injection string
    Enables Process Injection Mode and specify the path to the process to create/inject into (use \ for the path).
-noamsi
    Disables the AMSI patching that prevents AMSI BuffferScanner.
-noetw
    Disables the ETW patching that prevents ETW events from being generated.
-nosleep
    Disables the sleep delay before the loader unhooks and executes the shellcode.
-sandbox
    Enables sandbox evasion using IsDomainedJoined calls.
```
## 📥 Clone the Project
```bash
git clone https://github.com/GeorgePatsias/ScareCrow-CobaltStrike.git
```

## 🏭 Install ScareCrow

Setup ScareCrow [https://github.com/optiv/ScareCrow](https://github.com/optiv/ScareCrow) just by running the `install.sh` script.
```bash
chmod +x install.sh
./install.sh
```

## 🔧 Setup CNA Script Configurations

Edit the ScareCrow.cna and replace the variables below accordingly. **NOTE!** Do not add the final **/** at the end of the paths!
```
#Path to the ScareCrow-CobaltStrike repository you just cloned.
$script_path = "/home/user/ScareCrow-CobaltStrike";

#Path to the compiled ScareCrow Go executable of the installation.
$scarecrow_executable = "/home/user/ScareCrow-CobaltStrike/ScareCrow/ScareCrow";
```

## 💀 Add the CNA script to Cobalt Strike
`Cobalt Strike > Script Manager > Load > Select ScareCrow.cna`

You will see the new menu item called **ScareCrow** on the top menu of Cobalt Strike.

### Side notes
* Run DLLs as following and slightly change the name of the exported DLL <br> `rundll32 example.dll,DllRegisterServer` <br> `rundll32 example.dll,DllGetClassObject`
* Process Injection field must be defined with a single `\` e.g `C:\Windows\System32\notepad.exe`
* When signing the loader with microsoft.com, using them against WINDOWS DEFENDER ATP products may not be as effective as they can validate the cert as it belongs to them. If you are using a loader against a windows product possibly use a different domain.

## 📖 Screenshot
<img src=Screenshot1.png>

## 📖 References
* [https://github.com/optiv/ScareCrow](https://github.com/optiv/ScareCrow)
* https://adamsvoboda.net/evading-edr-with-scarecrow/<br/>
* https://www.optiv.com/insights/source-zero/blog/endpoint-detection-and-response-how-hackers-have-evolved (Part 1)<br/>
* https://www.optiv.com/insights/source-zero/blog/edr-and-blending-how-attackers-avoid-getting-caught (Part 2)
