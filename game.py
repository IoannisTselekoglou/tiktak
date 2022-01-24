import numpy as np
import random
list1 = [0,0,0,0,0,0,0,0,0]

def gamefield():
  return np.array(list1).reshape(3,3)


def move(number):
  while number > 10 or number < 0:
    number = int(input("To large, number needs to be 1-9\n"))
  if  list1[number-1] == (1 or 2):
    number = int(input("Spot taken\n"))
    move(number)
  elif list1[number-1] == 0:
    list1[number-1] = 1
    if checkwinner():
        return print("congrats u win\n", gamefield())
    botmove()


def botmove():
  botnumber = random.randint(1,9) 
  if list1[botnumber-1] == 0:
    list1[botnumber-1] = 2
    print(gamefield())
    if botwinner():
      return print("congrats bot wins \n", gamefield())
    move(int(input("Your turn\n"))) 
  elif list1[botnumber-1] == (1 or 2):
      botmove()



def botwinner():
  if (list1[0] and list1[1] and  list1[2]) == 2: 
    return True

  elif (list1[3] and  list1[4] and list1[5]) == 2: 
    return True

  elif (list1[6] and list1[7] and list1[8]) == 2: 
    return True

  elif (list1[0] and  list1[3]and list1[6]) == 2: 
    return True

  elif (list1[4] and list1[1] and list1[7]) == 2: 
    return True

  elif (list1[2] and list1[5] and list1[8]) == 2:
    return True

  elif (list1[0] and list1[4] and list1[8]) == 2:
    return True

  elif (list1[2] and list1[4] and list1[6]) == 2:
    return True

def checkwinner():
  if (list1[0] and list1[1] and list1[2]) == 1: 
    return True

  elif (list1[3] and  list1[4] and list1[5]) == 1: 
    return True

  elif (list1[6] and list1[7] and list1[8]) == 1: 
    return True

  elif (list1[0] and list1[3] and list1[6]) == 1: 
    return True

  elif (list1[4] and list1[1] and list1[7]) == 1: 
    return True

  elif (list1[2] and list1[5] and list1[8]) == 1: 
    return True

  elif (list1[0] and list1[4] and list1[8]) == 1: 
    return True

  elif (list1[2] and list1[4] and list1[6]) == 1: 
    return True

print(gamefield())
move(int(input("Type in number\n")))
