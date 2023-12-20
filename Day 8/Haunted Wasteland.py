file = open('input.txt','r')

directions, codes = file.read().split("\n\n")

locations = {}
for code in codes.split('\n'):
    locations[code[0:3]] = code[7:10], code[12:15]


currentNode = 'AAA'
currentStep = 1
while currentNode != 'ZZZ':
    step = (currentStep -1) % len(directions)
    currentDirection = 0 if directions[step] == 'L' else 1
    currentNode = locations[currentNode][currentDirection]
    currentStep += 1
print(currentStep -1)
