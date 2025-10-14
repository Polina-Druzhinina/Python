n,m = map(int, input().split())
table_z = list(input().strip() for _ in range(n))
table_t = [list(map(int, input().split())) for _ in range(n)]

code = {0: set('.'), 1: set('.B'), 2: set('.G'), 3: set('.GB'), 4: set('.R'), 5: set('.RB'), 6: set('.RG'), 7: set('.RGB')}
print("YES" if all(table_z[i][j] in code[table_t[i][j]] for i in range(n) for j in range(m)) else "NO")
        
