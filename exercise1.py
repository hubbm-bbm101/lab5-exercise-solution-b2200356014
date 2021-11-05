N = int(input())
total = 0
total1 = 0
for num in range(1, 1+N):
    if num % 2 == 1:
        total += num
    else:
        total1 += num
total1 /= N

print(total, total1)
