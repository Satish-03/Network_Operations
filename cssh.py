#! /usr/bin/python3
#Importing necesaary modules to call functions
from netmiko import ConnectHandler
from netmiko.ssh_exception import AuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from icmplib import ping

#All functions that organize code go here
#Function to ssh and configur a device
def cssh_connect(ip, username, passwd, cmd_file):
    try:
       print("-"*120)

       print('\nGetting into: {}\n'.format(ip))
       Device = {'ip':ip,
                      'username':username,
                      'password':passwd,
                      'secret':'Lab123', 
                      'device_type':'cisco_ios',
               }
        #Establishing ssh connection
       connection = ConnectHandler(**Device)
       print(f"We are able to login into {ip} with username {username} and password {passwd} you entered\n")
       #getting into enable mode
       connection.enable()
       #Getting hostname
       host = connection.find_prompt()
       hname = host.strip('#')
       #configuring device 
       confout = connection.send_config_from_file(config_file=cmd_file)
       print(confout+'\n')
       #getting output from show command
       intbrief = connection.send_command('sh ip int b')
       print(intbrief)
       connection.save_config()
       #Disconnecting from the current device
       connection.disconnect() 
       print(f"\nAll the configurations have been pushed into '{hname}' successfully")
       print("-"*120)
    except (AuthenticationException):
       print("Oops! Authentication fails    Try again....")
    except (NetMikoTimeoutException):
       print("Session timed out....Try again")

#Function to ssh and save the configs
def save_config(ip, username, passwd):
    try:
       print("-"*120)

       print('\nGetting into: {}\n'.format(ip))
       Device = {'ip':ip,
                      'username':username,
                      'password':passwd,
                      'secret':'Lab123', 
                      'device_type':'cisco_ios',
               }
       connection = ConnectHandler(**Device)
       print(f"We are able to login into {ip} with username {username} and password {passwd} you just entered\n")
       connection.enable()
       print("Saving configs.....")
       startup_config = connection.send_command('sh startup-config')
       #Disconnecting from the current device
       connection.disconnect() 
       with open("startupconfig.txt", 'w') as f:
           f.write(startup_config)
       print("\nAll the startup config have been saved into a text file successfully")
       print("-"*120)
    except (AuthenticationException):
       print("Oops! Authentication fails    Try again....")
    except (NetMikoTimeoutException):
       print("Session timed out....Try again")

def ping_test(ip):
       print("-"*120)
       print("Checking connectivity.....hold on\n")
       test = ping(ip, privileged = False)
       if test.packet_loss == 0.0:
           print(f"Device with IP {ip} is reachable :)")
       else:
           print("Oops! Device is unreachable :( Is you network connection fine?")

#At the end, the main function encapsulates the core logic
def main():
    cssh_connect()

if __name__ == "__main__":
    main()