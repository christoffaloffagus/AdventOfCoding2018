with open('input.txt', 'r') as f:
    all_lines = [line.replace('\n','') for line in f.readlines()]

twos = 0
threes = 0

for line in all_lines:
    check2 = False
    check3 = False
    for char in set(line):
        if check2 and check3:
            break
        if not check2 and line.count(char) == 2:
            check2 = True
            twos += 1
        if not check3 and line.count(char) == 3:
            check3 = True
            threes += 1

print(twos * threes)
