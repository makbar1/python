import os

files = []

for file in os.listdir():
    if file == "network_chuck1.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)
