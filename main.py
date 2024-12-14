from card import Card
from hand import Hand
from deck import Deck
from pile import Pile

deck = Deck()
#test
player1 = Hand([])
player2 = Hand([])
player3 = Hand([])
player4 = Hand([])

discard = Pile([])

hands = [player1, player2, player3, player4]

deck.shuffle()
deck.deal(hands, 5)

run = True
while run:
    print("Welcome to Yaniv!")
    input("Press enter to continue")
    game = True

    print("The cards have been dealt!")
    while game:
        print("Here is your hand: " + player1.display_hand())
        played_card = input("Which card do you wish to play? (1-5)")
        played_card = int(played_card) - 1

        while True:
            if played_card <= len(player1.cards) and played_card > 0:
                player1.play_card(played_card, discard)
                break
            else:
                try_again = input("Please select a card that is in your hand! ")
                try_again = int(try_again) - 1
                if try_again <= len(player1.cards) and try_again > 0:
                    player1.play_card(try_again, discard)
                    break

        print("Discard: " + discard.display_pile())