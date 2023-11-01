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
  deckmain=[1d,1h,1s,1c,2d,2h,2s,2c,3d,3h,3s,3c,4d,4h,4s,4c,5d,5h,5s,5c,6d,6h,6s,6c,7d,7h,7s,7c,8d,8h,8s,8c,9d,9h,9s,9c,10d,10h,10s,10c,11d,11h,11s,11c,12d,12h,12s,12c,13d,13h,13s,13c

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
      start==1
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
        start==1
      else:
        #it would be cool if we could get a gif in here of the dude from tombstone saying this!
        print('Well, bye')
                 
    
    
  
