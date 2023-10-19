# Debian server guide

## Installér via grafisk interface

- Følg instrukserne der kommer på skærmen. 
- Når der skal vælges ekstra pakker/DE, vælges *kun* webserver, SSH og standard system utilities.

## Efter installation

- Login med bruger lavet under installation
- Skift til root med "su -"
- Opdatér + opgrader pakker med "apt update" + "apt upgrade"
- Installér sudo + git med "apt install sudo git"
- Tilføj bruger til sudo gruppen med "usermod -aG sudo $USERNAME"
- Gå ud af root med "exit"
- Log ud fra bruger med "logout"
- Log ind igen.
- Tjek om bruger er tilføjet sudo gruppen med "sudo whoami"
- klon github med "git clone https://github.com/ExManubis/debian_server/"
- "cd debian_server" 
- gør skrift eksekvérbart med "chmod +x server_install.sh"
- kør script "./server_install.sh"
- Done!
