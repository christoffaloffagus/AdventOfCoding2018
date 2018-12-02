with open('Input.txt', 'r') as f:
    all_nums = [int(line.replace('\n','')) for line in f.readlines()]

seen = set((0,))
i = 0
total = 0
length = len(all_nums)
while True:
    total += all_nums[i % length]
    if total in seen:
        break
    else:
        seen.add(total)
    i+=1
print(total)