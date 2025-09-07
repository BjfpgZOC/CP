t = int(input())
possible = [10**k + 1 for k in range(1, 19)]

for _ in range(t):
    n = int(input())
    res = []

    for div in possible:
        if n % div == 0:
            res.append(n // div)
    
    res.sort()
    
    if res:
        print(len(res))
        print(" ".join(str(val) for val in res))
    else:
        print(str(0))
    
