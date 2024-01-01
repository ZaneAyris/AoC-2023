file = open('input.txt','r')

def findStart(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == "S":
                return row, column
    return None

dArray = [list(row.strip()) for row in file.readlines()]

up = "|", "7", "F", "S"
left = "-", "L", "F", "S"
down = "|", "L", "J", "S"
right = "-", "F", "L", "S"


loc = findStart(dArray)
currentPiece = dArray[loc[0]][loc[1]]
prevLoc = None

length = 0

pieces = []


while length == 0 or not currentPiece == "S":
    pieces.append(loc)
    if currentPiece == "S" and length == 0:
        if dArray[loc[0] - 1][loc[1]] in up:
            loc = loc[0] -1, loc[1]
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "D"
            length += 1
            continue
            

            
        if dArray[loc[0] +1][loc[1]] in down:
            loc = loc[0] +1, loc[1]
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "U"
            length += 1
            continue

            
        if dArray[loc[0]][loc[1] + 1] in right:
            loc = loc[0], loc[1] + 1
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "L"
            length += 1
            continue
            
        if dArray[loc[0]][loc[1] -1] in left:
            loc = loc[0], loc[1] -1
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "R"
            length += 1
            continue
        
    if currentPiece == "-":
        if prevLoc == "R":
            loc = loc[0], loc[1] -1
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "R"
            length += 1
            continue
            #Check Left
        else:
            loc = loc[0], loc[1] + 1
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "L"
            length += 1
            continue
            #Check Right

    if currentPiece == "|":
        if prevLoc == "D":
            #Check Up
            loc = loc[0] -1, loc[1]
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "D"
            length += 1
            continue
        else:
            loc = loc[0] +1, loc[1]
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "U"
            length += 1
            continue
            #Check Down

    if currentPiece == "J":
        if prevLoc == "L":
            loc = loc[0] -1, loc[1]
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "D"
            length += 1
            continue
            #Check Up
        else:
            loc = loc[0], loc[1] -1
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "R"
            length += 1
            continue
            #Check Left

    if currentPiece == "L":
        if prevLoc == "U":

            loc = loc[0], loc[1] + 1
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "L"
            length += 1
            continue
            #Check Right
        else:
            loc = loc[0] -1, loc[1]
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "D"
            length += 1
            continue
            #Check Up

    if currentPiece == "7":
        if prevLoc == "L":
            loc = loc[0] +1, loc[1]
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "U"
            length += 1
            continue
            #Check Down
        else:
            loc = loc[0], loc[1] -1
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "R"
            length += 1
            continue
            #Check Left

    if currentPiece == "F":
        if prevLoc == "D":
            #Check Right
            loc = loc[0], loc[1] + 1
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "L"
            length += 1
            continue
        else:
            loc = loc[0] +1, loc[1]
            currentPiece = dArray[loc[0]][loc[1]]
            prevLoc = "U"
            length += 1
            continue

direct = {(0, -1) : "L" , (0, 1) : "R" ,(-1, 0) : "U", (1, 0) : "D" }

S = pieces[0]

direction1 = direct[(pieces[1][0] - pieces[0][0],  pieces[1][1] - pieces[0][1])]
direction2 = direct[(pieces[-1][0] - pieces[0][0], pieces[-1][1] - pieces[0][1])]

dictdict = {"DU": "|", "LR": "-", "DL": "7", "DR":"F", "LU":"J", "RU":"L"}

newPiece = "".join(sorted(direction1 + direction2))


dArray[pieces[0][0]][pieces[0][1]] = dictdict[newPiece]

enclosed = 0

toFind = ("|", "L", "J")
for row in range(len(dArray)):
    for tile in range(len(dArray[row])):
        if (row, tile) not in pieces:
            count = 0
            for ray in range(tile):
                if (row, ray) in pieces and dArray[row][ray] in toFind:
                    count += 1
            if count % 2 == 1:
                enclosed += 1
print(enclosed)
