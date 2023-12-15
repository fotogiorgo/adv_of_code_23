num_list = ("zero", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

result = 0

def getNumber(line):
    global result
    first_idx_in_line = float('inf')
    last_idx_in_line = -1
    first_idx_in_list = 0
    last_idx_in_list = 0
    print(line)
    for idx, num in enumerate(num_list):
        i = line.find(num)
        if i != -1:
            #print(f"first found in line index: {i} and list index: {idx}")
            if i < first_idx_in_line:
                first_idx_in_line = i
                first_idx_in_list = idx
            if i > last_idx_in_line:
                last_idx_in_line = i
                last_idx_in_list = idx
    result += (first_idx_in_list % 10) * 10 + (last_idx_in_list % 10)
    print(f"first index in list {first_idx_in_list}: {num_list[first_idx_in_list]}")
    print(f"last index in list {last_idx_in_list}: {num_list[last_idx_in_list]}")
    print(result)

with open("puzzle2.input") as file:
    for line in file:
        getNumber(line)
       # inp = input()
    print (result)
