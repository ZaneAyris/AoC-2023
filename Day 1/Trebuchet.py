file = open("input.txt", "r")
lines = file.readlines()
output = 0
for line in lines:
    numbers = []
    for char in line:
        if char.isnumeric():
            numbers.append(char)
    newNum = numbers[0] + numbers[-1]
    newNum = int(newNum)
    output += newNum
print(output)
