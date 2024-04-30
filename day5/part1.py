def parse_from_filepath(filepath: str) -> list:
    # Reading from the file
    with open(filepath) as f:
        text = f.read()
        lines = text.splitlines()
    # Parsing
    lines.append("") # we add "" to dont allow the loop to get index out of range
    seeds = [int(seed) for seed in lines[0][7:].split(" ")]
    available_map_names = ["seed-to-soil map:", "soil-to-fertilizer map:",
                        "fertilizer-to-water map:", "water-to-light map:",
                        "light-to-temperature map:", "temperature-to-humidity map:",
                        "humidity-to-location map:"]
    maps_in_text = []
    # Go through all the lines
    for i in range(2, len(lines) - 1):
        # Search for the lines that contain text string with name of a map
        if lines[i] in available_map_names:
            current_map = []
            j = i + 1
            # Iterate until reach empty text string, which indicates end of mapping
            while True:
                if lines[j] == "":
                    break
                start_end_length = [int(num) for num in lines[j].split(" ")]
                current_map.append(start_end_length)
                j += 1
            maps_in_text.append(current_map)
    return (seeds, maps_in_text)


def map_number(number: int, mappings: list) -> int:
    # Look for appropriate mapping
    for mapping in mappings:
        dest_start, source_start, length = mapping
        seed_position_wrt_map = number - source_start
        # If the mapping is found, map the number
        if 0 <= seed_position_wrt_map <= length - 1:
            return dest_start + seed_position_wrt_map
    return number


if __name__ == "__main__":
    seeds, maps = parse_from_filepath("input.txt")
    n_of_maps = len(maps)
    mapped_numbers = seeds
    for i in range(n_of_maps):
        mapped_numbers = [map_number(number, maps[i]) for number in mapped_numbers]
    answer = min(mapped_numbers)
    
    print(answer)