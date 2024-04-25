import sys


def get_number_line_number(line):
    extracted_digits = [int(char) for char in line if char.isdigit()]

    line_number = 10 * extracted_digits[0] + extracted_digits[-1]
    return line_number


def main():
    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()

    total_sum = 0

    for line in lines:
        line_number = get_number_line_number(line)

        total_sum += line_number

    return total_sum


if __name__ == "__main__":
    print(main())