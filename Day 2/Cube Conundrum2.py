file = open("input.txt","r")
text = file.read()
lines = text.split("\n")

sumOfPower = 0

for game in lines:
    gameInfo, allSets = game.split(":", 1)
    gameID = gameInfo[5:]
    individualSets = allSets.split(";")
    valid = True
    red = 0
    blue = 0
    green = 0
    for attempt in individualSets:
        colours = attempt.split(",")
        
        for colour in colours:
            count, category = colour.strip().split(" ")
            count = int(count)
            if (category == "red"):
                if(count > red):
                    red = count
            if (category == "green"):
                if(count > green):
                    green = count
            if (category == "blue"):
                if(count > blue):
                    blue = count
    sumOfPower += (red * green * blue)
print(sumOfPower)
