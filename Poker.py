import random

class Player:
    def __init__(self):
        self.amount = 100
    

# main문 
player = Player()
com_money = 200


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
