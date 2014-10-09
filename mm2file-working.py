import getpass
import sys
import telnetlib
import time

sys.stdout = open('blah6', 'wb')

user = 'cisco'
password = 'arsenal'
# user = raw_input("Username: ")
# password = getpass.getpass()
# dlist = ['1.1.1.2','1.1.1.3']

def file_to_list(filename):
   result = []					               #create a list from text file
   file_list = [line.strip() for line in open(filename)]       #remove white space
   for line in file_list:				
       if not line.startswith('#'):			       #ignore commented lines
           if not line == '':				       #ignore blank lines
               result.append(line)			       #add cleansed lines to the list
   return result
   # Get device list from file
dlist = file_to_list('devicelist.txt')
print dlist

cmd_list = [
        'sh clock',
        'show ip int brief',
        #'sh ver | i IOS|uptime'
    ]

for d in dlist:
    tn = telnetlib.Telnet(d)
    tn.read_until("sername: ")
    tn.write(user + "\n")
    if password:
       tn.read_until("assword: ")
       tn.write(password + "\n")
    tn.read_until(">")
    for cmd in cmd_list:
       tn.write(cmd + "\n")
    tn.write("exit\n")
#   tn.write("show clock\n")
#   tn.write("exit\n")
    print tn.read_all()

time.sleep(3)




