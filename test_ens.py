from time import sleep
import os
#from ens_status import check_ens
import subprocess
#check_ens()
print('sleepijng')
sleep(30)
print('restarting')
os.system('python ens_status.py')
sleep(70)
print('restarting')
os.system('python ens_status.py')
sleep(240)
print('restarting')
os.system('python ens_status.py')
