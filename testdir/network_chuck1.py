import os

from cryptography.fernet import Fernet

files = []

os.chdir("testdir")

for file in os.listdir():
    if file == "network_chuck1.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        files.append(file)

#print(files)
print(os.getcwd())

key = Fernet.generate_key()
#print(key)

with open("thekey.key", "wb") as thekey:
    thekey.write(key)

