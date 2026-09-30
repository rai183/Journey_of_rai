import random

print("NUMBER GUESSING GAME")
print("_______________________")

random_value = random.randint(1, 5)
tries = 0 
tuloy = True

while tuloy == True:
    num = eval(input("Guess the number from 1 to 5 --> "))
    tries += 1
    if num == random_value:
        print("WINNER!!!")
        break
    else:
        print("Wrong Guess Try Again:<")
        continue

print(f" Hi, you guess is correct. The number of tries {tries}")