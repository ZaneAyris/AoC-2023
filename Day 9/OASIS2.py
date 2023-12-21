file = open('input.txt','r')

reading = [[int(number) for number in line.split()] for line in file.readlines()]

outputTotal = 0


for line in reading:
    solved = False
    allVersions = [line.copy()]
    while not solved and len(allVersions[-1]) != 0:
        allVersions.append([allVersions[-1][x + 1] - allVersions[-1][x] for x in range(len(allVersions[-1]) -1)])
        if len(set(allVersions[-1])) == 1 and 0 in allVersions[-1]:
            solved = True

    # Now to percolate up

    for version in range(len(allVersions) -1, -1 , -1):
        if version == len(allVersions) -1:
            allVersions[version].insert(0, 0)
        else:
            allVersions[version].insert(0,allVersions[version][0] - allVersions[version + 1][0])

    outputTotal += allVersions[0][0]

print(outputTotal)
