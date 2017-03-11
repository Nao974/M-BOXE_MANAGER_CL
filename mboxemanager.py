#!/usr/bin/env python
# -*- coding: latin-1 -*-

# === mboxe-manager==============================================
# .....
# ===============================================================
# ....
# ...
#
# Licence CC-BY-SA

import time
import struct
from mboxe import *
from Ah_I2C import *

command=0x00
address=0x00
dashboard=1
positionLast=0
mode=0

detailState= False
detailData= False
detailParameter= False
bye= False

def getAddress():
        try:
                ad_input = int(input("MBOXE ID  (0x00 to Quit): "),16)
                if ad_input == 0: return 0
                
                i2c= Ah_I2C( ad_input)
                i2c.readU8_Test(0x00)
        except:
                ad_input= getAddress()
        return (ad_input)

def getCmd():
        global detailState
        global detailData
        global detailParameter
        global bye
        
        cmd_input= input("Cmd: ")
        return_input= -1
        try:
                if cmd_input.upper()== 'Q': bye= not bye
                elif cmd_input.upper()== 'S': detailState= not detailState
                elif cmd_input.upper()== 'D': detailData= not detailData
                elif cmd_input.upper()== 'P': detailParameter= not detailParameter
                else:                     
                        temp= mboxeGet.reg_list[int(cmd_input,16)]
                        return_input= int(cmd_input,16)
        except:
                return_input= getCmd()
        return (return_input)
                
