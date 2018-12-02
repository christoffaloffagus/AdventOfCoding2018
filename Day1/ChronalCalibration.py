with open('Input.txt', 'r') as f:
    total = sum([int(line[:-1]) for line in f.readlines()])

print(total)
