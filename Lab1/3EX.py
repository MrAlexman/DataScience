# Мы делаем  dating-сервиса, и у нас есть список парней и девушек.
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена по алфавиту и познакомим людей
# с одинаковыми индексами после сортировки! Но мы не будем никого знакомить, если кто-то может остаться без пары
Nboys = (int)(input("Введите количество мальчиков:\n"))
Ngirls = (int)(input("Введите количество девочек:\n"))
if Nboys == Ngirls:
    N = Ngirls
    i = 1
    boys = []
    girls = []
    print("Введите имена девочек:\n")
    while (i <= N):
        print("Девочка №", i)
        girls.append(input())
        i += 1
    boys.sort()
    i = 1
    while (i <= N):
        print("Мальчик №", i)
        boys.append(input())
        i += 1
    girls.sort()
    bg = list(zip(boys, girls))
    print("Идеальные пары:")
    for v in bg:
        print(f"{v[0]} и {v[1]}")
else:
    print("Кто-то может остаться без пары!\n")
