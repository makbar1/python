import os

files= []

for file in os.listdir():
    if file.endswith(".py"):
        continue
    files.append(file)
print(files)