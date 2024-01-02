
def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

def addSpace(array_2d):
    spaceCopy = array_2d.copy()
    found = 0
    for row in range(len(spaceCopy)):
        if set(spaceCopy[row]) == set('.'):
            array_2d.insert(row + found, ['.'] * len(array_2d[row]))
            found += 1

file = open("input.txt","r")

space = [list(x) for x in file.read().split('\n')]

addSpace(space)
space = rotated(space) 
addSpace(space)
space = rotated(space) 
space = rotated(space) 
space = rotated(space) 

galaxies = []

distance = 0

for row in range(len(space)):
    for column in range(len(space[row])):
        if space[row][column] == "#":
            galaxies.append((row, column))

while len(galaxies) > 1:
    currGalaxy = galaxies.pop()
    for x in galaxies:
        distance += abs(abs(currGalaxy[0] - x[0]) + abs(currGalaxy[1] - x[1]))

print(distance)
