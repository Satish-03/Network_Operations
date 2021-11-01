#! /usr/bin/python3
#Importing necesaary modules to call functions
from cssh import cssh_connect, save_config, ping_test

#All functions that organize code go here
#Define a funtion to configure a device and ask appropriate inputs
def configure():
    print("-"*120)
    dev_ip = input("Enter your device IP you want to push your configurations: ")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    cmd_file = input("Enter the config commands file name: ")
    return dev_ip, username, password, cmd_file

#Define a funtion to check the ping connectivity and ask foe device IP
def ping_check():
    print("-"*120)
    dev_ip = input("Enter your device IP to check the IP connectivity: ")
    return dev_ip

#Define a funtion to save the configs and ask appropriate inputs
def saveconf():
    print("-"*120)
    dev_ip = input("Enter your device IP you want to save your configurations: ")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")
    return dev_ip, username, password

#At the end, the main function encapsulates the core logic
def main():
    usr_input = input('''Please select the approriate option from the options mentioned below to perform the task \n 
1) Configure a device 2) Check the IP connectivity of a device 3) Save the configuration\n\nYour input: ''')
    if usr_input == '1':
        ip, user, passd, cmdfile = configure()
        cssh_connect(ip, user, passd, cmdfile)
    elif usr_input == '2':
        ip = ping_check()
        ping_test(ip)
    elif usr_input == '3':
        ip, user, passd = saveconf()
        save_config(ip, user, passd)
    else:
        print("\noopsy!!! Invalid Input :( Try again!")

if __name__ == "__main__":
    main()