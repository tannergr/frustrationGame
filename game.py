from random import shuffle
import math
# cards represented with integers as follows:
# ints 0-6 maps to cards 3-9
# ints 7-10 maps to cards 10, J, Q, K
# 11 maps to Ace
# 12 maps to 2 (wild card)
# 13 maps to joker

class Game:
    def __init__(self, noPlayers):
        self.noPlayers = noPlayers
        self.round = 0
        self.decks = math.ceil((3*10+10)*noPlayers/54)
        self.hands = []
        self.buysRemaining = [10] * noPlayers

        for i in range(noPlayers):
            self.hands.append([])

    # create deck and shuffle
    def buildDeck(self):
        self.cards = []
        for i in range(13):
            for j in range(self.decks * 4):
                self.cards.append(i)

        for i in range(2 * self.decks):
            self.cards.append(13)
        shuffle(self.cards)
        return

    # build deck and deal out cards
    def dealCards(self):
        self.buildDeck()

        # empty previous hands
        self.hands = []
        for i in range(self.noPlayers):
            self.hands.append([])

        # deal out cards
        for i in range(10):
            for j in range(self.noPlayers):
                self.hands[j].append( self.cards.pop() )

    def playGame(self):
        # play 8 rounds
        for i in range(0,8):
            self.playRound(i)
        return

    def playRound(self, roundNo):
        self.round = Round(self.noPlayers)
        print("Round: ", roundNo)
        self.roundNo = roundNo
        self.dealCards()
        roundEnded = False
        whosTurn = 0
        count = 0
        while(not roundEnded):
            self.playTurn(whosTurn)
            whosTurn = whosTurn + 1 if whosTurn < self.noPlayers - 1 else 0
            count+=1;
            if(count > 20):
                roundEnded = True
        return

    def playTurn(self, whosTurn):
        print("It is player: ", whosTurn, "'s Turn")
        print("Your cards are:")
        print(self.hands[whosTurn])

        self.hands[whosTurn].append(self.cards.pop())

        # First Stage of Turn: buy or pick up
        if not self.buysRemaining[whosTurn] < 0:
            actionAcceptable = False
            while not actionAcceptable:
                action = input("Pickup (p) or Buy (b)?")
                if action == "b":
                    if len(self.round.discardPile) < 1:
                        raise Exception('No cards in discard')
                    else:
                        newCards = []
                        newCards.append(self.round.discardPile.pop())
                        for i in range(3):
                            newCards.append(self.cards.pop())
                        print("You bought: ", newCards)
                        actionAcceptable = True
                elif action == "p":
                    newCards = []
                    newCards.append(self.cards.pop())
                    print("You picked up: ", newCards)
                    actionAcceptable = True
        else:
            print("No Buys Left!")
            newCards = []
            newCards.append(self.cards.pop())
            print("You picked up: ", newCards)

        print("Your cards are:")
        self.hands[whosTurn].extend(newCards)
        print(self.hands[whosTurn])


        input()
        self.round.discardPile.append(self.hands[whosTurn].pop(0))
        print(self.round.discardPile)

class Round:
    def __init__(self, noPlayers):
        self.cardsOnTable = []
        self.playerSets = []
        self.playerIsDown = [False] * noPlayers
        self.discardPile = []
        for i in range(noPlayers):
            self.playerSets.append([])



game = Game(3)
game.dealCards()
print(game.hands)
print(len(game.cards),54*3)
try game.playGame()
