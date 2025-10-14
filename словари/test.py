dict_1 = {"r": [34, 45],"w":"hello", "y":{34: "hf", (2,3): 34}, "e":23}
for i in dict_1.keys():
    print(i, dict_1[i])
dict_1["r"] = 34
dict_1["y"] = "world"
dict_1["now"] = "nownow"
for item in dict_1.items():
    print(item)
dict_1.update({34:"df", 67:"bn"})
for key in dict_1:
    print(key, dict_1[key])
if "gfdgf" in dict_1:
    print("yes")
