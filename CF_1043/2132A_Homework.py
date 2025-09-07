t = int(input())

for _ in range(t):
    n = int(input())
    a = str(input())
    m = int(input())
    b = str(input())
    c = str(input())

    for i in range(m):
        if c[i] == "D":
            a = a + b[i]
        else:
            a = b[i] + a
    
    print(a)