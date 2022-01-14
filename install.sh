#!/bin/bash
# requirement pour l'update de wifi tool le 29/11/2021
RED='\e[31m'
echo -e "${RED} "
echo ""
echo "  __      __.__  _____._____________           .__    ";
echo " /  \    /  \__|/ ____\__\__    ___/___   ____ |  |   ";
echo " \   \/\/   /  \   __\|  | |    | /  _ \ /  _ \|  |   ";
echo "  \        /|  ||  |  |  | |    |(  <_> |  <_> )  |__ ";
echo "   \__/\  / |__||__|  |__| |____| \____/ \____/|____/ ";
echo "        \/   ";
echo " ======================================================== ":
echo " = GITHUB: https://github.com/actonetor                 = ";
echo " = INSTAGRAM: lefrentoune                               = ";
echo " = TIKTOK: https://tiktok.com/@charlie_bernard_au_fbi   = ";
echo " = Actonetor, 2021                                 V2.0 = ";
echo " ======================================================== ";

echo " Détéction du réseau.... ";
wget -q --tries=10 --timeout=20 --spider https://google.com/
if [[ $? -eq 0 ]]; then
    echo -e "INSTALLATION... "
    sudo apt install wifiphisher
    sudo apt install python3
    chmod 777 wifitool
    echo "Les requirements sont installés ! "
    rm install.sh
    
fi
