print("""
Введите в список слова, разделенные строкой
Чтобы выйти напишите "ё"
""")
string = []
string2 = []
while (True):
    word = input("Ваше слово: ")
    if word == 'ё':
         break
    else:
         string.append(word)
string_set = set(string)
f = open('Lab7_text.txt', 'w')
print("Ваши слова: ",string_set)
kol = len(str(string).split())
print("Количество слов ",kol)
lenth = str(string)
print("Длина строки =",len(lenth)-(int(kol)*4))
print("Введите новый список ",len(lenth)-(int(kol)*4))
for i in range(len(string)):
    word2 = input("Ваше слово "+str(i+1)+": ")
    string2.append(word2)
d = {}
d = {string[i]:string2[i] for i in range(kol)}
print("Ваш словарь(первое место-ключи, второе-значения):")
f.write(str(d))
print(d)
f.close()
input()
