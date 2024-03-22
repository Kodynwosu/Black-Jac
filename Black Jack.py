import random

DeckofCards = []
sList = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
nList = [2, 3, 4, 5, 6, 7, 8, 9, 'A', 'J', 'Q', 'K']

for suit in sList:
    for value in nList:
        DeckofCards.append(str(value) + " of " + suit)
random.shuffle(DeckofCards)


def dealCard(turn):
    card = DeckofCards.pop()
    turn.append(card)


def total(turn):
    total = 0
    num_Ace = 0
    for card in turn:
        cardValue = card.split()[0]
        if cardValue.isdigit():
            total += int(cardValue)
        elif cardValue in ['J', 'Q', 'K']:
            total += 10
        elif cardValue == 'A':
            num_Ace += 1
            total += 11

    while total > 21 and num_Ace:
        total -= 10
        num_Ace -= 1
    return total


def print_game_state(player_hand, dealer_hand, player_score, dealer_score):
    print("Player's Hand:", player_hand, "Total Score:", player_score)
    print("Dealer's Hand:", dealer_hand, "Total Score:", dealer_score)


def play_blackjack():
    Playerhand = []
    Dealerhand = []

    dealCard(Playerhand)
    dealCard(Dealerhand)
    dealCard(Playerhand)
    dealCard(Dealerhand)

    player1Score = total(Playerhand)

    print("Starting Game Cards:")
    print_game_state(Playerhand, Dealerhand, player1Score, total(Dealerhand))

    dealerScore = 0
    while dealerScore < 17:
        dealCard(Dealerhand)
        dealerScore = total(Dealerhand)

    while player1Score < 21:
        decision = input("Do you want to hit or stay? (h/s): ").lower()
        if decision == 'h':
            dealCard(Playerhand)
            player1Score = total(Playerhand)
            print("Your current total is:", player1Score)
            print_game_state(Playerhand, Dealerhand, player1Score, total(Dealerhand))
        elif decision == 's':
            break
        else:
            print("Invalid input. Please enter 'h' to hit or 's' to stay.")

    if player1Score > 21:
        print("Player busts! Dealer wins.")
    else:
        dealerScore = total(Dealerhand)
        while dealerScore < 17:
            dealCard(Dealerhand)
            dealerScore = total(Dealerhand)

        if dealerScore > 21:
            print("Dealer busts! Player wins.")
        else:
            if player1Score > dealerScore:
                print("Player wins with a score of", player1Score)
            elif player1Score < dealerScore:
                print("Dealer wins with a score of", dealerScore)
            else:
                print("It's a tie!")

    print("Final Game Cards:")
    print_game_state(Playerhand, Dealerhand, player1Score, dealerScore)


play_blackjack()
