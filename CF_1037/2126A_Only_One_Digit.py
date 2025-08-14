t = int(input())

for _ in range(t):
    x = int(input())
    if x == 0:
        print(0)
    
    minimum = 9
    while x:
       minimum = min(x % 10, minimum)
       if minimum == 0:
           break
       x = x // 10

    print(minimum)