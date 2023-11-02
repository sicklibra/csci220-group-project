"""names
  1:Josh Hodges
  2:Conner E.
  3:Carter Wilcox
  4:Colin Wade
  Problem/ solution:
  This project is to create a black-jack program that will run six hands before asking the user to continue and shuffling the deck
  the deck will be referenced by place and suit in a list that will be manipulated for actual game play that will be conducted via graphic interface."""

import random

def play():
    deckmain= ["1d", "1h", "1s", "1c", "2d", "2h", "2s", "2c", '3d', '3h', '3s', '3c', '4d', '4h', '4s', '4c', '5d', '5h', '5s', '5c', '6d', '6h', '6s', '6c', '7d', '7h', '7s', '7c', '8d', '8h', '8s', '8c', '9d', '9h', '9s', '9c', '10d' ,'10h', '10s', '10c', '11d', '11h', '11s', '11c', '12d', '12h', '12s', '12c', '13d', '13h', '13s', '13c']
    deckuse=deckmain
    #this will contain the whole game
    for i in range (3):
       #initial deal
       deckuse,d1,d2,p1,p2=deal(deckuse)
       print(deckuse)
       print(d1,d2,p1,p2)

def playhand(deckuse,d1,d2,p1,p2):
        #assignment of values
        ace="1"
        

def deal(deckuse):
       #deal the first two cards for player and dealer.
       #face down
       d1=random.choice(deckuse)
       place=deckuse.index(d1)
       del(deckuse[place])
       #faceup
       p1=random.choice(deckuse)
       place=deckuse.index(p1)
       del(deckuse[place])
       d2=random.choice(deckuse)
       place=deckuse.index(d2)
       del(deckuse[place])
       p2=random.choice(deckuse)
       place=deckuse.index(p2)
       del(deckuse[place])

       return deckuse,d1,d2,p1,p2
       


def main():
  #opening statement determine if user wishes to play.
  start=input('Are you ready for some Blackjack?y/n: ')
  #by typing yes user initiates while loop.
  if start[0]=="y" or start[0]=="Y":
    start=1
  #second chance to play
  else:
    start=input('Are you sure?y/n: ')
    if start[0]=="y" or start[0]=="Y":
      start==2
    else:
      print('Well, bye')
      
  #loop will allow user to continue playing as many rounds as they like.
  while start==1:
    #play the game
    play()
    start= input("Would you like to shuffle and play another six hands?y/n:")
    if start[0]=="y" or start[0]=="Y":
        start=1
        #second chance to play
    else:
        start=input('Are you sure?y/n: ')
        if start[0]=="y" or start[0]=="Y":
            start=2
        else:
            #it would be cool if we could get a gif in here of the dude from tombstone saying this!
            print('Well, bye')
                 

main()