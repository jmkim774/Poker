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

#spade_card

class SCard(Card):
    def __init__(self, num):
        self.suit = chr(9824)
        self.shape = [0 for i in range(6)]
        self.num = num
        self.state = "unmatch"

#heart_card

class HCard(Card):
    def __init__(self, num):
        self.suit = chr(9829)
        self.shape = [0 for i in range(6)]
        self.num = num
        self.state = "unmatch"

#diamond_card

class DCard(Card):
    def __init__(self, num):
        self.suit = chr(9674)
        self.shape = [0 for i in range(6)]
        self.num = num
        self.state = "unmatch"

#clover_card

class CCard(Card):
    def __init__(self, num):
        self.suit = chr(9827)
        self.shape = [0 for i in range(6)]
        self.num = num
        self.state = "unmatch"

class Player:
    def __init__(self):
        self.amount = 100
    
    # decorator를 위한 함수
def makedraw(card:Card):
    card.draw()

# check flush
def isflush(cards):
    SFcount, HFcount, DFcount, CFcount = 0, 0, 0, 0
    for i in range(len(cards)):
        if cards[i].suit == chr(9824):
            SFcount += 1
        elif cards[i].suit == chr(9829):
            HFcount += 1
        elif cards[i].suit == chr(9674):
            DFcount += 1
        elif cards[i].suit == chr(9827):
            CFcount += 1
        if SFcount >= 5:
            for j in cards:
                if j.suit == chr(9824):
                    j.state = "match"
            return True
        elif HFcount >= 5:
            for j in cards:
                if j.suit == chr(9829):
                    j.state = "match"
            return True
        elif DFcount >= 5:
            for j in cards:
                if j.suit == chr(9674):
                    j.state = "match"
            return True
        elif CFcount >= 5:
            for j in cards:
                if j.suit == chr(9827):
                    j.state = "match"
            return True
          
# straight 판별 함수
def isstraight(cards):
    nlist = []
    for i in cards:
        nlist.append(i.num)
    nlist.sort()
    for i in range(len(nlist)):
        count = 0
        for j in range(i, len(nlist)):
            if nlist[j] == 0 and nlist[j - 1] == 11:
                count += 1
            if count == 5:
                for k in cards:
                    if k.num in [nlist[j], nlist[j-1], nlist[j-2], nlist[j-3], nlist[j-3]] :
                        k.state = "match"
                return True
    return False

# main문 
player = Player()
com_money = 200


# 카드 표시
class Deco(Card):
    def __init__(self, card:Card):
        self.card = card
    def draw(self):
        self.card.draw()

while(player.amount > 0 and com_money > 0):
    print("----------------new game----------------")
    betting = 0
    print("---------------making deck--------------")
    # make deck...
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
