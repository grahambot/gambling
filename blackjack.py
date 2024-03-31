

import random


def casino_wash():
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = values*4
    shoe = deck*6
    random.shuffle(shoe)
    return shoe
def deal_cards(shoe):
    players_hand = []
    houses_hand = []
    players_hand.append(shoe.pop())
    houses_hand.append(shoe.pop())
    players_hand.append(shoe.pop())
    houses_hand.append(shoe.pop())
    return players_hand, houses_hand

def tally_cards(hand):
    score  = 0
    soft_num =  0
    for card in hand:
        if card in ["J", "Q", "K"]:
            score += 10
        elif card == "A":
            score += 11
            soft_num += 1
        else:
            score += int(card)
    soft_num_iter = soft_num
    for ace in range(soft_num_iter):
        if score > 21:
            score -= 10
            soft_num -= 1
    return score, soft_num > 0
        
        

def play_hands(hand, shoe):
    score, soft = tally_cards(hand)
    while score < 16 or (score < 17 and soft):
        hand.append(shoe.pop())
        score,soft = tally_cards(hand)
    return score

wins = 0
losses = 0
j= 10000
while(j>0):
    shoe = casino_wash()
    while(len(shoe) > 26):
        players_hand,houses_hand = deal_cards(shoe)
        players_score = play_hands(players_hand,shoe)
        if players_score > 21:
            losses += 1
            continue
        houses_score = play_hands(houses_hand, shoe)
        
        if houses_score > 21 or players_score > houses_score:
            wins += 1
        elif houses_score > players_score:
            losses +=1
    j-=1



print(wins,losses,wins/(wins+losses))