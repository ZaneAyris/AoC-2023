import numpy as np

file = open("input.txt", "r")
text = file.read()
lines = text.split("\n")

partSum = 0

lines_array = np.array([list(line) for line in lines])

lines_padded = np.pad(lines_array, pad_width=((1, 1), (1, 1)), mode='constant', constant_values=".")

for row in range(1, lines_padded.shape[0] - 1):
    for column in range(1, lines_padded.shape[1] - 1):
        if lines_padded[row][column].isnumeric():
            surrounded = False
            curr_number = ""
            temp_row, temp_column = row, column
            while lines_padded[temp_row][temp_column].isnumeric():
                curr_number += lines_padded[temp_row][temp_column]
                lines_padded[temp_row][temp_column] = "."
                if surrounded == False:
                    for row_adjacent in range(-1, 2):
                        for col_adjacent in range(-1, 2):
                            if lines_padded[row_adjacent + temp_row][col_adjacent + temp_column].isnumeric() == False and lines_padded[row_adjacent + temp_row][col_adjacent + temp_column] != ".":
                                surrounded = True
                temp_column += 1
                
            if surrounded:
                print(curr_number)
                partSum += int(curr_number)
print(partSum)

