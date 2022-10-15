
import random

while True:
    i=input("Roll[R] or Quit[Q] : ")
    i=i.capitalize()
    if i=="R":
        print(random.randint(1,6))
    
    elif i=="Q":
        break

    else:
        print("\tPlease enter R or Q")

print("Thanks For using Dice stimulator")
