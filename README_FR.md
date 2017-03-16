# M-BOXE_MANAGER_CL
[English Version](https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/README.md)  

Gérer votre M-BOXE Servo-moteur en ligne de commande à partir d'une Rapsberry Pi par I2C

<img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/Manager_CL.png" title="Screenshoot Menu" alt="ScrenShoot Menu">

## Avant tout

Ce programme permet de paramétrer une M-Boxe dont la construction est detaillée dans le dépot [M-BOXE] (https://github.com/Nao974/M-BOXE/blob/master/README.md)  

## Contenu

`Ah_I2C.py` Librairie pour protocole I2C issue de la librairie ADAFRUIT_I2C  
`M-BOXE.py` Classe définissant l'objet M-BOXE avec paramétre et fonction s'appuyant sur la librairie Ah-I2C.py  

`M-BOXE_DEMO.py` Démonstration en boucle de mouvement d'une M-BOXE  
`M-BOXE_MANAGER_CL.py` Programme permettant le paramétrage de votre M-BOXE


## Installation

#### Step 1: Install Python3

Python 3.4 est normalement déja installé sur Raspbian si vous utilisé `python3`au lieu de `python`, si ce n'est pas le cas `sudo apt-get install python3`.  


#### Step 2: Active I2C

* Mettre en commentaire la ligne `blacklist i2c-bcm2708` dans le fichier `/etc/modprobe.d/raspi-blacklist.conf`
* Installez la suite des outils de gestion I2C `apt-get install i2c-tools`
* Redémarrer votre Raspberry.

Une fois votre M-BOXE paramétrée et connectée au bus I2C, tapez la commande `i2cdetect -y 1` (remplacer '1' par '0' par les versions 256Mo).  
<img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/i2cdetect.png" title="screenshoot_i2cdetect" alt="screenshoot_i2cdetect">  
Dans l'exemple ci dessus, la M-BOXE est configurée à l'adresse 0x14.  


## Usage

Aller dans dossier, puis tapez `python3 M-BOXE_MANAGER_CL.py`, saisir l'adresse de la M-BOXE:     
  <img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/Manager_CL_Connexion.png" title="Connexion" alt="Connexion"> 

* S pour agrandir le menu Etat (State)
* D pour agrandir le menu Données
* P pour agrandir le menu Paramètre

Pour changer une donnée du menu Paramètre, tapez le N° de registre de la donnée:  
<img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/Manager_CL_Change_Registre.png" title="Change_Registrer" alt="Change_Registrer">  
Vous pouvez lancer toutes les commandes I2C définies dans le référenciel de la M-BOXE  [Parameter_M-BOXE.pdf](https://github.com/Nao974/M-BOXE/blob/master/doc/Parameter_M-BOXE.pdf)  


## Historique

- [Historique](https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/history.md)


