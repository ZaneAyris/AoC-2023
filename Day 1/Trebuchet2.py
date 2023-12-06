import re
file = open("input.txt", "r")
lines = file.readlines()
parsedLines = []

digits = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
}

for line in lines:
    tuples = []
    newline = ""
    for index in range(len(line)):
        if line[index].isnumeric():
            tuples.append((line[index], index))
            
    for key, value in digits.items():
        currDigit = [m.start() for m in re.finditer(key, line)]
        for instance in currDigit:
            tuples.append((value, instance))
    tuples.sort(key=lambda x: x[1])
    for number in tuples:
        newline += number[0]
    parsedLines.append(newline)
    
output = 0
for line in parsedLines:
    numbers = []
    for char in line:
        if char.isnumeric():
            numbers.append(char)
    newNum = numbers[0] + numbers[-1]
    newNum = int(newNum)
    output += newNum
print(output)

