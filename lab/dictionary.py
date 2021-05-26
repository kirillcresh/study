print("""
Введите в список слова, разделенные строкой
Чтобы выйти напишите "стоп"
""")
string_1 = []
string_2 = []
while (True):
    word = input("Ваше слово: ")
    if word == 'стоп':
        break
    else:
        string_1.append(word)
string_set = set(string_1)
print("Ваши слова: ", string_set)
amount = len(str(string_1).split())
print("Количество слов ", amount)
lenth = str(string_1)
print("Длина строки =", len(lenth) - (int(amount) * 4))
print("Введите новый список из", len(str(string_1).split()), "слов")
for i in range(len(string_1)):
    word2 = input("Ваше слово " + str(i + 1) + ": ")
    string_2.append(word2)
dictionary = {}
dictionary = {string_1[i]: string_2[i] for i in range(amount)}
print("Ваш словарь(первое место-ключи, второе-значения):")
print(dictionary)
input()
