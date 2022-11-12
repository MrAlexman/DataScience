# Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж.
# Напишите программу, которая возвращает название канала с максимальным объемом продаж.

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

print(f"Максимальный объем продаж на рекламном канале: {max(stats, key=stats.get)}")