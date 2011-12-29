import random
import string

def generateCards():
    cards = range(2, 11)
    cards.append('J')
    cards.append('Q')
    cards.append('K')
    cards.append('A')

    cards = cards * 4
    random.shuffle(cards)
    print 'Deck: ', cards

    firstHand = []
    secondHand = []

    lastCard = cards[len(cards) - 1]
    cards.pop()
    firstHand.append(lastCard)

    lastCard = cards[len(cards) - 1]
    cards.pop()
    secondHand.append(lastCard)

    lastCard = cards[len(cards) - 1]
    cards.pop()
    firstHand.append(lastCard)

    lastCard = cards[len(cards) - 1]
    cards.pop()
    secondHand.append(lastCard)
    
    return cards, firstHand, secondHand


def hit(cards, hand):
    lastCard = cards[len(cards) - 1]

    print '\nHit:', lastCard
    cards.pop()
    hand.append(lastCard)


def sumCards(cards):

    totalPoint = 0

    for c in cards:
        if (c == 'J') or (c == 'Q') or (c == 'K'):
            point = 10
        elif (c == 'A'):
            point = 1
        else:
            point = c

        totalPoint += point

    if 'A' in cards and totalPoint <= 11:
        totalPoint += 10

    return totalPoint


def playersTurn(cards, firstHand):
    print '\nYour turn.'
    answer = raw_input('\nWould you like another card?: ')
    playerPoint = sumCards(firstHand)

    while (string.lower(answer) == 'y'):
        hit(cards, firstHand)
        playerPoint = sumCards(firstHand)

        print '\nDeck', cards
        print '\nPlayer:', firstHand, '=>', playerPoint

        if playerPoint > 21:
           print '\nYou went over 21.'
           return playerPoint
        

        else:
            answer = raw_input('\nWould you like another card?: ')

def dealersTurn(cards, secondHand):
    print '\n\nDealer\'s turn.'

    dealerPoint = sumCards(secondHand)

    while (dealerPoint < 17):
        hit(cards, secondHand)
        dealerPoint = sumCards(secondHand)

        print '\nDeck:', cards
        print '\nDealer:', secondHand, '=>', dealerPoint

    if ((dealerPoint >= 17) and (dealerPoint < 22)):
        return dealerPoint

    else:
        
        print '\nDealer went over 21.'
        return dealerPoint

def playBlackjack(cards, firstHand, secondHand):


    playersTurn(cards, firstHand)

    dealersTurn(cards, secondHand)

    playerPoint = sumCards(firstHand)
    dealerPoint = sumCards(secondHand)

    if (playerPoint > 21 and dealerPoint > 21):
        print '\nBoth player and dealer lose!'
        print playerPoint
        print dealerPoint

    elif (playerPoint > 21 and dealerPoint <= 21):
        print '\nDealer wins!'
        print playerPoint
        print dealerPoint

    elif (playerPoint <= 21 and dealerPoint > 21):
        print '\nPlayer wins!'
        print playerPoint
        print dealerPoint

    elif (playerPoint == dealerPoint):
        print '\nTie game!'
        print playerPoint
        print dealerPoint

    elif (playerPoint > dealerPoint):
        print '\nPlayer wins!'
        print playerPoint
        print dealerPoint

    else:
        print '\nDealer wins!'
        print playerPoint
        print dealerPoint
    

def main():

    deck, playerCards, dealerCards = generateCards()
    
    print '\nDeck after first hand:', deck
    print '\nPlayer\'s cards:', playerCards
    print '\nDealer\'s cards:', dealerCards

    playBlackjack(deck, playerCards, dealerCards)

main()

