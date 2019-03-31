import os.path
import sys

# To connect to the server we want to have the user add a file with the login info
def ip_file_valid():

    # Ask for the config file location holding the IP addresses of your servers
    ip_file = input("\n# Please enter Server IPs config file path (e.g. C:\server_ips.env): ")

    # Use the internal python function os.path to check if the file exists, otherwise exit
    if os.path.isfile(ip_file) == True:
        print("\n* File accepted\n")
    
    else:
        print("\n* {} Not found!\n".format(ip_file))
        sys.exit()

    # Open file for reading
    selected_ip_file = open(ip_file, 'r')
    
    # Start reading from the beginning
    selected_ip_file.seek(0)
    
    # Reading each line - has to be 1 IP address per line file - and write it into a variable
    ip_list = selected_ip_file.readlines()
    
    # Close file
    selected_ip_file.close()
        
    # Return the list of IP addresses
    return ip_list