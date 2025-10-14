lst = [int(x) for x in input().split()]
lenn = len(lst)
print(*([lst[0]] if lenn == 1 else [lst[i-1] + lst[(i+1)%lenn] for i in range(lenn)]))
