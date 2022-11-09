# Дана переменная, в которой хранится информация о затратах и доходе рекламных кампаний по различным источникам.
# Необходимо дополнить исходную структуру показателем ROI, который рассчитаем по формуле: (revenue / cost - 1) * 100

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}

for key, value in results.items():
    i = 0
    for key1, value1 in value.items():
        if (i == 0):
            revenue = value1
            i += 1
        else:
            cost = value1
            break
    value["ROI"] = round((revenue / cost - 1) * 100, 2)
c = (dict)(sorted(results.items()))
for key2, value2 in c.items():
    print("{0}: {1}".format(key2, value2))
