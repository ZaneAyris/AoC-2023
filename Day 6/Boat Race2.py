file = open('input.txt','r')

time, distance = [y.split(":")[1].split() for y in [x for x in file.readlines()]]

time = int(''.join(time))
distance = int(''.join(distance))


waysToWin = 0
for ms in range(time):
    if ms * (time - ms) > distance:
        waysToWin += 1

    
print(waysToWin)


# O(N) can definitely refine by finding the min and max pointers with accepted values
