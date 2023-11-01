"""names
  1:Josh Hodges
  2:Conner E.
  3:Carter Wilcox
  4:Colin Wade
  Problem/ solution:
  This project is to create a black-jack program that will run six hands before asking the user to continue and shuffling the deck
  the deck will be referenced by place and suit in a list that will be manipulated for actual game play that will be conducted via graphic interface."""

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
  
    
  
