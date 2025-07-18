n = int(input())
x = 0

for i in range(n):
    x = x + 1 if "+" in input() else x - 1

print(x)