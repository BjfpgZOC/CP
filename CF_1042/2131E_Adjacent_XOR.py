t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if a[-1] != b[-1]:
        print('NO')
        continue

    px = [0] * (n + 1)
    for i in range(n):
        px[i + 1] = px[i] ^ a[i]

    possible = True
    i = 0
    while i < n - 1:
        if b[i] == a[i]:
            i += 1
            continue

        found = False
        for r in range(i + 1, n):
            if (px[r + 1] ^ px[i]) == b[i]:
                good = True
                for j in range(i + 1, r):
                    if (px[r + 1] ^ px[j]) != b[j]:
                        good = False
                        break
                if good:
                    i = r
                    found = True
                    break
        if not found:
            possible = False
            break

    print("YES" if possible else "NO")