with open('Input.txt', 'r') as f:
    total = sum([int(line.replace('\n','')) for line in f.readlines()])

print(total)
