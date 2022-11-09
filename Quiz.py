import math

def checkNum (number):
    number = int(number)
    if number < 10:

        print("number too low")

    elif number > 20:

        print("number too high")

    else:

        answer = math.sqrt(number)
        print(answer)

 
while True:
    number = input("Please enter a number  ")
    checkNum(number)