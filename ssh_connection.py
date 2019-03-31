import paramiko # might have to be installed 'pip install paramiko' - needed for SSH connection
import os.path
import time
import sys
import re

# As before with the server IPs we now ask for the SSH credentials
user_file = input("\n# Please enter SSH config file path (e.g. C:\ssh_credentials.env) ")

# Verifying the validity of the USERNAME/PASSWORD file
if os.path.isfile(user_file) == True:
    print("\n* Username/password file is valid\n")

else:
    print("\n* File {} does not exist!\n".format(user_file))
    sys.exit()
        
# Checking commands file
cmd_file = input("\n# Enter Commands file path (e.g. C:\commands.env): ")

# Verifying the validity of the COMMANDS FILE
if os.path.isfile(cmd_file) == True:
    print("\n* Command file is valid\n")

else:
    print("\n* File {} does not exist!".format(cmd_file))
    sys.exit()
    
#Open SSHv2 connection to the device
def ssh_connection(ip):
    
    # make login credentials and SSH commands available inside the function
    global user_file
    global cmd_file
    
    #Creating SSH CONNECTION
    try:
        # Set SSH login parameters from the file (username and password have to be on the same line, separated by a comma)
        selected_user_file = open(user_file, 'r')
        
        # Starting from the beginning of the file
        selected_user_file.seek(0)
        
        # Reading the username from the file by splitting the string by the separating comma  (see ./Python_Net_App_04.png)
        # we are additionally striping every new line character that might have found it's way into the file '.rstrip("\n")'
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")
        
        # Starting from the beginning of the file
        selected_user_file.seek(0)
        
        # Reading the password from the file
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")
        
        # Use SSH client from paramiko library to establish connection
        session = paramiko.SSHClient()
        
        # For testing purposes, this allows auto-accepting unknown host keys
        # Do not use in production! The default would be RejectPolicy()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the device using username and password          
        session.connect(ip.rstrip("\n"), username = username, password = password)
        
        # Start an interactive shell session on the router
        connection = session.invoke_shell()	
        
        # Hardcoded block - e.g. to start a program before running your commands
        # connection.send("enable\n")
        # connection.send("terminal length 0\n")
        # we are using the time module we imported at the beginning of the file to add a waiting period before continuing
        # time.sleep(1)
        
        # Hardcoded block - e.g. to start a program before running your commands
        # connection.send("\n")
        # connection.send("configure terminal\n")
        # time.sleep(1)
        
        # Open user selected file for reading
        selected_cmd_file = open(cmd_file, 'r')
            
        # Starting from the beginning of the file
        selected_cmd_file.seek(0)
        
        # Writing each line in the file to the device
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + '\n')
            time.sleep(2)
        
        # Closing the user file
        selected_user_file.close()
        
        # Closing the command file
        selected_cmd_file.close()
        
        # Checking command output for syntax errors
        server_response = connection.recv(65535)
        
        if re.search(b"% Invalid input", server_response):
            print("* There was at least one syntax error in the given command {}".format(ip))
            
        else:
            print("\nServer {} Response:\n".format(ip))
            
        # Test for reading command output
        # print(re.findall(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", str(server_response))[3])
        print(str(server_response) + "\n")
        
        # Closing the connection
        session.close()
     
    except paramiko.AuthenticationException:
        print("* Invalid username or password \n* Please check the username/password file or the device configuration.")
        print("* Closing program...")