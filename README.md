# M-BOXE_MANAGER_CL

To manage your M-BOXE Servo-motor command line from a Rapsberry Pi by I2C / Gérer votre M-BOXE Servo-moteur en ligne de commande à partir d'une Rapsberry Pi par I2C

<img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/Photo_CL.jpg" title="Photo CL" alt="Photo CL">

## First of all / Avant tout

This program allows to parameterize an M-Boxe whose construction is detailed in the deposit [M-BOXE] (https://github.com/Nao974/M-BOXE/blob/master/README.md)  

--

Ce programme permet de paramétrer une M-Boxe dont la construction est detaillée dans le dépot [M-BOXE] (https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/readme.md)  

## Contents / Contenu

`Ah_I2C.py` Librairie pour protocole I2C issue de la librairie ADAFRUIT_I2C  
`M-BOXE.py` Classe définissant l'objet M-BOXE avec paramétre et fonction s'appuyant sur la librairie Ah-I2C.py  

`M-BOXE_DEMO.py` Démonstration en boucle de mouvement d'une M-BOXE  
`M-BOXE_MANAGER_CL.py` Programme permettant le paramétrage de votre M-BOXE

--

`Ah_I2C.py` Libraries for I2C protocol from the ADAFRUIT_I2C library
`M-BOXE.py` Class defining the M-BOXE object with parameter and function based on the Ah-I2C.py library  

`M-BOXE_DEMO.py` M-BOXE Motion Loop Demonstration  
`M-BOXE_MANAGER_CL.py` Program for setting up your M-BOXE


## Installation

####Step 1: Install Python3

Python 3.4 is already installed if you use 'python3' instead of 'python', if it's not the case `sudo apt-get install python3`.  

--

Python 3.4 est normalement déja installé sur Raspbian si vous utilisé `python3`au lieu de `python`, si ce n'est pas le cas `sudo apt-get install python3`.  


####Step 2: Active I2C


* Comment the line `blacklist i2c-bcm2708` in the file `/ etc / modprobe.d / raspi-blacklist.conf`
* Install the suite of I2C management tools `apt-get install i2c-tools`
* Restart your Raspberry.

Once your M-BOXE is set up and connected to the I2C bus, type `i2cdetect -y 1` (replace '1' with '0' with 256MB versions):  
<img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/i2cdetect.png" title="screenshoot_i2cdetect" alt="screenshoot_i2cdetect">  

--

* Mettre en commentaire la ligne `blacklist i2c-bcm2708` dans le fichier `/etc/modprobe.d/raspi-blacklist.conf`
* Installez la suite des outils de gestion I2C `apt-get install i2c-tools`
* Redémarrer votre Raspberry.

Une fois votre M-BOXE paramétrée et connectée au bus I2C, tapez la commande `i2cdetect -y 1` (remplacer '1' par '0' par les versions 256Mo).  
Dans l'exemple ci dessus, la M-BOXE est configurée à l'adresse 0x14.  


## Usage


Go to folder, then type `python3 M-BOXE_MANAGER_CL.py`, enter the address of the M-BOXE 
  <img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/Manager_CL_Connexion.png" title="Connexion" alt="Connexion"> 

* S to unfold the State (State)
* D to unfold the Data menu
* P to unfold the Parameter menu

To change a data item in the Parameter menu, enter the data number of the data:  
<img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/Manager_CL_Change_Registre.png" title="Change_Registrer" alt="Change_Registrer">  
You can launch all I2C commands defined in the M-BOXE benchmarks [Parameter_M-BOXE.pdf](https://github.com/Nao974/M-BOXE/blob/master/doc/Parameter_M-BOXE.pdf)  

--

Aller dans dossier, puis tapez `python3 M-BOXE_MANAGER_CL.py`, saisir l'adresse de la M-BOXE (voir screenshoot ci dessus).   

* S pour déplier le menu Etat (State)
* D pour déplier le menu Données
* P pour déplier le menu Paramètre

Pour changer une donnée du menu Paramètre, tapez le N° de registre de la donnée: (voir screenshoot ci dessus). 
Vous pouvez lancer toutes les commandes I2C définies dans le référenciel de la M-BOXE  [Parameter_M-BOXE.pdf](https://github.com/Nao974/M-BOXE/blob/master/doc/Parameter_M-BOXE.pdf)  


## History / Historique

- [History] (https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/history.md)


