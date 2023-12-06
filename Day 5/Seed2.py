def parseFromRange(start, rangeValue):
    return start + rangeValue -1

def parseToRange(start, end):
    return end-start+1

    
def mapX(inputList, nextList):
    outputList = []

    allInputLists = inputList

    while len(allInputLists) != 0:
        selection = allInputLists[0]

        inpStart, inpRange = [n for n in selection]
        inpEnd = inpStart + inpRange -1
        
        for numbers in nextList:
            destStart, sourStart, rangeLen = [int(s) for s in numbers.split()]
            sourEnd = sourStart + rangeLen - 1

            #6 cases
            #If a part of the range isnt connected with one of the functions, keep it for the future checks ie a unconnected range is checked against all ranges of source
            #If input range is a subset of output range
            if inpStart >= sourStart and  inpEnd <= sourEnd:
                startRange = inpStart - sourStart
                endRange = inpEnd - sourStart +1
                outputForm = (destStart + startRange, destStart + endRange)
                outputList.append(outputForm)
                break

            elif inpStart < sourStart <= inpEnd <= sourEnd:
                # First add matching
                connectedEndRange = inpEnd - sourStart + 1
                connectedOutputForm = (sourStart, destStart + connectedEndRange)
                outputList.append(connectedOutputForm)
                # leave what has not been connected
                disconnectedEnd = sourStart - inpStart
                inpEnd = sourStart -1

            elif sourStart <= inpStart <= inpEnd < sourEnd:

        allInputLists = allInputLists[1:]
    return outputList


file = open("input.txt","r")
sections = file.read().split("\n\n")


seeds = [int(x) for x in sections[0].split(":")[1].strip().split(" ")]
soil, fert, water, light, temp, humid, location = [section.split(":")[1].strip().split("\n") for section in sections[1:]]


seedRanges = []

for i in range(0,len(seeds),2):
    seedRanges.append((seeds[i], seeds[i+1]))

poo = mapX(seedRanges, soil)
print(mapX(poo, fert))



