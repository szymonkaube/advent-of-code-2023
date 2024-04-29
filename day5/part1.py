def parse_from_filepath(filepath: str) -> list[list[dict]]:
    with open(filepath) as f:
        text = f.read()
        lines = text.splitlines()

    # Parsing
    lines.append("") # we add "" to dont allow parsing loop get index out of range
    seeds = lines[0][7:].split(" ")
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
                start_end_length = lines[j].split(" ")
                start_end_length_dict = {"dest_start": start_end_length[0],
                                        "source_start": start_end_length[1],
                                        "length": start_end_length[2]}
                current_map.append(start_end_length_dict)
                j += 1
            maps_in_text.append(current_map)
    return maps_in_text


parsed_data = parse_from_filepath("input.txt")

