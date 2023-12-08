def mapX(inputList, nextList):
    outputSet = set()

    allInputLists = inputList.copy()

    while len(allInputLists) != 0:
        
        selection = allInputLists[0]

        inpStart, inpRange = [n for n in selection]
        inpEnd = inpStart + inpRange -1
        completed = False
        # (Start, Range)
        
        for numbers in nextList:
            destStart, sourStart, rangeLen = [int(s) for s in numbers.split()]
            sourEnd = sourStart + rangeLen - 1
            destEnd = destStart + rangeLen - 1
            if inpStart >= sourStart and  inpEnd <= sourEnd:
                startRange = inpStart - sourStart +1
                endRange = inpEnd - sourStart +1
                outputForm = (destStart + startRange -1, endRange)
                outputSet.add(outputForm)
                completed = True
                break

            elif inpStart < sourStart <= inpEnd <= sourEnd:
                # First add matching
                connectedEndRange = inpEnd - sourStart + 1
                connectedOutputForm = (destStart, connectedEndRange)
                outputSet.add(connectedOutputForm)
                # leave what has not been connected
                inpEnd = sourStart -1

            elif sourStart <= inpStart <=  sourEnd < inpEnd:
                connectedRange = sourEnd - inpStart + 1
                connectedOutputForm = (destStart, connectedRange)
                outputSet.add(connectedOutputForm)
                inpStart = sourEnd + 1

            elif inpStart < sourStart < sourEnd < inpEnd:
                allInputLists.append((sourEnd, inpEnd + 1))
                # this is whats left allInputLists.append((inpStart, sourStart +1))
                connectedOutputForm = (destStart, rangeLen)
                outputSet.add(connectedOutputForm)
                inpEnd = sourStart +1
                
            else:
                pass

        if completed == False:
            outputSet.add((inpStart, inpEnd - inpStart + 1))
                    
        allInputLists = allInputLists[1:]
    return list(outputSet)


file = open("input.txt","r")
sections = file.read().split("\n\n")


seeds = [int(x) for x in sections[0].split(":")[1].strip().split(" ")]
soil, fert, water, light, temp, humid, location = [section.split(":")[1].strip().split("\n") for section in sections[1:]]


seedRanges = []

for i in range(0,len(seeds),2):
    seedRanges.append((seeds[i], seeds[i+1]))

seedToSoil = mapX(seedRanges, soil)
soilToFert = mapX(seedToSoil, fert)
fertToWater = mapX(soilToFert, water)
waterToLight = mapX(fertToWater, light)
lightToTemp = mapX(waterToLight, temp)
tempToHumid = mapX(lightToTemp, humid)
humidToLocation = mapX(tempToHumid, location)
sorted_list = sorted(humidToLocation, key=lambda x: x[0])

print(sorted_list)

