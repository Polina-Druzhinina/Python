import os
#print(os.getcwd()) где находится файл
#print(os.path.join("C:\\", "users", "Documents")) #собирает путь
#print(os.listdir("английский")) #список содержимого в файле
#os.makedirs(os.path.join('test_dir', 'level_1', 'level_2','level_3')) создание файла с вложеннвми файлами

my_file = open("my_text.txt", "w") #w  - файл может не существовать, в других должен существовать
#my_file.write("Hello\n")
#my_file.write("45\n")
#my_file.writelines(["fdfd ", "fdffd"]) #запись
print(my_file.readline())
my_file.close()