#!/usr/bin/env python3

import re
multi = 0

try:
    with open("corrupted_memory.txt", "r") as file:
        for line in file:
            mulList = re.findall(r"mul\((\d+),(\d+)\)", line)
            for set in mulList:
                multi += int(set[0]) * int(set[1])

        print(f"Multiplication results = {multi}")
except OSError as e:
    print(f"Error reading file: {e}")
    exit()