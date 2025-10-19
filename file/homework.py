with open("roles.txt", "r", encoding="utf-8") as file:
    lst = [i.strip() for i in file if i.strip() and i.strip()!="roles:"]
    
isText = True
roles = []
textlines = []

for i in lst:
    if i == "textLines:":
        isText = False
        continue
    (roles if isText else textlines).append(i)
    
combined_lines = []
current_phrase = ""
for line in textlines:
    if any(line.startswith(i + ":") for i in roles):
        if current_phrase:
            combined_lines.append(current_phrase)
        current_phrase = line
    else:
        current_phrase += " " + line
if current_phrase:
    combined_lines.append(current_phrase)

count = 1
res = dict()
for i, value in enumerate(combined_lines, 1):
    name, phrase = value.split(":", 1)
    name = name+":"
    if name not in res:
        res[name] = []
    res[name].append(f"{i}){phrase.strip()}")

for name in roles:
    if name + ":" not in res:
        res[name + ":"] = []

res_text = open("res.txt", "w", encoding="utf-8")
for role, phrase in res.items():
    res_text.write(f"{role}\n") 
    for i in phrase:
        res_text.write(f"{i}\n")
    res_text.write("\n")
res_text.close()
