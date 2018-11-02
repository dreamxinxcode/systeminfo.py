import os
import platform
import psutil
import socket

class bold:
    on = "\033[1m"
    off = "\033[0m"

mem=psutil.virtual_memory()

model = open("/sys/devices/virtual/dmi/id/product_version").read()

with open("/sys/class/thermal/thermal_zone0/temp") as tempfile:
    temp=tempfile.read()

user=os.getlogin()
host=platform.node()
print(bold.on + user + "@" + host + bold.off + "\n")
print(bold.on + "OS: " +  bold.off + platform.system() + " " + platform.release())
print(bold.on + "Kernel: " + bold.off + platform.release())
print(bold.on + "Model:" + bold.off + " " + model)
print(bold.on + "Platform: " +  bold.off + platform.platform())
print(bold.on + "Processor: " +  bold.off + platform.processor())   
print(bold.on + "Compiler: " +  bold.off + platform.python_compiler()) 
print(bold.on + "Python: " +  bold.off + "Version " + platform.python_version())
print(bold.on + "Local IP: " + bold.off + socket.gethostbyname(socket.gethostname()) + " " + socket.getfqdn())
#print(psutil.sensors_temperatures())
#print(platform.dist())
#print(bold.on + "Disk (/): " + bold.off + mem.total)            
#print(psutil.disk_usage("/dev/sda"))
