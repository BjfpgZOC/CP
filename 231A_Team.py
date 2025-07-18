n = int(input())
count = 0

for _ in range(n):
    lst = list(map(int, input().rstrip().split()))
    if sum(lst) >= 2:
        count += 1

print(count)