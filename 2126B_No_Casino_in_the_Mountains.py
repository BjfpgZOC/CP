t = int(input())

for _ in range(t):
    n, k = tuple(map(int, input().rsplit()))
    w = list(map(int, input().rsplit()))
    max_hike = 0

    i = 0
    while i < n:
        if w[i] == 0:
            hike = True
            if i + k > n:
                break
            j = i
            while j < i + k:
                if w[j] != 0:
                    hike = False
                    i = j + 1
                    break
                j += 1
            if hike:
                max_hike += 1
                i = i + k + 1
        else:
            i += 1

    print(max_hike)
            



