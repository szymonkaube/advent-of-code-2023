# get_all_numbers() gets (row, start column, end column) of all numbers in the list of lists
def get_all_numbers(two_d_array):
    numbers_positions = []
    for i, row in enumerate(two_d_array):
        number_start_idx = -1
        number_end_idx = -1
        in_number = False
        for j, col in enumerate(row):
            current_elem_is_digit = two_d_array[i][j].isdigit()
            # Case for finding a start of a number
            if not in_number and current_elem_is_digit:
                in_number = True
                number_start_idx = j
            # Case for finding an end of a number when a there is no character after number
            if in_number and current_elem_is_digit and j == len(two_d_array[i]) - 1:
                number_end_idx = j
                # print((i ,number_start_idx, number_end_idx))
                numbers_positions.append((i ,number_start_idx, number_end_idx))
                in_number = False
            # Case for finding an end of a number when there is a character after a number
            elif in_number and not current_elem_is_digit:
                number_end_idx = j - 1
                # print((i ,number_start_idx, number_end_idx))
                numbers_positions.append((i, number_start_idx, number_end_idx))
                in_number = False

    return numbers_positions


# is_there_adjacent_symbol() checks whether there is a symbol adjacent to cell in (i, j)
def is_there_adjacent_symbol(two_d_array, i, j, symbols):
    n_rows = len(two_d_array)
    n_cols = len(two_d_array[0])

    # Top left corner
    if i == 0 and j == 0:
        submatrix = [row[:2] for row in two_d_array[:2]]
    # Top right corner
    elif i == 0 and j == n_cols - 1:
        submatrix = [row[-2:] for row in two_d_array[:2]]
    # Top row
    elif i == 0:
        submatrix = [row[j-1:j+2] for row in two_d_array[:2]]
    # Bottom left corner
    elif i == n_rows - 1 and j == 0:
        submatrix = [row[:2] for row in two_d_array[-2:]]
    # Bottom right corner
    elif i == n_rows - 1 and j == n_cols - 1:
        submatrix = [row[j-2:j] for row in two_d_array[-2:]]
    # Bottom row
    elif i == n_rows - 1:
        submatrix = [row[j-1:j+2] for row in two_d_array[-2:]]
    # Left column
    elif j == 0:
        submatrix = [row[:2] for row in two_d_array[i-1:i+2]]
    # Right column
    elif j == n_cols - 1:
        submatrix = [row[-2:] for row in two_d_array[i-1:i+2]]
    # Inner part of the matrix
    else:
        submatrix = [row[j-1:j+2] for row in two_d_array[i-1:i+2]]

    flattened_submatrix = [char for word in submatrix for char in word]

    for char in flattened_submatrix:
        if char in symbols:
            return True
        
    return False


def main():
    # Reading from a file
    with open("day3_input.txt") as f:
        text = f.read()

    # Getting the set of symbols that qualify the number to be added
    chars = list(text)
    unique_chars = set(chars)
    symbols = []
    for char in unique_chars:
        if not char.isdigit() and char not in [".", "\n"]:
            symbols.append(char)

    symbols = set(symbols)

    # Create a list of lists of characters in the text
    matrix_of_chars = [list(i) for i in text.splitlines()]

    # Get the positions of the starts and ends of numbers in the text
    numbers_positions = get_all_numbers(matrix_of_chars)

    # Calculate the sum of the numbers that have an special symbol adjacent to them
    result = 0
    for row, start, end in numbers_positions:
        number_elems_positions = range(start, end + 1)
        for j in number_elems_positions:
            # If the number has a special symbol adjacent to it then add its value to the result
            if is_there_adjacent_symbol(matrix_of_chars, row, j, symbols):
                current_num = int("".join(matrix_of_chars[row][start:end+1]))
                result += current_num
                break

    print(result)


if __name__ == "__main__":
    main()