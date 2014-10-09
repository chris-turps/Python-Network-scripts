import sys
import re
import os

sys.stdout = open('output', 'wb')

path = "./configs"              # location of config files
listofiles = os.listdir(path)
#print listofiles

cmds_ios = [
        'hostname',
        'route-target',
        'ip vrf',
        ' rd '
    ]

# falsepos_ios = [
#        'ip vrf forwarding'
#    ]

# cmds_xr = [
#        'hostname',
#        'route-target',
#        'vrf'
#    ]

# cmds_timos = [
#        'hostname',
#        'route-target',
#        'ip vrf',
#        'export-map'
#    ]

for individual in listofiles:
    file = os.path.join(path, individual)
    cfg = open(file,'r')
    for line in cfg:
        if re.search('IOS XR',line):
#            print line
#            for line in cfg:
#                for cmd in cmds_ios:
#                    if re.search(cmd,line):
#                        print line
        elif re.search('TiMOS',line):
#            print line
#            for line in cfg:
#                for cmd in cmds_timos:
#                    if re.search(cmd,line):
#                        print line
        elif re.search('version 1[2-5]',line):
#            print line
            for line in cfg:
                if not re.search('ip vrf forwarding',line):
                    for cmd in cmds_ios:
                        if re.search(cmd,line):
                            print line

    cfg.close()

sys.stdout.close()
               

        
    
