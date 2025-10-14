str_1 = input().split()
dict_1 = {}

for key in str_1:
    if key not in dict_1:
        dict_1[key] = 1
    else:
        dict_1[key] += 1
max_key = max(dict_1, key=dict_1.get)
min_key = min(dict_1, key=dict_1.get)
print(max_key,  ":",  dict_1[max_key])
print(min_key,  ":",  dict_1[min_key])
