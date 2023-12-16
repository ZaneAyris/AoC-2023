file = open('input.txt','r')
hand = [tuple(x.split()) for x in [y for y in file.readlines()]]
print(hand[0])
