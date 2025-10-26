import os
#print(os.getcwd()) где находится файл
#print(os.path.join("C:\\", "users", "Documents")) #собирает путь
#print(os.listdir("английский")) #список содержимого в файле
#os.makedirs(os.path.join('test_dir', 'level_1', 'level_2','level_3')) создание файла с вложеннвми файлами
global my_file
try:
    my_file = open("my_text.txt", "r") #w  - файл может не существовать, в других должен существовать
    #my_file.write("Hello\n")
    #my_file.write("45\n")
    #my_file.writelines(["fdfd ", "fdffd"]) #запись
    s = my_file.readline()
    str_list = []
    raise Exception
    while s != "":
        str_list.append(s)
        s = my_file.readline()
    print(str_list)
    my_file.close()
except FileNotFoundError as fnfe:
    print("Файл не найден", fnfe)
except NameError as ne:
    print("Неверное имя файла")

except Exception as ex:
    print("что-то произошло",  ex)

