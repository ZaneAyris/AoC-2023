import math
file = open('input.txt','r')

directions, codes = file.read().split("\n\n")

locations = {}
for code in codes.split('\n'):
    locations[code[0:3]] = code[7:10], code[12:15]


currentNodes = [] # Find Starting nodes
for node in locations.keys():
    if node[2] == "A":
        currentNodes.append(node)

nodeRanges = []

for node in currentNodes:
    currentStep = 1
    currentNode = node
    outputNode = None
    while not outputNode:
        if currentNode[2] == 'Z':
            outputNode = currentStep -1
        step = (currentStep -1) % len(directions)
        currentDirection = 0 if directions[step] == 'L' else 1
        currentNode = locations[currentNode][currentDirection]
        currentStep += 1
    nodeRanges.append(outputNode)

print(nodeRanges)
print(*nodeRanges)
print(math.lcm(*nodeRanges))
