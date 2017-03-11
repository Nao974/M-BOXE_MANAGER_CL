#!/usr/bin/env python
# -*- coding: latin-1 -*-

# === mboxe-demo==============================================
# .....
# ===============================================================
# ....
# ...
#
# Ecrit par Nao-Tumu Réunion Island
# www.encours.fr
# Licence CC-BY-SA

import time
import struct
from Adafruit_I2C import Adafruit_I2C

positionCurrent=0
address=0
count=0

while 1:
	print ""
	print "--------mboxe-Demo--------"
	if address == 0x00:
		address = input("MBOXE ID: ")
		i2c = Adafruit_I2C( address )
	else:
		print "MBOXE ID: 0x%x" %address

	#--- get limitBW
	time.sleep(0.100)
	lstData =  i2c.readList( 0x20, 2 )
	sData = ''
	for aByte in lstData:
			sData = sData + chr(aByte)
	limitBW, = struct.unpack('<H',sData)
	limitBW=100 
	print "0x30.Limit BW: %d" % limitBW

	#--- get limitFW
	time.sleep(0.100)
	lstData =  i2c.readList( 0x21, 2 )
	sData = ''
	for aByte in lstData:
			sData = sData + chr(aByte)
	limitFW, = struct.unpack('<H',sData)
	limitFW=1000
	print "0x31.Limit FW: %d" % limitFW

	#--- get Position
	time.sleep(0.100)
	lstData =  i2c.readList( 0x40, 2 )
	sData = ''
	for aByte in lstData:
			sData = sData + chr(aByte)
	positionCurrent, = struct.unpack('<H',sData)
	print "0x40.Current position: %d" % positionCurrent

	print "--------------------------"
	print " "

	time.sleep(3)
	print "   * --> LimitFW"
	i2c.write16(0x50,limitFW)
	
	time.sleep(3)
	print "   * <-- LimitBW"
	i2c.write16(0x50,limitBW)

	time.sleep(3)
	print "   * --> Middle"
	i2c.write16(0x50,limitBW+((limitFW-limitBW)/2))
	
	time.sleep(3)
	print "   * --> LimitFW"
	i2c.write16(0x50,limitFW)
	
	time.sleep(3)
	print "   * <-- Middle"
	i2c.write16(0x50,limitBW+((limitFW-limitBW)/2))
	
	time.sleep(3)
	print "   * <-- LimitBW"
	i2c.write16(0x50,limitBW)
	
	time.sleep(3)
	print "   * -Slowly-> LimitFW by Step 10/0.1s"
	count=limitBW
	while count< limitFW:
		i2c.write16(0x50,count)
		count=count+10
		time.sleep(0.1)
		if count % 100 == 0:
			lstData =  i2c.readList( 0x40, 2 )
			sData = ''
			for aByte in lstData:
					sData = sData + chr(aByte)
			positionCurrent, = struct.unpack('<H',sData)
			print "   Read Current position: %d" % positionCurrent
		
	print "   * <-Slowly- LimitBW by Step 10/0.1s"
	count=limitFW
	while count > limitBW:
		i2c.write16(0x50,count)
		count=count-10
		time.sleep(0.1)
		if count % 100 == 0:
			lstData =  i2c.readList( 0x40, 2 )
			sData = ''
			for aByte in lstData:
					sData = sData + chr(aByte)
			positionCurrent, = struct.unpack('<H',sData)
			print "   Read Current position: %d" % positionCurrent
			
	time.sleep(3)
	print "   * <--Continuous rotation-->"
	i2c.write16(0x50,5000)

	time.sleep(5)
	i2c.write16(0x50,limitBW+((limitFW-limitBW)/2))
	
	count=0
	while count>20:
		print " "
		count = count+1