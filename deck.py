import random
from card import Card


class Deck:
    def __init__(self):
        self.deck = self.create_deck()

    def shuffle(self):
        random.shuffle(self.deck)

    def create_deck(self):
        suits = ["S", "C", "D", "H"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cards = []

        for suit in suits:
            for value in values:
                card = Card(value, suit)
                cards.append(card)

        card = Card("Joker", "Red")
        cards.append(card)
        card = Card("Joker", "Black")
        cards.append(card)

        return cards

    def deal(self, hands, card_num):
        for i in range(card_num):
            for hand in hands:
                hand.cards.append(self.deck[0])
                self.deck.pop(0)

    def display_deck(self):
        all_cards = ""
        for card in self.deck:
            all_cards = all_cards + f" {card.value + card.suit}"

        return all_cards
        print(f"Deck length: {len(self.deck)}")