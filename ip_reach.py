import sys
import subprocess

#Check if IP can be pinged
def ip_reach(list):
    # take each IP from the file
    for ip in list:
        # by removing the newline character
        ip = ip.rstrip("\n")
        # and ping the address but suppress the std output or error messages  (see ./Python_Net_App_03.png)
        ping_reply = subprocess.call('ping %s -n 2' % (ip,), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        # a reply of 0 means that the ping was successful
        if ping_reply == 0:
            print("\n* {} is online!\n".format(ip))
            continue
        
        else:
            print('\n* {} cannot be reached!'.format(ip))
            sys.exit()