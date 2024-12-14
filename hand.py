from card import Card

class Hand:
    def __init__(self, cards):
        self.cards = cards

    def play_card(self, card_played, pile):
        print(f"You played: {self.cards[card_played].value + self.cards[card_played].suit}")
        pile.cards.append(self.cards[card_played])
        del self.cards[card_played]

    def display_hand(self):
        cards = ""
        for card in self.cards:
            cards = cards + f" {card.value + card.suit}"

        return cards