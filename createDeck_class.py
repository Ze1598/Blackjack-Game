class Card():
    def __init__(self, rank, value, suit):
        self.rank = rank
        self.value = value
        self.name = rank + ' of ' + suit

    def get_rank(self):
        return self.rank

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

def createDeck():
    deck = []
    #Card = [rank, value, suit, name]
    suits = ['Hearts', 'Spades', 'Clubs', 'Diamonds']
    rank = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    royal = ['Jack', 'Queen', 'King']
    deck = [Card(rank[i2-1],i2,i) for i in suits for i2 in range(1,11)]
    royal_cards = [Card(i2,10,i) for i in suits for i2 in royal]
    deck += royal_cards
    return deck

deck = createDeck()
print(len(deck))
for i in deck:
    print(i.get_rank(), i.get_value(), i.get_name())