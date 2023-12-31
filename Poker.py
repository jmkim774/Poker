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

#card_factory

class factory(Card):
    def makecard(self, suit:suitEnum, num):
        if suit == suitEnum.SPADE:
            return SCard(num)
        elif suit == suitEnum.HEART:
            return HCard(num)
        elif suit == suitEnum.DIAMOND:
            return DCard(num)
        elif suit == suitEnum.CLUB:
            return CCard(num)

    def calc(self, num):
        self.amount += num
        
# money
class Singleton(object):
    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.amount = 100

    def calc(self, num):
        self.amount += num

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

# 랭크 판별 함수
def card_rank(cards):
    rank = 0
    rank = ispair(cards)
    if isstraight(cards):
        if rank < 5:
            rank = 5
    if isflush(cards):
        if rank == 5:
            rank = 9
        elif rank <6:
            rank = 6
    return rank

# main문 
player = Singleton()
com_money = 200

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

    
    print("--------------shuffle deck---------------")
    random.shuffle(deck)


    print("----------------your hand----------------")
    player_cards = [ deck[k] for k in range(0, 5)]
    com_cards = [ deck[k] for k in range(5, 10)]


    player_rank = card_rank(player_cards)


    player_hand = ["" for i in range(6)]
    for i in player_cards:
        if i.state == "match":
            di = matchCard(i)
        elif i.state == "unmatch":
            di = unmatchCard(i)
        makedraw(di)
        for j in range(6):
            player_hand[j] = player_hand[j] + i.shape[j]
            player_hand[j] = player_hand[j] + "   "

  
    for i in player_hand:
        print(i)

    print("-----------------------------------------")
    
    print("your rank is ", player_rank)
    print("your money : ",player.amount)
    print("com money : " ,com_money)

    print("if you want betting, please insert amount? (-1 is Fold) :")
    TB = int(input())
    if TB < 0:
        print("---------------you fold---------------")
        print()
        continue
    if betting+TB >player.amount:
        print("you can't betting more than your money!!")
        print()
    else:
        betting = betting + TB   

    print("----------------2nd turn----------------")
    print()
    player_cards.append(deck[11])
    com_cards.append(deck[12])

    print("----------------your hand----------------")
    print()
    player_rank = card_rank(player_cards)

    player_hand = ["" for i in range(6)]
    for i in player_cards:
        if i.state == "match":
            di = matchCard(i)
        elif i.state == "unmatch":
            di = unmatchCard(i)
        makedraw(di)
        for j in range(6):
            player_hand[j] = player_hand[j] + i.shape[j]
            player_hand[j] = player_hand[j] + "   "
  
    for i in player_hand:
        print(i)

    print("-----------------------------------------")

    print("your rank is ", player_rank)

    print("your betting amount is ", betting) # 전 턴과는 달리 현재 베팅 금액을 표시해줌
    print("your money : ",player.amount)
    print("com money : " ,com_money)
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
    player_cards.append(deck[13])
    com_cards.append(deck[14])

    print("----------------your hand----------------")
    player_rank = card_rank(player_cards)

    player_hand = ["" for i in range(6)]
    for i in player_cards:
        if i.state == "match":
            di = matchCard(i)
        elif i.state == "unmatch":
            di = unmatchCard(i)
        makedraw(di)
        for j in range(6):
            player_hand[j] = player_hand[j] + i.shape[j]
            player_hand[j] = player_hand[j] + "   "

    for i in player_hand:
        print(i)

    print("-----------------------------------------")    

    print("your rank is ", player_rank)
    print("your betting amount is ", betting)
    print("your money : ",player.amount)
    print("com money : " ,com_money)
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
    player_rank = card_rank(player_cards)

    player_hand = ["" for i in range(6)]
    for i in player_cards:
        if i.state == "match":
            di = matchCard(i)
        elif i.state == "unmatch":
            di = unmatchCard(i)
        makedraw(di)
        for j in range(6):
            player_hand[j] = player_hand[j] + i.shape[j]
            player_hand[j] = player_hand[j] + "   "

    for i in player_hand:
        print(i)

    print("your rank is ", player_rank)
    print("-----------------------------------------")
    
    print("----------------com hand----------------")
    com_rank = card_rank(com_cards)

    com_hand = ["" for i in range(6)]
    for i in com_cards:
        if i.state == "match":
            di = matchCard(i)
        elif i.state == "unmatch":
            di = unmatchCard(i)
        makedraw(di)
        for j in range(6):
            com_hand[j] = com_hand[j] + i.shape[j]
            com_hand[j] = com_hand[j] + "   "

    for i in com_hand:
        print(i)

    print("com rank is ", com_rank)
    print("-----------------------------------------")  
    
    if com_rank < player_rank:
        print("You Win!")
        player.calc(betting)
        com_money -= betting
    elif com_rank > player_rank:
        print("You Lose!")
        player.calc(-betting)
        com_money += betting
        
    else: 
        print("DRAW!")
    print("your money : ",player.amount)
    print("com money : " ,com_money)
    
    if player.amount > 0:
        if com_money <= 0:
            input("----Finally You Win!! Congratulation----")
        input("press enter to next game")
    else:
        input("----Finally You Lose!! Try Again Later----")
