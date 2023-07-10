import random
from enum import Enum

# 카드 클래스 생성
class suitEnum(Enum):
    SPADE = 0
    HEART = 1
    DIAMOND = 2
    CLUB = 3

# 카드 클래스 생성
class Card:
    def __init__(self):
        self.suit = "UND"
        self.num = 0
        self.state = "unmatch"
        self.shape = []

    def setState(self, state:str):
        self.state = state

    def draw(self):
        pass

    # decorator를 위한 함수
def makedraw(card:Card):
    card.draw()

class Player:
    def __init__(self):
        self.amount = 100
    
    # decorator를 위한 함수
def makedraw(card:Card):
    card.draw()

# main문 
player = Player()
com_money = 200


# 카드 표시
class Deco(Card):
    def __init__(self, card:Card):
        self.card = card
    def draw(self):
        self.card.draw()

# 카드 표시
class matchCard(Deco):
    def draw(self):
        if self.card.num >= 10:
            self.card.shape[0] = "###########"
            self.card.shape[1]="#         #"
            self.card.shape[2]="#    " + self.card.suit + "    #"
            self.card.shape[3]="#    " + str(self.card.num) + "   #"
            self.card.shape[4]="#         #"
            self.card.shape[5]="###########"    
        else:
            self.card.shape[0]="###########"
            self.card.shape[1]="#         #"
            self.card.shape[2]="#    " + self.card.suit + "    #"
            self.card.shape[3]="#    " + str(self.card.num) + "    #"
            self.card.shape[4]="#         #"
            self.card.shape[5]="###########"     
    
# 카드 표시
class unmatchCard(Deco):
    def draw(self):
        if self.card.num >= 10:
            self.card.shape[0]="-----------"
            self.card.shape[1]="|         |"
            self.card.shape[2]="|    " + self.card.suit + "    |"
            self.card.shape[3]="|    " + str(self.card.num) + "   |"
            self.card.shape[4]="|         |"
            self.card.shape[5]="-----------"    
        else:
            self.card.shape[0]="-----------"
            self.card.shape[1]="|         |"
            self.card.shape[2]="|    " + self.card.suit + "    |"
            self.card.shape[3]="|     " + str(self.card.num) + "   |"
            self.card.shape[4]="|         |"
            self.card.shape[5]="-----------" 

while(player.amount > 0 and com_money > 0):
    print("----------------new game----------------")
    betting = 0
    print("---------------making deck--------------")
    # make deck
    deck = list() 
    fac = factory()
    for i in range(1, 14):
        deck.append(fac.makecard(suitEnum.SPADE, i))
    for i in range(1, 14):
        deck.append(fac.makecard(suitEnum.HEART, i))
    for i in range(1, 14):
        deck.append(fac.makecard(suitEnum.DIAMOND, i))
    for i in range(1, 14):
        deck.append(fac.makecard(suitEnum.CLUB, i))
    # make cards...
    print("--------------shuffle deck---------------")
    # random.shuffle(deck)
    print("----------------your hand----------------")
    # print player's hand card
    print("-----------------------------------------")
    # print player's rank
    # print player's and com's money

    print("if you want betting, please insert amount? (-1 is Fold) :")
    # input batting amount
    TB = int(input())
    if TB < 0:
        print("---------------you fold---------------")
        break
    if betting+TB >player.amount:
        print("you can't betting more than your money!!")
    else:
        betting = betting + TB
        

    print("----------------2nd turn----------------")
    # add card
    print("----------------your hand----------------")
    # repeat 
    print("-----------------------------------------")
    print("if you want betting, please insert amount? (-1 is Fold) :")
    TB = int(input())
    if TB < 0:
        print("---------------you fold---------------")
        continue
    if betting+TB >player.amount:
        print("you can't betting more than your money!!")
    else:
        betting = betting + TB
    
    print("----------------last turn----------------")
    # add cord
    print("----------------your hand----------------")
    # repeat
    print("-----------------------------------------")    
    print("if you want betting, please insert amount? (-1 is Fold) :")
    TB = int(input())
    if TB < 0:
        print("---------------you fold---------------")
        continue
    if betting+TB >player.amount:
        print("you can't betting more than your money!!")
    else:
        betting = betting + TB

    print("---------------result-------------------")
    print("----------------your hand----------------")
    # show player's card and rank
    print("-----------------------------------------")
    
    print("----------------com hand----------------")
    # show com's card and rank
    print("-----------------------------------------")  
    # print win or lose or draw 
        
    if player.amount > 0:
        if com_money <= 0:
            input("----Finally You Win!! Congratulation----")
        input("press enter to next game")
    else:
        input("----Finally You Lose!! Try Again Later----")
