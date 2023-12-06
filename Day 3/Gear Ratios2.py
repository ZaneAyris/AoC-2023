import numpy as np

file = open("input.txt", "r")
text = file.read()
lines = text.split("\n")


gear_dict = {}
gear_ratio_sum = 0

lines_array = np.array([list(line) for line in lines])

lines_padded = np.pad(lines_array, pad_width=((1, 1), (1, 1)), mode='constant', constant_values=".")

for row in range(1, lines_padded.shape[0] - 1):
    for column in range(1, lines_padded.shape[1] - 1):
        if lines_padded[row][column].isnumeric():
            surrounded_by = []
            curr_number = ""
            temp_row, temp_column = row, column
            while lines_padded[temp_row][temp_column].isnumeric():
                curr_number += lines_padded[temp_row][temp_column]
                lines_padded[temp_row][temp_column] = "."
                for row_adjacent in range(-1, 2):
                    for col_adjacent in range(-1, 2):
                        if lines_padded[row_adjacent + temp_row][col_adjacent + temp_column]== "*" and (row_adjacent + temp_row, col_adjacent + temp_column) not in surrounded_by:
                            surrounded_by.append((row_adjacent + temp_row, col_adjacent + temp_column))
         
                temp_column += 1
            
            for gear in surrounded_by:
                if gear not in gear_dict.keys():
                    gear_dict[gear] = [curr_number]
                else:
                    gear_dict[gear].append(curr_number)

print(gear_dict)

for gear in gear_dict.values():
    if len(gear) == 2:
        gear_ratio_sum += int(gear[0]) * int(gear[1])

print(gear_ratio_sum)

