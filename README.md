This repo contain three projects, one for configuring OSPF, one for configuring vlans and one for backing up devices. all using netmiko library.
both projects prompt the user to enter the specefications for OSPF/vlan/backup without the need to enter any commands.


![ospf script](https://github.com/user-attachments/assets/15182273-5993-4038-82f3-abe3d5411cbc)
![vlan script](https://github.com/user-attachments/assets/0fdae2b6-6a9c-4417-890b-522214efb8ec)


for example the user can choose the process id and area number for OSPF and the ospf will be created with those specefications, same things with vlan, the user choose the vlans and their names and interfaces and they'll be created automatically.
The backup script loop across all devices giving you the option to backup the device or not.
if you have any notes or improvments please let me know.
