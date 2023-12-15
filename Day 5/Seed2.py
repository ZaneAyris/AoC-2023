file = open("input.txt","r")
sections = file.read().split("\n\n")

seeds = [int(x) for x in sections[0].split(":")[1].strip().split(" ")]
maps = [[int(y) for y in section.split(":")[1].strip().split()] for section in sections[1:]]

maps = [[tuple(m[i:i + 3]) for i in range(0, len(m), 3)] for m in maps]

minLocation = None

bagOfSeeds = []

for i in range(0,len(seeds),2):
    bagOfSeeds.append((seeds[i], seeds[i] + seeds[i+1] -1))


for m in maps:
    nextBag = []
    while bagOfSeeds:
        seedStart, seedEnd = bagOfSeeds.pop()
        overlap = False
        for destStart, srcStart, rangeLen in m:
            destEnd = destStart + rangeLen -1
            srcEnd = srcStart + rangeLen -1
            if seedStart > srcEnd or srcStart > seedEnd: # No Overlap
                continue
                
            
            if seedStart < srcStart and seedEnd <= srcEnd: # Left side only Overlap
                tempRange = seedEnd - srcStart
                bagOfSeeds.append((seedStart, srcStart -1))
                nextBag.append((destStart, destStart + tempRange))
                overlap = True
                break
            
            if seedStart >= srcStart and seedEnd > srcEnd: # Right side only Overlap
                tempRange = seedStart - srcStart
                nextBag.append((destStart + tempRange, destEnd))
                bagOfSeeds.append((srcEnd+1, seedEnd))
                overlap = True
                break
            
            if seedStart < srcStart and seedEnd > srcEnd: # Seed larger than Src
                bagOfSeeds.append((seedStart, srcStart -1))
                bagOfSeeds.append((srcEnd +1, seedEnd))
                nextBag.append((destStart, destEnd))
                overlap = True
                break
                
            if seedStart >= srcStart and seedEnd <= srcEnd: # Complete Overlap
                tempStartRange = seedStart - srcStart
                tempEndRange = seedEnd - srcStart
                nextBag.append((destStart + tempStartRange, destStart + tempEndRange))
                overlap = True
                break
        if overlap == False:
            nextBag.append((seedStart, seedEnd))
            
    bagOfSeeds = nextBag
            
minLocation = min(bagOfSeeds, key=lambda t:t)
print(minLocation)
