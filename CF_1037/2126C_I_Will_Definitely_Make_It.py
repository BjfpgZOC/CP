t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    wl = list(map(int, input().split()))

    curr = wl[k - 1]
    wl.sort()

    print("NO" if any(wl[i] - wl[i - 1] > curr for i in range(1, n)) else "YES")


    


                
