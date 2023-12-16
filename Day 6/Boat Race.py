file = open('input.txt','r')

time, distance = [y.split(":")[1].split() for y in [x for x in file.readlines()]]

time = [int(x) for x in time]
distance = [int(x) for x in distance]
winSum = 0

for race in range(len(time)):
    waysToWin = 0
    for ms in range(time[race]):
        if ms * (time[race] - ms) > distance[race]:
            
            waysToWin += 1
    if winSum == 0:
        winSum = waysToWin
    else:
        winSum *= waysToWin
    
print(winSum)
