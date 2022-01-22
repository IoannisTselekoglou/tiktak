import numpy as np
import random
list1 = [0,0,0,0,0,0,0,0,0]

def gamefield():
  return np.array(list1).reshape(3,3)


def gamelogic(number):
  if number < 10 and number > 0 and list1[number - 1] == 0: 
    return True
  else:
    return False

def move(number):
  while number > 10 or number < 0:
    number = int(input("invalid input, type an intiger number between 1-9 each representing one position on the board where u want to make an cross\n "))
  if gamelogic(number) and list1[number-1] == (1 or 2):
      number = int(input("type number bitch\n "))
      move(number)
  elif gamelogic(number) and list1[number-1] != 1:
      list1[number-1] = 1
      if checkwinner():
        return print("congrats u won\n", gamefield())
  botmove()



def botmove():
  botnumber = random.randint(1,9) 
  if list1[botnumber-1] == 0:
    list1[botnumber-1] = 2
    if botwinner():
      return print("congrats bot wins \n", gamefield())
  else:
    while list1[botnumber-1] == (1 or 2):
      botnumber = random.randint(1,9) 
      botmove()
  print(gamefield())
  move(int(input("Your Turn, Bitch \n\n"))) 


def botwinner():
  if (list1[0] and list1[1] and list1[2]) == 2: 
    return True

  elif (list1[3] and  list1[4] and list1[5]) == 2: 
    return True

  elif (list1[6] and list1[7] and list1[8]) == 2: 
    return True

  elif (list1[0] and list1[3] and list1[6]) == 2: 
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

move(int(input("Type in number, representing spot on playingfield\n ")))
