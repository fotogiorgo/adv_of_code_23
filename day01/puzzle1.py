with open("puzzle1.input") as file:
    result = 0
    for line in file:
        for c in line:
            if c.isdigit():
                result += (int(c) * 10)
                break
        for c in reversed(line):
            if c.isdigit():
                result += int(c)
                break
    print (result)
