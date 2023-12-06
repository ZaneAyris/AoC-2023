file = open("input.txt","r")
sections = file.read().split("\n\n")

def mapX(currObject, nextList):
    currObject = int(currObject)
    for numbers in nextList:
        destStart, sourStart, rangeLen = [int(s) for s in numbers.split()]
        if currObject >= sourStart and currObject < sourStart + rangeLen - 1:
            return currObject - sourStart + destStart
    return sourStart

seeds = sections[0].split(":")[1].strip().split(" ")

soil, fert, water, light, temp, humid, location = [section.split(":")[1].strip().split("\n") for section in sections[1:]]

for seed in seeds:
    dirt = mapX(seed, soil)
    fertalizer = mapX(dirt, fert)
    h2o = mapX(fertalizer, water)
    sun = mapX(h2o, light)
    heat = mapX(sun, temp)
    hummas = mapX(heat, humid)
    local = mapX(hummas, location)
    print(local)

