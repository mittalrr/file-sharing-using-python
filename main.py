# py -m http.server [OPTIONAL_PORT_NUMBER]



import os
os.system('cmd /k "py -m http.server"')




''' 
1) Place this file in the directory that you want to share
2) This would then launch the server @ : http://localhost:8000/
3) Now to access the contents using some other devices like your PC or Android Phone find the ip address of your laptop or the host system by typing in "ipconfig" in the command prompt.
4) Then look for the ipv4 address, it will be of the form 192.168.x.x 
5) Now in your mobile browser type the following link <above_ip_address>:<port_number> example 192.168.2.104:8000
6) Now you are ready to instantly access files of your laptop into your phone!
'''