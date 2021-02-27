string = input("Введите строку ")
print(len(string), "символов")
print("строка без последнего символа", string[0:-1])
for i in string:
    print(i)
string = input("Введите строку ")
if "с" in string:
    print("Буква 'с' есть в строке")
else:
    print("Буквы 'с' нет в строке")
    string = input("Введите строку ")
    print("Строка до удаления:" + string)
    new_string = ""
    for i in range(0, len(string)):
        if i != 2:
            new_string = new_string + string[i]
    print("Печать строки после удаления:" + new_string)
    input()
