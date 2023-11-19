
import random
import tkinter
from tkinter import PhotoImage, StringVar
from PIL import Image, ImageTk
#window
app= tkinter.Tk()
app.title("War")
app.geometry('900x500')
app.configure(background='green')
#Frame
mainframe = tkinter.Frame(app,background='green')
mainframe.pack(pady=20)
#Frames for Cards
dealer_frame = tkinter.LabelFrame(mainframe, text = "Dealer",border=0)
dealer_frame.pack(padx=20)
player_frame= tkinter.LabelFrame(mainframe, text ="Player",border=0)
player_frame.pack(pady=20)

#Cards in Frames
dealer_label = tkinter.Label(dealer_frame, text='')
dealer_label.pack(pady=20)

player_label = tkinter.Label(player_frame, text='')
player_label.pack(pady=20)

#Resize Cards
def resize_cards(card):
    #Open Image
    global card_img
    card_img = Image.open(card)
    #Resize
    card_img_resize = card_img.resize((150,218))
    #Output Card
    card_img = ImageTk.PhotoImage(card_img_resize)
    #Return Card
    return card_img
#Deal Cards
def getcards():
    suit = ["heart","diamond","spade","club"]
    value = ["2","3","4","5","6","7","8","9","10","11","12","13","14"]
    global deck
    deck = []
    for i in range (2):
            deck.append(f'{random.choice(suit)}{random.choice(value)}')
    #Players
    print(deck)

    dealer = []
    player = []

    #Grab a Random Card
    card = deck[0]
    dealer.append(card)
    global dealer_image
    dealer_image = resize_cards(f'{card}')
    dealer_label.config(image=dealer_image)

    card=deck[-1]
    player.append(card)
    global player_image
    player_image = resize_cards(f'{card}')
    player_label.config(image=player_image)

#Create Buttons
deal_button = tkinter.Button(mainframe, text="Deal",command=getcards)
deal_button.pack(pady=20)



# all heart cards
heart2=PhotoImage(file="2_of_hearts.png")
heart3=PhotoImage(file="3_of_hearts.png")
heart4=PhotoImage(file="4_of_hearts.png")
heart5=PhotoImage(file="5_of_hearts.png")
heart6=PhotoImage(file="6_of_hearts.png")
heart7=PhotoImage(file="7_of_hearts.png")
heart8=PhotoImage(file="8_of_hearts.png")
heart9=PhotoImage(file="9_of_hearts.png")
heart10=PhotoImage(file="10_of_hearts.png")
heart11=PhotoImage(file="11_of_hearts.png")
heart12=PhotoImage(file="12_of_hearts.png")
heart13=PhotoImage(file="13_of_hearts.png")
heart14=PhotoImage(file="14_of_hearts.png")

#all 14 diamonds
diamond2=PhotoImage(file="2_of_diamonds.png")
diamond3=PhotoImage(file="3_of_diamonds.png")
diamond4=PhotoImage(file="4_of_diamonds.png")
diamond5=PhotoImage(file="5_of_diamonds.png")
diamond6=PhotoImage(file="6_of_diamonds.png")
diamond7=PhotoImage(file="7_of_diamonds.png")
diamond8=PhotoImage(file="8_of_diamonds.png")
diamond9=PhotoImage(file="9_of_diamonds.png")
diamond10=PhotoImage(file="10_of_diamonds.png")
diamond11=PhotoImage(file="11_of_diamonds.png")
diamond12=PhotoImage(file="12_of_diamonds.png")
diamond13=PhotoImage(file="13_of_diamonds.png")
diamond14=PhotoImage(file="14_of_diamonds.png")

#all 14 spades
spade2=PhotoImage(file="2_of_spades.png")
spade3=PhotoImage(file="3_of_spades.png")
spade4=PhotoImage(file="4_of_spades.png")
spade5=PhotoImage(file="5_of_spades.png")
spade6=PhotoImage(file="6_of_spades.png")
spade7=PhotoImage(file="7_of_spades.png")
spade8=PhotoImage(file="8_of_spades.png")
spade9=PhotoImage(file="9_of_spades.png")
spade10=PhotoImage(file="10_of_spades.png")
spade11=PhotoImage(file="11_of_spades.png")
spade12=PhotoImage(file="12_of_spades.png")
spade13=PhotoImage(file="13_of_spades.png")
spade14=PhotoImage(file="14_of_spades.png")

#all 14 clubs
club2=PhotoImage(file="2_of_clubs.png")
club3=PhotoImage(file="3_of_clubs.png")
club4=PhotoImage(file="4_of_clubs.png")
club5=PhotoImage(file="5_of_clubs.png")
club6=PhotoImage(file="6_of_clubs.png")
club7=PhotoImage(file="7_of_clubs.png")
club8=PhotoImage(file="8_of_clubs.png")
club9=PhotoImage(file="9_of_clubs.png")
club10=PhotoImage(file="10_of_clubs.png")
club11=PhotoImage(file="11_of_clubs.png")
club12=PhotoImage(file="12_of_clubs.png")
club13=PhotoImage(file="13_of_clubs.png")
club14=PhotoImage(file="14_of_clubs.png")


def testing():
    dealer_label['image']=heart4
    player_label['image']=club13
testing()
######## end ########
'''getcards()'''
app.mainloop()