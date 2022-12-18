import math

for num in range(2, 11):
  #  if all(num %i !=0 for i in range(2, int(math.sqrt(num)) +1)):
  #     print (num)
	#if num % i != 0:
		for i in range(2, int(math.sqrt(num)) + 1):
			#if num % i != 0:
			print(num, i)