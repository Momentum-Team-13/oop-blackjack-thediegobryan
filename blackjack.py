
class Deck():
    def __init__(self):
        self.cards = []

    def __str__(self):
        return f"{self.cards}"

    # create cards and add to list
    def add_cards(self, card):
        self.cards.append(card)
        return self.cards

class Card():
    def __init__(self, suit, value, rank):
        # card rank, suit, and value
        self.rank = rank
        self.suit = suit
        self.value = value
    
    def __str__(self):
        return f"{self.suit} {self.rank} is worth {self.value} points."
    

#for player
class Player():
    def __init__(self):
        self.player_hand = []
    # right? that makes sense? Yes i believe so

    #ask for another card
    def hit_player(self):
        pass

    #calculate score
    def player_score():
        pass
    
    #this feels spicy
    # betting is in our "extras" haha
    def place_wager():
        pass

class Dealer():
    def __init__(self):
        self.dealer_hand = []

    def start_deal(self):
        pass

    def hit_dealer(self):
        pass

    def dealer_score():
        pass


deck = Deck()
suit = ['♠️','♣️','♥️','♦️']
value = [1,2,3,4,5,6,7,8,9,10,10,10,10]
rank = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

for suit_type in suit:
    for index in range(len(value)):
        value_type = value[index]
        rank_type = rank[index]
        name = f"{rank_type} {suit_type}"
        name = Card(suit_type,value_type,rank_type)
        print(name)

        deck.add_cards(name)

print(deck)