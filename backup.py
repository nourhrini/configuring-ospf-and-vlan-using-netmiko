from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException
username=input('enter ur ssh username: ')
password=getpass()
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
    backup=input('would you like to backup: '+ip_addr+' ?(yes/no)').lower()
    if backup=='yes' or 'y':
        running_config = net_connect.send_command('show running-config')
        with open(f'running_config_for{ip_addr}.txt', 'w') as file:
            file.write(running_config)
        print('device: '+ip_addr+' backupped successfully')
    elif backup=='no' or 'n':
        print("device "+ip_addr+' was skipped')
