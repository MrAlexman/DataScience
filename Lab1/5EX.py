# Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого пользователя.
# Вам необходимо написать программу, которая выведет на экран множество уникальных гео-меток всех пользователей.

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
# Результат: {98, 35, 15, 213, 54, 119}

AllList = []
for list in ids.values():
    AllList += list
print(f"Результат: {set(AllList)}")
