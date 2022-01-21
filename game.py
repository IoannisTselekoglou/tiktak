import numpy as np

list1 = [0,0,0,0,0,0,0,0,0]

def gamefield():
  return np.array(list1).reshape(3,3)




def gamelogic(number):
  if list1[number] == 0: 
    return True
  else:
    return False

def move(number):
  while number > 9 or number < 1:
    print("invalid input, type an intiger number between 1-9 each representing one position on the board where u want to make an cross\n ")
    while gamelogic(number)== False and list1[number] == 1:
      number = input("type number bitch\n ")
      if gamelogic(number) and list1[number] != 1:
        list1[number]
        botmove()


def botmove():
  botnumber = random.randrange(1,9,1) 
  while gamelogic(botnumber)== False and list1[botnumber] == 1:
    botnumber = random.randrange(1,9,1) 
    if gamelogic(botnumber) and list1[botnumber] != 1:
      list1[botnumber]

print(gamefield())

move(input("Type in number, representing spot on playingfield\n "))


print(gamefield())





