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
    if [[ `wifiphisher` ]];then
            sudo apt install wifiphisher
    elif [[ `python3` ]]; then
            sudo apt install python3
    chmod 777 wifitool
    echo "Les requirements sont installés ! "
exit_on_signal_SIGINT() {
        { printf "\n\n%s\n\n" "Programme interuper..." 2>&1; }
        exit 0    
    }
    
exit_on_signal_SIGTERM() {
    { printf "\n\n%s\n\n" "Programme terminer." 2>&1; }
    exit 0
    }
