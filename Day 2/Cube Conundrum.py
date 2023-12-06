file = open("input.txt","r")
text = file.read()
lines = text.split("\n")

sumOfIDs = 0

for game in lines:
    gameInfo, allSets = game.split(":", 1)
    gameID = gameInfo[5:]
    individualSets = allSets.split(";")
    valid = True
    for attempt in individualSets:
        colours = attempt.split(",")
        
        for colour in colours:
            count, category = colour.strip().split(" ")
            count = int(count)
            if (category == "red" and count > 12) or (category == "green" and count > 13) or (category == "blue" and count > 14):
                valid = False
    if valid:
        sumOfIDs += int(gameID)

print(sumOfIDs)
