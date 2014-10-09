import sys
import re

sys.stdout = open('ios-vrfs', 'wb')

stuff = open('output','r')
for line in stuff:
    if re.search('hostname', line):
        x = str(line)
#       print x
    elif re.search('ip vrf', line):
        y = str(line)
#       print y
    elif re.search('rd', line):
        z = str(line)
    elif re.search('export', line):
        w = str(line)
        expy = str.splitlines(x + y + z + w)
        print expy
    elif re.search('import', line):
        v = str(line)
        impy = str.splitlines(x + y + z + v)
        print impy
    else:
        pass

sys.stdout.close()
            

    

    

        
