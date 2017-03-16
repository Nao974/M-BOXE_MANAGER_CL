# M-BOXE_MANAGER_CL
[Version Française](https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/README_FR.md)  

To manage your M-BOXE Servo-motor command line from a Rapsberry Pi by I2C.  

<img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/Manager_CL.png" title="Screenshoot Menu" alt="ScrenShoot Menu">

## First of all

This program allows to parameterize an M-Boxe whose construction is detailed in the deposit [M-BOXE] (https://github.com/Nao974/M-BOXE/blob/master/README.md)  

## Contents

`Ah_I2C.py` Libraries for I2C protocol from the ADAFRUIT_I2C library
`M-BOXE.py` Class defining the M-BOXE object with parameter and function based on the Ah-I2C.py library  

`M-BOXE_DEMO.py` M-BOXE Motion Loop Demonstration  
`M-BOXE_MANAGER_CL.py` Program for setting up your M-BOXE


## Installation

#### Step 1: Install Python3

Python 3.4 is already installed if you use 'python3' instead of 'python', if it's not the case `sudo apt-get install python3`.  


#### Step 2: Active I2C

* Comment the line `blacklist i2c-bcm2708` in the file `/ etc / modprobe.d / raspi-blacklist.conf`
* Install the suite of I2C management tools `apt-get install i2c-tools`
* Restart your Raspberry.

Once your M-BOXE is set up and connected to the I2C bus, type `i2cdetect -y 1` (replace '1' with '0' with 256MB versions):  
<img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/i2cdetect.png" title="screenshoot_i2cdetect" alt="screenshoot_i2cdetect">  


## Usage

Go to folder, then type `python3 M-BOXE_MANAGER_CL.py`, enter the address of the M-BOXE 
  <img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/Manager_CL_Connexion.png" title="Connexion" alt="Connexion"> 

* S to enlarge the State Menu (State)
* D to enlarge the Data menu
* P to enlarge the Parameter menu

To change a data item in the Parameter menu, enter the data number of the data:  
<img src="https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/screenshoot/Manager_CL_Change_Registre.png" title="Change_Registrer" alt="Change_Registrer">  
You can launch all I2C commands defined in the M-BOXE benchmarks [Parameter_M-BOXE.pdf](https://github.com/Nao974/M-BOXE/blob/master/doc/Parameter_M-BOXE.pdf)  


## History / Historique

- [History](https://github.com/Nao974/M-BOXE_MANAGER_CL/blob/master/history.md)


