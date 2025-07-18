n = int(input())
lst = list(map(int, input().rstrip().split()))

maximum, index = lst[0], 0
sec_max = -1

for i in range(n):
    if lst[i] > maximum:
        sec_max = maximum
        maximum = lst[i]
        index = i
    elif lst[i] > sec_max and lst[i] < maximum:
        sec_max = lst[i]

print(index + 1, sec_max)

