#!/usr/bin/env python3

import re
lines_to_read = []

with open("corrupted_memory.txt", "r") as file:

    # initialy reading is enabled
    start, stop = True, False

    for line in file:
        for i in range(len(line)):

            # beggining of the line/do() was found and don't() was found
            if start and stop:
                if start == True:
                    start = 0
                lines_to_read.append(line[start:stop])
                start, stop = False, False

            # beggining of the line/do() was found and end of the line reached
            elif start and i == len(line)-1:
                stop = i
                lines_to_read.append(line[start:stop])

                # reading is alowded form the beginning of the line if it did not end with don't()
                start, stop = True, False

            # only acknowlandge don't() if it comes after when reading allowded
            elif start and line[i:i+len("don't()")] == "don't()":
                stop = i+len("don't()")

            # only enabled when start initially is set to False
            elif line[i:i+len("do()")] == "do()" and not start:
                start = i

multi = 0
for line in lines_to_read:
    #print(line)
    mulList = re.findall(r"mul\((\d+),(\d+)\)", line)
    for set in mulList:
        multi += int(set[0]) * int(set[1])

print(f"Multiplication results = {multi}")