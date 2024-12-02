#!/usr/bin/env python3

list1, list2, = [], []

# file reading into two lists of numbers
try:
    file = open("IDs_lists.txt", "r")
    for line in file:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))
    file.close()
except OSError as e:
    print(f"Error reading file: {e}")
    exit()  # Exit the program if the file can't be read

# check if lists have the same number of IDs and sort the lists if so
if len(list1) == len(list2):
    #print(f"Both list have eaqual number of IDs, which is {len(list2)}")
    list1.sort()
    list2.sort()

    # calculate the difference between numbers
    sum_of_differences = sum(abs(list1[i]-list2[i]) for i in range(len(list2)))
    print(f"The sum of dofferences is {sum_of_differences}")

else:
    print(f"The number of IDs in the list does not match. 1st list has {len(list1)} IDs while the 2nd list has {len(list2)} IDs")

# make a dict from the first list with initial counts as 0
IDs_Dict = {}
for ID in list1:
    IDs_Dict[ID] = 0
#print(IDs_Dict)

# iterate throught the second list and count occurrences of each ID
for ID in list2:
    if ID in IDs_Dict.keys():
        IDs_Dict[ID] += 1
#print(IDs_Dict)

print(f"The similarity score is: {sum(ID * IDs_Dict[ID] for ID in list1)}")
