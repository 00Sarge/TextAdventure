import math
def askNum():
   failure = True
   while failure:
      userInput = input("Please give a number")
      if int(userInput) < 10:
         print("number is too low, try again")
      elif int(userInput) > 20:
         print("number is too high, try again")
      else:
         answer = math.sqrt(int(userInput))
         print(answer)
         failure = False
askNum()