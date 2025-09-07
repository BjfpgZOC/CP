t = int(input())

wm = [1]
while wm[-1] * 3 <= 10**9:
    wm.append(wm[-1] * 3)

deal_cost = []
for i, nw in enumerate(wm):
    pre_cost = nw * 3
    if i > 0:
        pre_cost += i * wm[i - 1]
    deal_cost.append(pre_cost) 

for _ in range(t):
    n = int(input())
    cost = 0

    for i in range(len(wm) - 1, -1, -1):
        wm_dc = n // wm[i]
        if wm_dc:
            cost += wm_dc * deal_cost[i]
            n -= wm_dc * wm[i]
    
    print(str(cost))


    