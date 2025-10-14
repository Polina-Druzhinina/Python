w, h = map(int, input().split())
n = int(input())
table = [[0 for _ in range(w)] for _ in range(h)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            if 0 <= x < w and 0 <= y < h:
                table[y][x] = 1
print(sum(cell==0 for row in table for cell in row))

    
    
