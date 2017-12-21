deck = []
#Card = [rank, value, suit, name]
suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
rank = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
royal = ['Jack', 'Queen', 'King']

for i in suits:
    for i2 in range(1, 11):
        card = []
        card.append(rank[i2-1])
        card.append(i2)
        card.append(i)
        card.append(card[0] + ' of ' + i)
        deck.append(card)
    for i2 in royal:
        card = [10, i]
        card.insert(0,i2)
        card.append(card[0] + ' of ' + i)
        deck.append(card)

for i in deck:
    print(i[0], i[1], i[2], i[3])