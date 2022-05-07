import random


# Card Constants

SUIT_TUPLE = ('Spades', 'Hearts', 'Clubs', 'Diamonds')

RANK_TUPLE = ('Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')

NCARDS = 8

# Pass in a deck and this function returns a random card from the deck

def getCard(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

# Pass in a deck and this function returns a shuffled copy of the deck

def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut


# Main Game
print('Welcome to Higher or Lower')
print('You have to choose whether the next card to be shown will be higher or lower than the current card.')
print('Getting it right adds 20 points; get it wrong and you lose 15 points.')
print('You have 50 points to start with')

startingDeckList = []
# 1
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {'rank': rank, 'suit': suit, 'value': thisValue + 1}
        startingDeckList.append(cardDict)

score = 50


#Play multiple games

while True:
    gameDeckList = shuffle(startingDeckList)
    #2
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict['rank']
    currentCardValue = currentCardDict['value']
    currentCardSuit= currentCardDict['suit']

    print(f"Starting card is: {currentCardRank} of {currentCardSuit}")

    # play one game of this many cards

    #3
    for cardNumber in range(0, NCARDS):
        answer = input(f'Will the next card be higher or lower than the {currentCardRank} of {currentCardSuit}? Enter "H" or "L":\n').upper()

        #4
        nextCardDict = getCard(gameDeckList)

        nextCardRank = nextCardDict['rank']
        nextCardSuit = nextCardDict['suit']
        nextCardValue = nextCardDict['value']

        print(f'Next card is: {nextCardRank} of {nextCardSuit}')

        #5
        if answer == 'H':
            if nextCardValue > currentCardValue:
                print("You're right! It was higher.")
                score += 20
            else:
                print("Sorry, it was lower.")
                score -= 15

        elif answer == 'L':
            if nextCardValue < currentCardValue:
                print("You're right! It was lower.")
                score += 20
            else:
                print("Sorry, it was lower.")
                score -= 15
                
        print(f"Your score is: {score}")

        # Set the new card to be current card
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue
    #6
    goAgain = input('To play again, press ENTER! If you would rather quit, just enter "Q":\n').upper()
    if goAgain == 'Q':
        break

print('Beep boop, Thanks for playing. Goodbye!')
