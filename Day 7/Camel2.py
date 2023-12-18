file = open('input.txt','r')
hand = [tuple(x.split()) for x in [y for y in file.readlines()]]
dictionary = {1: [], 2:[], 2.5:[], 3:[], 3.5:[], 4:[], 5:[]}
for game in hand:
    currentSet = set(game[0])
    if 'J' not in currentSet:
        dictionary[len(currentSet)].append(game)
    else:
        if len(currentSet) != 1:
            dictionary[len(currentSet) -1].append(game)
        else:
            dictionary[1].append(game)

Order = {'A': 0, 'K': 1, 'Q': 2, 'T' : 3, '9': 4, '8': 5, '7': 6, '6': 7, '5': 8, '4': 9, '3': 10, '2': 11, 'J': 12}


toMove = []

for game in dictionary[2]: # Separating 4 of a kind and Full House
    gameSet = set(game[0])
    if 'J' in gameSet:
        Jokers = game[0].count("J")
        gameSet.remove("J")
        maxCount = 0
        for card in gameSet:
            maxCount = max(game[0].count(card) + Jokers, maxCount)

        if maxCount == 3: # If Full house move it to 3.5
            toMove.append(game)
        continue
        
    if game[0].count(game[0][0]) == 3 or game[0].count(game[0][0]) == 2:
        toMove.append(game)

for game in toMove:
    dictionary[2].remove(game)
    dictionary[2.5].append(game)

toMove = []

for game in dictionary[3]: # Separating Three of a kind with 2 pair
    gameValues = set(game[0])
    if "J" not in gameValues:
        threeOfAKind = False
        for cardType in gameValues:
            if game[0].count(cardType) == 3:
                threeOfAKind = True
        if threeOfAKind == False:
            toMove.append(game)

            

for game in toMove:
    dictionary[3].remove(game)
    dictionary[3.5].append(game)


for gameType in dictionary.keys():
    dictionary[gameType] = sorted(dictionary[gameType],  key=lambda game: [(Order.get(card), Order.get((game[0][1:])[0])) for card in game[0]])
    
allGames = [game for gameType in dictionary.values()  for game in gameType]
allGames.reverse()
sumWin = 0
for game in allGames:
    sumWin += int(game[1]) * (allGames.index(game) + 1)
print(sumWin)

