#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:54:53 2019

@author: koushik
"""
def prRed(skk): 
    blank = ''
    offset = 11 - len(str(skk)[:7])
    blank += ' ' * offset
    print("\033[92m {}\033[00m" .format(str(skk)[:7]),end = blank) 
    #print("\033[91m {}\033[00m" .format(str(skk)[:7]),end='    ') 
def prGreen(skk):
    blank = ''
    offset = 11 - len(str(skk)[:7])
    blank += ' ' * offset
    print("\033[92m {}\033[00m" .format(str(skk)[:7]),end = blank) 
def prYellow(skk): 
    blank = ''
    offset = 11 - len(str(skk)[:7])
    blank += ' ' * offset
    print("\033[93m {}\033[00m" .format(str(skk)[:7]),end = blank) 
def clear_screen():
    print("\033c")
# In[22]:
from datetime import datetime
import configparser
def fetch_file_configuration():
    configParser = configparser.RawConfigParser() 
    ensconfig_path = '/home/shift/Desktop/ens_status/'
    name_ensconfig = 'monitor_configfile.dat'
    ensconfig_path = ensconfig_path + name_ensconfig
    configParser.read(ensconfig_path)
    log_directory = configParser.get('Configuration Settings','log_directory')
    ens_logfile = configParser.get('Configuration Settings','ens_logfile')
    irnswt_logfile = configParser.get('Configuration Settings','irnswt_logfile')
    return(log_directory,ens_logfile,irnswt_logfile)


# In[46]:
from datetime import datetime
from time import sleep
import subprocess
if __name__ == '__main__':
    OUTPUT_HEADER ='TIME                  TSA-GNSS    TSB-GNSS    TSA-GPS    TSB_GPS'
    print(OUTPUT_HEADER)
    while True:
        log_directory,_,irnswt_logfile = fetch_file_configuration()
        day_of_year = datetime.now().timetuple().tm_yday
        year_of_day = datetime.now().timetuple().tm_year
        irnwt_logfile = log_directory + irnswt_logfile  + str(day_of_year) + '_' + str(year_of_day) + '.txt' 
        current_time =  str(datetime.now())[:19]
        current_time = datetime.strptime(current_time,'%Y-%m-%d %H:%M:%S')
        if current_time.minute in [0,15,30,45]:
            clear_screen()
            print(OUTPUT_HEADER)
        else:
            pass
    
        last_irnwt_status = subprocess.check_output(['tail', '-1', irnwt_logfile])
        last_irnwt_status = last_irnwt_status.decode('utf-8')
        last_irnwt_status = last_irnwt_status.split(',')
        time_now = (last_irnwt_status[0]).split(':')[1]
        TSA_GNSS = float((last_irnwt_status[1]).split(':')[1])
        TSB_GNSS = float((last_irnwt_status[2]).split(':')[1])
        TSA_GPS     = float((last_irnwt_status[3]).split(':')[1])
        TSB_GPS = float((last_irnwt_status[4]).split(':')[1])
        print(time_now,end='  ')
        
        if abs(TSA_GNSS) <= 10:
            prGreen(TSA_GNSS)
        elif abs(TSA_GNSS) > 10 and abs(TSA_GNSS) <= 20 :
            prYellow(TSA_GNSS)
        elif abs(TSA_GNSS) > 20:
            prRed(TSA_GNSS)

        if abs(TSB_GNSS) <= 10:
            prGreen(TSB_GNSS)
        elif abs(TSB_GNSS) > 10 and abs(TSB_GNSS) <= 20 :
            prYellow(TSB_GNSS)
        elif abs(TSB_GNSS) > 20:
            prRed(TSB_GNSS)
    
        if abs(TSA_GPS) <= 10:
            prGreen(TSA_GPS)
        elif abs(TSA_GPS) > 10 and abs(TSA_GPS) <= 20 :
            prYellow(TSA_GPS)
        elif abs(TSA_GPS) > 20:
            prRed(TSA_GPS)
    
        if abs(TSB_GPS) <= 10:
            prGreen(TSB_GPS)
            print()
        elif abs(TSB_GPS) > 10 and abs(TSB_GPS) <= 20 :
            prYellow(TSB_GPS)
            print()
        elif abs(TSB_GPS) > 20:
            prRed(TSB_GPS)
            print()
        sleep(70)
     
        
