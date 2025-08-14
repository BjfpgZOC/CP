t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))

    s = [0 if (i % k == 0) else min(i % k, k - (i % k)) for i in s]
    t = [0 if (i % k == 0) else min(i % k, k - (i % k)) for i in t]
         
    s.sort()
    t.sort()

    print(['NO', 'YES'][s == t])