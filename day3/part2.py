# get_all_number_positions() gets (row, start column, end column) of all numbers in the list of lists
def get_all_number_positions(two_d_array):
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

def get_all_star_positions(two_d_array):
    star_positions = []
    for i, row in enumerate(two_d_array):
        for j, elem in enumerate(row):
            if elem == "*":
                star_positions.append((i, j))
    return star_positions


if __name__ == "__main__":
    # Reading from a file
    with open("day3_input.txt") as f:
        text = f.read()

    # Create a list of lists of characters in the text
    matrix_of_chars = [list(i) for i in text.splitlines()]

    # Get the positions of the starts and ends of numbers in the text
    numbers_positions = get_all_number_positions(matrix_of_chars)
    # Get the positions of "*" in the text
    star_positions = get_all_star_positions(matrix_of_chars)

    result = 0
    for star_position in star_positions:
        # Initialize the list that will contain numbers adjacent to the current star
        star_adjacent_numbers = []
        star_row_neighbourhood = range(star_position[0] - 1, star_position[0] + 2)
        star_col_neighbourhood = range(star_position[1] - 1, star_position[1] + 2)
        for number_pos in numbers_positions:
            number_row = number_pos[0]
            # First we check if the row of the number is in the row neighbourhood of the star
            if number_row in star_row_neighbourhood:
                number_col_start = number_pos[1]
                number_col_end = number_pos[2]
                # Then we check if the column of the number is in the column neighbourhood of the star
                if number_col_start in star_col_neighbourhood or number_col_end in star_col_neighbourhood:
                    # If it is, then the number is adjacent to the star and we append it to the list
                    star_adjacent_numbers.append(int("".join(matrix_of_chars[number_row][number_col_start:number_col_end+1])))

        # For every star that has exactly two numbers adjacent to it,
        # we multiply those numbers and add it to the result
        if len(star_adjacent_numbers) == 2:
            result += star_adjacent_numbers[0] * star_adjacent_numbers[1]

    print(result)