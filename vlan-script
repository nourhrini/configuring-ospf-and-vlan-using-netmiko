from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
# getting user's crededentials for SSH
username=input('enter ur ssh username: ')
password=getpass()
# devices_file is expected to contain the IP addresses of the devices we want to configure, each IP in a separate line.
with open('devices_file') as f:
    devices_list=f.read().splitlines()
for device in devices_list:
    print("connecting to: "+device)
    ip_addr=device
    cisco_sw = {
    'device_type': 'cisco_ios',
    'host':   ip_addr,
    'username': username,
    'password': password,
     }
    try:
        net_connect=ConnectHandler(**cisco_sw)
    except (AuthenticationException, NetMikoTimeoutException, SSHException, Exception) as error:
        print(f"Failed to connect to {device}: {error}")
        continue

    num=int(input('how many vlans you want to configure in this switch?'))
#creating the syntax for configuring vlans using user's input
    for i in range(num):
        vlan_num=input('enter vlan number: ')
        vlan_name=input('enter vlan name:')
        vlan_command1='vlan '+vlan_num
        vlan_command2='name '+vlan_name
        config_commands=[vlan_command1,vlan_command2]
        print('what interfaces you want to be access ports for this vlan?')
        while True:
            int_name=input()
            if int_name=='':
                break
            config_commands.append(f'interface {int_name}')
            config_commands.append('switchport mode access')
            config_commands.append(f'switchport access vlan {vlan_num}')
        output=net_connect.send_config_set(config_commands)
        print(f'vlan {vlan_name} configured successfully')
        
            
