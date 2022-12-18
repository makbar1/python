myDict = {"1": 34, "key1": 35, 
          "key2": 55, 1:40,
          True: 45, False: 34}

counter = 0
for k in myDict.keys():
    if isinstance(k, str):
        counter += 1
print(counter)