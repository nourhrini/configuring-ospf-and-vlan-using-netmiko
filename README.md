This repo contain four projects, one for configuring OSPF, one for configuring vlans, one for backing up devices and one for troubleshooting OSPF. all using netmiko library.
first three projects prompt the user to enter the specefications for OSPF/vlan/backup without the need to enter any commands.


![ospf script](https://github.com/user-attachments/assets/15182273-5993-4038-82f3-abe3d5411cbc)


![vlan script](https://github.com/user-attachments/assets/0fdae2b6-6a9c-4417-890b-522214efb8ec)


for example the user can choose the process id and area number for OSPF and the ospf will be created with those specefications, same things with vlan, the user choose the vlans and their names and interfaces and they'll be created automatically.
The backup script loop across all devices giving you the option to backup the device or not.
the OSPF troubleshooting script looks for inconsistancies withen: hello timer,dead timer and network type and check for duplicate router-id, then print a report of collected values that include warnings for error in the mentioned values.

![tr](https://github.com/user-attachments/assets/57bf602a-eaf4-402b-ab5e-bd7d8aca524f)

if you have any notes or improvments please let me know.
