t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    print(sum(max(0, i - j) for i, j in zip(a, b)) + 1)