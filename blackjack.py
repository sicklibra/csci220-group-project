"""names
  1:Josh Hodges
  2:Conner E.
  3:Carter Wilcox
  4:Colin Wade
  Problem/ solution:
  This project is to create a black-jack program that will run six hands before asking the user to continue and shuffling the deck
  the deck will be referenced by place and suit in a list that will be manipulated for actual game play that will be conducted via graphic interface."""

import random
import math
def play():
    deckmain= ["1d", "1h", "1s", "1c", "2d", "2h", "2s", "2c", '3d', '3h', '3s', '3c', '4d', '4h', '4s', '4c', '5d', '5h', '5s', '5c', '6d', '6h', '6s', '6c', '7d', '7h', '7s', '7c', '8d', '8h', '8s', '8c', '9d', '9h', '9s', '9c', '10d' ,'10h', '10s', '10c', '11d', '11h', '11s', '11c', '12d', '12h', '12s', '12c', '13d', '13h', '13s', '13c']
    deckuse=deckmain
    #this will contain the whole game
    for i in range (3):
      #initial deal
      deckuse,d1,d2,p1,p2=deal(deckuse)
      #  print(deckuse)
      #  print(d1,d2,p1,p2)
      setup(deckuse,d1,d2,p1,p2)

def setup(deckuse,d1,d2,p1,p2):
  #assignment of values
  dealertot=0
  playertot=0
  dealhand=[d1,d2]
  playerhand=[p1,p2]
  ph1=playerhand
  ph2=[]
  ph3=[]
  ph4=[]
  splithands=[ph1,ph2,ph3,ph4]
  handnum=0
  print('The dealers hand is',dealhand)
  print("Your hand is: ", playerhand)
  #splits the hand
  handnum=splitTree(splithands, deckuse, handnum)
  playhand(ph1, deckuse, dealhand)
  if ph2!=[]:
     handnum=splitTree(splithands, deckuse, handnum)
     playhand(ph2 deckuse, dealhand)
  if ph3!=[]:
     handnum=splitTree(splithands, deckuse, handnum)
     playhand(ph2 deckuse, dealhand)
  if ph4!=[]:
    #im only allowing exact match cards to split(not all 10's)
     playhand(ph2 deckuse, dealhand)
  #if hand can't be split, just play the hand.      
  else:
    playhand(playerhand,deckuse, dealhand)
        #generate values of cards
  # for i in dealhand:
  #   i=cardValue(i)
  # # gets the numeric value for the card     
  # #possibly make this it's own function to iterate for splits
  # for i in playerhand:
  #   i=cardValue(i)
  # #initialize boolean statements for the hand

def playhand(hand, deckuse, dealhand):
  #set conditions that would cause end of hand activity
  bust=False
  stay=False
  blackjack=False
  handtotal=0
  dhtot=cardValue(dealhand)
  #actual bame play
  while stay==False and bust==False and blackjack== False:
     #display hands that have been 
    print("The dealers hand is : x",dealhand[:-1])
    print("\n Your hand is: ", hand)
    if hand.count('ace')==1:
       hand[hand.index('ace')]=11
       

def splittest(hand):
  test=[]
    #split test
  for i in hand:
    if len(i)==3:
      test.append(int(i[0:1]))
    else:
      test.append(int(i[0]))
    if test[0]==test[1]:
      choice=input('Would you like to split?Y/N')
      if choice=="Y" or choice=="y":
         return True
      else:
        return False


def splitTree(splithands, deckuse, handnum):
  split=splithands[handnum]
  if split==True:
     splithands[handnum+1]=[splithands[handnum[1]]]
     splithands[handnum]=[splithands[handnum[0]]]
     hit(splithands[handnum])
     return handnum+1
        
           

def cardValue(card):
    if len(card)==3:
        return 10
    elif int(card[0])>1:
        return card[0]
    elif int(card[0])==1:
        return "ace"

def hit(hand,deckuse):
    hitcrd=random.choice(deckuse)
    hand.append(hitcrd)
    place=deckuse.index(hitcrd)
    del(deckuse[place])
    
        

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


#different ways ive tried running the split tree function

  # split==True
  # counter=0
  # #variable to account for multiple splits on same iteration.
  # multi=1
  # # for i in range(splithands):
  #   #tests to see if splitable and if user wants to.
     
  # while split==True:
  #   #tests and prompts if the hand can and will be split
  #   split=splittest(splithands[counter])
  #   #will take the second card of the current hand,and assign it to first card slot of next hand
  #   splithands[multi]=[splithands[counter[1]]]
  #   #resets the first hand with a single card(the first in the current two card list.)
  #   splithands[counter]=splithands[counter[0]]
  #   #adds card to the new first hand
  #   hit(splithands[counter], dealhand)
  #   #hand to be tested as it works down the chain:
  #   recheck=splittest(splithands[counter])
  #   #if new hand can be split, it sends the next hand to be changed to the target of the split 
  #   if recheck==True:
  #      multi+=1
  #   #moves up to the next hand in the list if cant resplit first hand. 
  #   else:
  #      counter+=1
  # if hand3==0:
  #   hand3=[hand2[1]]
  #   hand2=[hand2[0]]
  #   hit(hand2, deckuse)
  #   return hand2,hand3,hand4
  # if hand4==0:
  #    hand4=[hand3[1]]
  #    hand3=[hand3[0]]
  #    hit(hand3, deckuse)
  #    return hand2, hand3, hand4  