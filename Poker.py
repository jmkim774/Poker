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

# check pair
def ispair(cards):
    nlist = []
    for i in cards:
        nlist.append(i.num)
    nlist.sort()
    result = []

    for i in range(1, 14):
        if nlist.count(i) == 4:
            for j in cards:
                if j.num == i:
                    j.state = "match"
            result.append(4)
        elif nlist.count(i) == 3:
            for j in cards:
                if j.num == i:
                    j.state = "match"
            result.append(3)
        elif nlist.count(i) == 2:
            for j in cards:
                if j.num == i:
                    j.state = "match"
            result.append(2)
    if 4 in result:
        return 8
    elif 3 in result:
        if 2 in result:
            return 7
        else:
            return 3
    elif 2 in result:
        if result.count(2) >= 2:
            return 2
        else:
            return 1
    else:
        return 0

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
