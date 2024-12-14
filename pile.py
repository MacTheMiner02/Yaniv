from card import Card


class Pile:
    def __init__(self, cards):
        self.cards = cards

    def pickup(self, card_picked_up):
        del self.cards[card_picked_up]

    def display_pile(self):
        cards = ""
        for card in self.cards:
            cards = cards + f" {card.value + card.suit}"

        return cards