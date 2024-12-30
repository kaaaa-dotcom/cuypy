import random
from time import sleep

while True:
 mylist = [1,2,3,4,5]
 act = random.choice(mylist)
 act2 = random.sample(mylist,2)
 i = input("Continue\nBack\n\n[C or B]")
 if i == "C":
  print('Sekarang aku di',act)
  print('dan juga di',act2)
  sleep(2.5)
 elif i == "B":
  break
 else:
  print("Ngetik yang bener bego")