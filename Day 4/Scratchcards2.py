file = open("input.txt", "r")
text = file.read()
lines = text.split("\n")


import time

start_time = time.time()



end_time = time.time()

cardTotalNumber = 0

numberOfCard = [1 for x in range(len(lines))]

for card in lines:
    matches = 0
    cardInfo, cardNumbers = card.split(":", 1)
    cardGame = int(cardInfo.split()[1])
    winningNumbers, heldNumbers = cardNumbers.split("|")
    winningNumbersList = winningNumbers.split()
    heldNumbersList = heldNumbers.split()
    
    for number in heldNumbersList:
        if number in winningNumbersList:
            matches += 1
            
    for match in range(1, matches + 1):
        numberOfCard[cardGame + match -1] += 1 * numberOfCard[cardGame -1]

print(sum(numberOfCard))

end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time) 
