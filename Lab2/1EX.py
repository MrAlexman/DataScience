# 1. Дана строка со значениями, которые разделены запятыми:
#
# line = '2019-07-01,organic,4293'
# Напишите функцию column_count, которая возвращает число столбцов в такой строке
def column_count(line):
    return len(line.split(","))

print(column_count("2019-07-01,organic,4293"))