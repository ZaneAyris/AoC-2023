file = open("input.txt", "r")
text = file.read()
lines = text.split("\n")

pointTotal = 0

for card in lines:
    matches = 0
    cardInfo, cardNumbers = card.split(":", 1)
    winningNumbers, heldNumbers = cardNumbers.split("|")
    winningNumbersList = winningNumbers.split()
    heldNumbersList = heldNumbers.split()

    
    for number in heldNumbersList:
        if number in winningNumbersList:
            matches += 1

    if matches == 1:
        pointTotal += 1
    if matches > 1:
        pointTotal += 2 ** (matches -1)
    print(matches)
print(pointTotal)
