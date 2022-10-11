import sys
import math

bank_cards = input()
player_cards = input()

bank_cards = bank_cards.split(' ')
player_cards = player_cards.split(' ')

for i in bank_cards:
    if i in 'JQK':
        var = bank_cards.index(i)
        bank_cards[var] = 10
    if i =='A':
        var=bank_cards.index(i)
        bank_cards[var] = 1
for i in player_cards:
    if i in 'JQK':
        var = player_cards.index(i)
        player_cards[var] = 10
    if i == 'A':
        var = player_cards.index(i)
        player_cards[var] = 1

bank_cards=list(map(int,bank_cards))
player_cards=list(map(int,player_cards))
if sum(bank_cards)<=11:
    bank_cards[bank_cards.index(1)]=11
if sum(player_cards)<=11:
    player_cards[player_cards.index(1)]=11

if sum(player_cards)==21 and sum(bank_cards)==21 and len(bank_cards)<=2:
    print('Draw')
elif sum(player_cards)==21 and len(player_cards)==2:
    print('Blackjack!')
elif  sum(player_cards)>21:
    print('Bank')
elif sum(bank_cards)<sum(player_cards) or sum(bank_cards)>21 :
    print('Player')
elif sum(bank_cards)>sum(player_cards) or sum(player_cards)>21:
    print('Bank')
elif sum(bank_cards)==sum(player_cards):
    print('Draw')