file = open('input.txt','r')
hand = [tuple(x.split()) for x in [y for y in file.readlines()]]
dictionary = {1: [], 2:[], 2.5:[], 3:[], 4:[], 5:[]}
for game in hand:
    dictionary[len(set(game[0]))].append(game)


Order = {'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T' : 4, '9': 5, '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12}


toMove = []

for game in dictionary[2]:
    if game[0].count(game[0][0]) == 3 or game[0].count(game[0][0]) == 2:
        toMove.append(game)

for game in toMove:
    dictionary[2].remove(game)
    dictionary[2.5].append(game)



for gameType in dictionary.keys():
    dictionary[gameType] = sorted(dictionary[gameType],  key=lambda game: [(Order.get(card), Order.get((game[0][1:])[0])) for card in game[0]])
    
allGames = [game for gameType in dictionary.values()  for game in gameType]

sumWin = 0
for game in allGames:
    sumWin += int(game[1]) * (allGames.index(game) + 1)
print(sumWin)
