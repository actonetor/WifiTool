#!/usr/bin/env bash
clear
# Verif root
blue='\e[1;34m'
[[ `id -u` -eq 0 ]] > /dev/null 2>&1 || { echo  "Lancez ce script en mode root !"; echo ; exit 1; }


#Verif internet
function checkinternet() 
{
  ping -c 1 google.com > /dev/null 2>&1
  if [[ "$?" != 0 ]]
  then
    echo -e " Verification de la connection internet: FAILED"
    echo
    echo -e "Ce script a besoin 'internet"
    echo
    echo -e " WifiTool Exit"
    echo && sleep 2
    exit
  else
    echo -e " Verification d la connection internet: CONNECTED"
  fi
}

echo -e "${blue} "
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
echo ""
checkinternet
sleep 1
echo ""
echo "® Vérification de tous les paquet installé  ®" 
echo "                                       " 
# check des paquets
which wifiphisher > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "[ ✔ ] Wifiphisher..............[ found ]"
which wifiphisher > /dev/null 2>&1
sleep 2
else
echo -e "[ X ] Wifiphisher..............[ not found ]"
echo -e "[ ! ] Installation de Wifiphisher "
sudo apt-get install wifiphisher
echo -e "[ ✔ ] Paquet installé ...."
which wifiphisher > /dev/null 2>&1
sleep 2
fi


# check des paquets
which python3 > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e "[ ✔ ] python3..............[ found ]"
which python3 > /dev/null 2>&1
sleep 2
else
echo -e "[ X ] python3..............[ not found ]"
echo -e "[ ! ] Installation de python3 "
sudo apt-get install python3
echo -e "[ ✔ ] Paquet installé ...."
which python3 > /dev/null 2>&1
sleep 2
fi

function apache_svc_start()
{
 service apache2 start | zenity --progress --pulsate --title "CHARGEMENT..." --text="Start apache2 service" --percentage=0 --auto-close --width 300 > /dev/null 2>&1
}
apache_svc_start



