import subprocess
x=input("enter a mac address : ")
y=input("which mac address your want to change eth0 OR wlan0 : ")
subprocess.run(["sudo","ifconfig",y,"down"]) 
subprocess.run(["ifconfig", y , "hw", "ether", x])
subprocess.run(["ifconfig",y,"up"])

print("macaddress changed successfully")