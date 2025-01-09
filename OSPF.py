from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

# extracting crededentials for SSH
username=input('enter ur ssh username: ')
password=getpass()

# devices_file is expected to only contain IP addresses of the devices you want to configure, each IP in separate line
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
    #asking the user to enter ospf process ID and area 
    ospfprocid = input('OSPF Process ID #: ')
    area_id = input('Area ID: ')
  # creating the command syntax 
    routerospf = 'router ospf ' + ospfprocid
    config_commands=[routerospf]
    output=net_connect.send_command('show ip int brief')
    lines=output.splitlines()[1:] #removing first line of the sh ip int br output since we wouldn't need it
  #configuring OSPF network command for the networks for each interface  
  for line in lines:
        x=line.split()
        if (x[1] == 'IP-Address') or (x[1] == 'unassigned'):
            continue
        else:
            network='network '+x[1] +' 0.0.0.0 area '+area_id
            config_commands.append(network)
          # prompting the user to choose wether each interface will be passive or not
            is_passive= input(f'is interface {x[0]} passive? (yes/no)').lower()
            if is_passive=='yes':
                passive_int='passive-interface ' + x[0]
                config_commands.append(passive_int)
            output=net_connect.send_config_set(config_commands)
    print('router '+device+' configured')    
