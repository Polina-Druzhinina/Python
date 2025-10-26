import json

name = input("Enter Name:")
login = input("Enter login:")
last_time = input("Enter last tinme:")
lenght_of_stay = int(input("Enter lenght of stay:"))

user = {"name":name, "Login":login, "Last Time":last_time, "Length of stay": lenght_of_stay}

file = open("json.txt", "r", encoding="utf-8")
content = file.read()
file.close()

if content.strip() == "":
    data_users = dict()
else:
    data_users = json.loads(content)

if "users" not in data_users:
    data_users["users"] = []

data_users["users"].append(user)

file = open("json.txt", "w", encoding="utf-8")

json.dump(data_users, file, skipkeys=True,ensure_ascii=False, check_circular=True, indent=4, separators=(",",": "), sort_keys=False)


print(json.dumps(data_users, ensure_ascii = False, indent=4))
file.close()

