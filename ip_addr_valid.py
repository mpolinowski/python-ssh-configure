import sys

#Checking octets
def ip_addr_valid(list):
    # for-loop over all IPs inside the config file
    for ip in list:
        # Every IP had to be written on a new line inside the file so we now have to strip the \n newline character
        ip = ip.rstrip("\n")
        # To see if they are valid IP we split each octet at the . (see ./Python_Net_App_01.png)
        octet_list = ip.split('.')
        # Max 4 octets
        # First octet has to be between 1 and 223, may not be 127 or 169 (reserved IP space)
        # Second octet cannot be 254 (reserved IP space) but has to be between 0-255
        # Between the 1st and 2nd octet we have to use the OR operator to allow for addresses like 169.253.1.1, 10.254.1.1 - only 169.254.x.x is restricted (see ./Python_Net_App_02.png)
        # All other cases have AND conditions
        # Third and Fourth octet has to be between 0-255
        if (len(octet_list) == 4) and (1 <= int(octet_list[0]) <= 223) and (int(octet_list[0]) != 127) and (int(octet_list[0]) != 169 or int(octet_list[1]) != 254) and (0 <= int(octet_list[1]) <= 255 and 0 <= int(octet_list[2]) <= 255 and 0 <= int(octet_list[3]) <= 255):
            continue
             
        else:
            print('\n* Invalid IP address added: {} :(\n'.format(ip))
            sys.exit()