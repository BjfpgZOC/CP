import math

t = int(input())

for _ in range(t):
    n = int(input())
    arr = [0] * n
    
    for i in range(n):
        if i % 2 == 0:
            arr[i] = -1
        else:
            arr[i] = 2 if i == n - 1 else 3

    print(" ".join(map(str, arr)))