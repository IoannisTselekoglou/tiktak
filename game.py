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
  print(gamefield())
  return botmove()



def botmove():
  botnumber = random.randint(1,9) 
  while list1[botnumber-1] == (1 or 2):
    botnumber = random.randint(1,9) 
    if gamelogic(botnumber) and list1[botnumber - 1] == 0:
      list1[botnumber-1] = 2
  print(gamefield())
  return move(int(input("Your Turn, Bitch \n"))) 

move(int(input("Type in number, representing spot on playingfield\n ")))








