#!/usr/bin/env python3

# file reading into two lists of numbers
safe_reports = 0

try:
    with open("reports.txt", "r") as file:    

        for line in file:
            numbers = [int(num) for num in line.split()]

            is_safe = True
            increasing = numbers[0] < numbers[1]

            for i in range(len(numbers)-1):
                diff = abs(numbers[i] - numbers[i + 1])

                if diff not in {1, 2, 3}:
                    is_safe = False
                    break

                if increasing and numbers[i] > numbers[i+1]:
                    is_safe = False
                    break

                if not increasing and numbers[i] < numbers[i+1]:
                    is_safe = False
                    break

            if is_safe:
                safe_reports += 1
                if increasing:
                    pass
                    #print(f"Increasing: {numbers}")
                else:
                    pass
                    #print(f"Decreasing: {numbers}")
        
except OSError as e:
    print(f"Error reading file: {e}")
    exit()  # Exit the program if the file can't be read

print(f"In total {safe_reports} safe reports were found!")
