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

# To Do
1. Create Model of Game
	- no buys
2. Create Simulation of Game using rule actions defined by me
	- Use only round status features and buys remaining
3. Create Learning model against simulation

# Assumptions
- number of decks is equal to: ceil((3*10+10)xNumPLayers+1)/54 (players using all buys in one round)
- Suits dont matter and wont be kept track of
- No last card announcements
- Cards aren't shown on a buy
- Can only buy one per turn