while not bye:
        if dashboard==1:
                if address == 0x00:
                        address = getAddress()
                        if address == 0: break
                        mboxeGet = Mboxe(address)
                print ("")
                print ("--------mboxe-manager v1.0--------")
                print ("MBOXE ID: 0x%02X" %address)
                #--- get versionCode
                time.sleep(0.100)
                mboxeGet.get_versionCode()
                reg= mboxeGet.versionCode_ref['write']
                print ("0x%02X.Firmware: %.2f" % (reg, mboxeGet.return_versionCode()) )

                #--- get infoConfig
                time.sleep(0.100)
                mboxeGet.get_infoConfig()
                reg= mboxeGet.infoConfig_ref['write']
                print ("0x%02X.Info Config: %s " % (reg, mboxeGet.return_infoConfig() ) )

                #--- get skeletonPosition
                time.sleep(0.100)
                mboxeGet.get_skeletonPosition()
                reg= mboxeGet.skeletonPosition_ref['write']
                print ("0x%02X.Skeleton Position: %s " % (reg, mboxeGet.return_skeletonPosition() ) )

                print ("- (S)tate - - - - - - - - - - ")
                if detailState:
                        #--- get state	
                        time.sleep(0.100)
                        mboxeGet.get_state()
                        print ("State: 0x%02X- %s" % (mboxeGet.return_state() , mboxeGet.state_list[mboxeGet.return_state()]) )
                       
                        #--- get mode
                        time.sleep(0.100)
                        mboxeGet.get_mode()
                        mode = mboxeGet.return_mode()
                        print ("Mode: 0x%02X- %s" % (mboxeGet.return_mode() , mboxeGet.mode_list[mode]) )
                        #--- get currentCurrent
                        time.sleep(0.100)
                        mboxeGet.get_currentCurrent()
                        print ("Current: %d A" % mboxeGet.return_currentCurrent())

                        #--- get temperatureCurrent
                        time.sleep(0.100)
                        mboxeGet.get_temperatureCurrent()
                        print ("Temperature: %.1f" % mboxeGet.return_temperatureCurrent())

                        #--- get protectionCurrent
                        time.sleep(0.100)
                        mboxeGet.get_protectionCurrent()
                        if mboxeGet.return_protectionCurrent()==0:
                                print ("Protection: OK")
                        else:
                                print("Fault Protection: %d", mboxeGet.return_protectionCurrent())

                print ("- (D)ata  - - - - - - - - - - ")
                if detailData:
                       #--- get contactBWFW
                        time.sleep(0.100)
                        mboxeGet.get_contactBWFW()
                        print ("contactBW: %s" % (1 & mboxeGet.return_contactBWFW() >> 5) )
                        print ("contactFW: %s" % (1 & mboxeGet.return_contactBWFW() >> 4) )

                        #--- get portD
                        time.sleep(0.100)
                        mboxeGet.get_portD()
                        portDValue = mboxeGet.return_portD()
                        portDString=  ' '.join(str(1 & (portDValue) >> i) for i in range(8)[::+1])
                        print ("Port D: %s" % portDString)

                        #--- get pinA2
                        time.sleep(0.100)
                        mboxeGet.get_pinA2()
                        print ("Pin A2: %s " % mboxeGet.return_pinA2() )

                       #--- get pinA3
                        time.sleep(0.100)
                        mboxeGet.get_pinA3()
                        print ("Pin A3: %s " % mboxeGet.return_pinA3()  )
 
                print ("- (P)arameter - - - - - -")
                if detailParameter:
                        #--- get limitBW
                        time.sleep(0.100)
                        mboxeGet.get_limitBW()
                        reg= mboxeGet.limitBW_ref['write']
                        print ("0x%02X.Limit BW: %s " % (reg, mboxeGet.return_limitBW() ) )

                        #--- get limitFW
                        time.sleep(0.100)
                        mboxeGet.get_limitFW()
                        reg= mboxeGet.limitFW_ref['write']
                        print ("0x%02X.Limit FW: %s " % (reg, mboxeGet.return_limitFW() ) )

                        #--- get offset
                        time.sleep(0.100)
                        mboxeGet.get_offset()
                        reg= mboxeGet.offset_ref['write']
                        print ("0x%02X.Offset: %s " % (reg, mboxeGet.return_offset() ) )

                        #--- get deadBand                        
                        time.sleep(0.100)
                        mboxeGet.get_deadBand()
                        reg= mboxeGet.deadBand_ref['write']
                        print ("0x%02X.DeadBand: %s " % (reg, mboxeGet.return_deadBand() ) )

                        # --- get kpPunch
                        time.sleep(0.100)
                        mboxeGet.get_kpPunch()
                        reg= mboxeGet.kpPunch_ref['write']
                        print ("0x%02X.kp-Punch: %.2f " % (reg, mboxeGet.return_kpPunch() ) )
                        
                        # --- get kdDumping
                        time.sleep(0.100)
                        mboxeGet.get_kdDumping()
                        reg= mboxeGet.kdDumping_ref['write']
                        print ("0x%02X.kd-Dumping: %.2f " % (reg, mboxeGet.return_kdDumping() ) )
                        
                        # --- get kiStretch
                        time.sleep(0.100)
                        mboxeGet.get_kiStretch()
                        reg= mboxeGet.kiStretch_ref['write']
                        print ("0x%02X.ki-Stretch: %.2f " % (reg, mboxeGet.return_kiStretch() ) )
                        
                        # --- get currentMaxSet
                        time.sleep(0.100)
                        mboxeGet.get_currentMaxSet()
                        reg= mboxeGet.currentMaxSet_ref['write']
                        print ("0x%02X.Current Max Set: %s " % (reg, mboxeGet.return_currentMaxSet() ) )
 
                        # --- get protectionGoSet
                        time.sleep(0.100)
                        mboxeGet.get_protectionGoSet()
                        reg= mboxeGet.protectionGoSet_ref['write']
                        print ("0x%02X.Protection Go Set: %s " % (reg, mboxeGet.return_protectionGoSet() ) )
        
                        # --- get temperatureMaxSet
                        time.sleep(0.100)
                        mboxeGet.get_temperatureMaxSet()
                        reg= mboxeGet.temperatureMaxSet_ref['write']
                        print ("0x%02X.TemperatureMax Set: %s " % (reg, mboxeGet.return_temperatureMaxSet() ) )

                print ("-------------------------")
                #--- get positionCurrent
                time.sleep(0.100)
                mboxeGet.get_positionCurrent()
                reg= mboxeGet.positionCurrent_ref['write']
                print ("0x%02X.Position: %d" % (reg,mboxeGet.return_positionCurrent()) )

                print ("-------------------------NtRi-2016--")
                print ("")                        

                dashboard=1 #display dashBord by default
                command = getCmd()

                #--- Update Config ---
                if command == 0x3B: # push versionCode
                        ref= mboxeGet.versionCode_ref
                        value= ref['type']
                        try: value = float ( input("Step:(%.2f): " % (ref['step'])) )
                        except:  print('Invalid value')
                        mboxeGet.set_versionCode(value)

                if command == 0x3C: # push infoConfig
                        ref= mboxeGet.infoConfig_ref                      
                        value= ref['type']
                        try: value = input("Value (Size:%d): " % (ref['size']))
                        except:  print('Invalid value')
                        result= mboxeGet.set_infoConfig(value)

                if command == 0x3D: # push skeletonPosition
                        ref= mboxeGet.skeletonPosition_ref                      
                        value= ref['type']
                        try: value = input("Value (Size:%d): " % (ref['size']))
                        except:  print('Invalid value')
                        result= mboxeGet.set_skeletonPosition(value)

                #--- Update Parameter ---
                if command == 0x30: # push limitBW
                        ref= mboxeGet.limitBW_ref                      
                        value= ref['type']
                        try: value = int (input("Value (%d ~ %d Step:%d): " % (ref['min'], ref['max'], ref['step'])) )
                        except:  print('Invalid value')
                        result= mboxeGet.set_limitBW(value)

                if command == 0x31: # push limitFW
                        ref= mboxeGet.limitFW_ref                      
                        value= ref['type']
                        try: value = int (input("Value (%d ~ %d Step:%d): " % (ref['min'], ref['max'], ref['step'])) )
                        except:  print('Invalid value')
                        result= mboxeGet.set_limitFW(value)

                if command == 0x32: # push offset
                        ref= mboxeGet.offset_ref                      
                        value= ref['type']
                        try: value = int (input("Value (%d ~ %d Step:%d): " % (ref['min'], ref['max'], ref['step'])) )
                        except:  print('Invalid value')
                        result= mboxeGet.set_offset(value)

                if command == 0x33: # push deadBand
                        ref= mboxeGet.deadBand_ref                      
                        value= ref['type']
                        try: value = int (input("Value (%d ~ %d Step:%d): " % (ref['min'], ref['max'], ref['step'])) )
                        except:  print('Invalid value')
                        result= mboxeGet.set_deadBand(value)

                if command == 0x34: # push kpPunch
                        ref= mboxeGet.kpPunch_ref                      
                        value= ref['type']
                        try: value = float (input("Value (%.2f ~ %.2f Step:%.2f): " % (ref['min'], ref['max'], ref['step'])) )
                        except:  print('Invalid value')
                        result= mboxeGet.set_kpPunch(value)

                if command == 0x35: # push kdDumping
                        ref= mboxeGet.kdDumping_ref                     
                        value= ref['type']
                        try: value = float (input("Value (%.2f ~ %.2f Step:%.2f): " % (ref['min'], ref['max'], ref['step'])) )
                        except:  print('Invalid value')
                        result= mboxeGet.set_kdDumping(value)

                if command == 0x36: # push kiStretch
                        ref= mboxeGet.kiStretch_ref                     
                        value= ref['type']
                        try: value = float (input("Value (%.2f ~ %.2f Step:%.2f): " % (ref['min'], ref['max'], ref['step'])) )
                        except:  print('Invalid value')
                        result= mboxeGet.set_kiStretch(value)

                if command == 0x38: # push currentMaxSet
                        ref= mboxeGet.currentMaxSet_ref                      
                        value= ref['type']
                        try: value = int (input("Value (%d ~ %d Step:%d): " % (ref['min'], ref['max'], ref['step'])) )
                        except:  print('Invalid value')
                        result= mboxeGet.set_currentMaxSet(value)

                if command == 0x39: # push protectionGoSet
                        ref= mboxeGet.protectionGoSet_ref                      
                        value= ref['type']
                        try: value = int (input("Value (%d ~ %d Step:%d): " % (ref['min'], ref['max'], ref['step'])) )
                        except:  print('Invalid value')
                        result= mboxeGet.set_protectionGoSet(value)

                if command == 0x3A: # push temperatureMaxSet
                        ref= mboxeGet.temperatureMaxSet_ref                      
                        value= ref['type']
                        try: value = int (input("Value (%d ~ %d Step:%d): " % (ref['min'], ref['max'], ref['step'])) )
                        except:  print('Invalid value')
                        result= mboxeGet.set_temperatureMaxSet(value)

                if command == 0x50: # push positionCurrent
                        ref= mboxeGet.positionCurrent_ref                      
                        value= ref['type']
                        try: value = int (input("Value (%d ~ %d Step:%d): " % (ref['min'], ref['max'], ref['step'])) )
                        except:  print('Invalid value')
                        result= mboxeGet.set_positionCurrent(value)

                #--- Push Mode ---
                ref= mboxeGet.mode_ref
                if command >= ref['min'] and command <= ref['max']:
                        print ('%s' % mboxeGet.mode_list[command])
                        mboxeGet.set_mode(command)
                        mode= command

                #--- EEPROM ---
                if command == 0x10:
                        print ('Load Parameter from EEPROM')
                        mboxeGet.cmd_eepromLoad()
                        time.sleep(1)
                if command == 0x11:
                        print ('Save Parameter to EEPROM')
                        mboxeGet.cmd_eepromSave()
                        time.sleep(1)

                #--- Def. MODE ---
                if (mode == 0x01): # Mode freewheel
                        print('^C for break')
                        while (True):
                                try: 
                                        time.sleep(0.500)
                                        mboxeGet.get_positionCurrent()
                                        reg= mboxeGet.positionCurrent_ref['write']
                                        print ("0x%02X.Position: %d" % (reg,mboxeGet.return_positionCurrent()) )
                                except:
                                        print('Return to Interactif Mode')
                                        mode=0x00
                                        break


                if (mode == 0x02): # Mode PID Position
                        print('^C for break')
                        while (True):
                                ref= mboxeGet.positionCurrent_ref                      
                                value= ref['type']
                                try: value = int (input("Value (%d ~ %d Step:%d): " % (ref['min'], ref['max'], ref['step'])) )
                                except:
                                        print('Invalid value, return to Interactif Mode')
                                        mode=0x00
                                        break
                                result= mboxeGet.set_positionCurrent(value)

 
