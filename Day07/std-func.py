#
# Standard Python Library
# https://docs.python.org/3/library/
#
import os

print("Biezacy folder:", os.getcwd())
print("Listowanie:", os.listdir("."))
if not os.path.exists("tmp"):
    os.mkdir("tmp")
else:
    print("podfolder 'tmp' juz jest")
    os.removedirs("tmp")


import shutil
shutil.copy("json.txt", "json-kopia.txt")
disk = shutil.disk_usage(".")
print(disk)

curr_dir = os.getcwd()
#new_dir = curr_dir + "\\tmp" - bedzie dzialac tylko w Windows
new_dir = os.path.join(curr_dir, "tmp")
print("OS:",os.name)
print("separator katalogow: ",os.sep)
print(new_dir)

# windows - c:\users\kowalski\Moje Dokumenty\plik.py
# macos/unix - /Users/marian/Downloads/plik.py

import platform
print("OS:",platform.system())
print("OS:",platform.architecture())
print("OS:",platform.processor())
print("OS:",platform.java_ver())