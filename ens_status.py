#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 11:54:53 2019

@author: koushik
"""
def prRed(skk): 
    print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk):
    print("\033[92m {}\033[00m" .format(skk)) 


def fetch_file_configuration():
    configParser = configparser.RawConfigParser() 
    ensconfig_path = '/home/shift/Desktop/ens_status/'
    name_ensconfig = 'monitor_configfile.dat'
    ensconfig_path = ensconfig_path + name_ensconfig
    configParser.read(ensconfig_path)
    ens_directory = configParser.get('Configuration Settings','log_directory')
    ens_logfile = configParser.get('Configuration Settings','ens_logfile')
    return(ens_directory,ens_logfile)

import configparser
from time import sleep
import subprocess
from datetime import datetime
import os
if __name__ == '__main__':
    OUTPUT_TEXT ='ENS_STATUS::{}{}{} TIME::{}'
    while True:
        hour = datetime.now().timetuple().tm_hour
        minute = datetime.now().timetuple().tm_min
        sec = datetime.now().timetuple().tm_sec
        if hour == 23 and minute == 59 :
            print('ENS Software starting in 3 minutes...')
            sleep(180) 
            os.system('python ens_status.py')
        ens_directory,ens_logfile = fetch_file_configuration()
        enslogfile = ens_directory + ens_logfile
        try:
            last_ens_status = subprocess.check_output(['tail', '-1', enslogfile])
            last_ens_status = last_ens_status.decode('utf-8')
            last_ens_status = last_ens_status.split(',')
            last_ens=(last_ens_status[1])
            if ' ENS : RUNNING' in last_ens:
                prGreen(OUTPUT_TEXT.format('UP',u'\u2714',u'\u2714',last_ens_status[0].split(':')[1]))
            elif 'ENS : NOT RUNNING\n' in last_ens:
                prRed(OUTPUT_TEXT.format('DOWN',u'\u2718',u'\u2718',last_ens_status[0].split(':')[1]))
            sleep(60)
        except FileNotFoundError :
            print('File not found...',datetime.now())
