if __name__ == "__main__":
    with open("day2_input.txt") as f:
        lines = f.read().splitlines()

    RED = 12
    GREEN = 13
    BLUE = 14

    sum_of_possible_indices = 0

    for line in lines:
        line_split = line.split()

        colors_numbers = line_split[2:]

        game_index_list = [s for s in list(line_split[1]) if s.isdigit()]
        game_index = int("".join(game_index_list))

        colors_numbers = [int(s) if s.isdigit() else s for s in colors_numbers]
        zipped = list(zip(colors_numbers[::2], colors_numbers[1::2]))

        red_zipped = [s[0] for s in zipped if "red" in s[1]]
        green_zipped = [s[0] for s in zipped if "green" in s[1]]
        blue_zipped = [s[0] for s in zipped if "blue" in s[1]]

        max_red = max(red_zipped)
        max_green = max(green_zipped)
        max_blue = max(blue_zipped)

        if max_red <= RED and max_green <= GREEN and max_blue <= BLUE:
            sum_of_possible_indices += game_index

    print(sum_of_possible_indices)