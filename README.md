# WORK IN PROGRESS
At the moment this readme is just my notes and todo list

# Game rules
1. Goal is to end the game with more point than the opponents.
2. Game starts with choosing dealer by players cutting for the highest card.
3. Starting each round dealer Cuts the deck and trys to get exact number of cards (10 per player plus 1 to discard), if succeeds, dealer gets 100 points.
4. The players take turns clockwise.
5. The goal of each round is to get rid of all cards in hand, when this happens, the round is over.
6. At the start of each turn, a player may pick up from the deck 1 card, or use one or multiple "buys".
7. Each player is allotted 10 buys for the entire game.
8. A buy consists of taking the top card from the discard pile and 3 from the deck and showing opponents these cards.
9. A player may use multiple buys in a turn but must do so all at the same time. (If a player buys one and doesn't get what they need, they cannot buy another.)
10. Once a player has picked up card(s) they may play them on the table but they must first satisfy the goal of the round. The goals of each round are:

| Round #        | Goal           | Example
| ------------- |-------------:| :-----:
| 1 | 1 group of 3 | three aces
| 2 | 2 groups of 3 | 2 aces and one wild card plus 3 threes
| 3 | 1 group of 4 | 4 kings
| 4 | 2 groups of 4 | 4 kings plus 4 sevens
| 5 | 1 group of 5 |
| 6 | 2 groups of 5 |
| 7 | 1 group of 5 |
| 8 | 2 groups of 5 |

11. Each must contain at least two non wild cards.
12. Twos and Jokers are wild.
13. Once you have met the goal and have played your cards, you may play sets of three (or pairs and a wild card) or single cards if they have been already played by you or another player in the current round or wild cards.
14. You may not play all the cards in your hand, because you must always discard.
15. You end your turn by discarding.
16. If a player had one card at the start of their turn, they must first discard and then pick up from the deck. If the card can be played the round is over, otherwise it is the next persons turn.
17. Otherwise the round ends by a player discarding their last card.
18. Each player gets points for all the cards they have played and loses points for all the cards in their hand.
19. The value of the cards are:
| Card        | Points          |
| ------------- |-------------:|
| 3-9 | 5 |
| 10 - King | 10 |
| Ace | 15 |
| 2 | 20 |
| Joker | 50 |
20. After summing the points, the next round begins as the first one did with the next player dealing and trying to get the exact amount of points.

# To Do
1. Create Model of Game
	- no buys
2. Create Simulation of Game using rule actions defined by me
	- Use only round status features and buys remaining

# Assumptions
- number of decks is equal to: ceil((3*10+10)xNumPLayers+1)/54 (players using all buys in one round)
- Suits dont matter and wont be kept track of
- No last card announcements
- Cards aren't shown on a buy
- Can only buy one per turn

# Features:
### 1. Game status
- number of players
- oplayer scores
- oplayer buys remaining
- player score
- player buys remaining

### 2. Round Status
- round goal
- cards in hand
- cards discarded
- cards discarded by other players
