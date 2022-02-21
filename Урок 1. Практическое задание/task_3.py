"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


# O(N log N) - Линейно-Логарифмическая
def company_one_res(el):
    res = list(el.items())  # O(N) - Линейная
    res.sort(key=lambda v: v[1], reverse=True)  # O(N log N) - Линейно-Логарифмическая
    for v in range(3):  # O(1) - Константная
        return dict(res[:3])  # O(1) - Константная


# O(N) - Линейная
def company_two_res(el):
    res = list(el.items())  # O(N) - Линейная
    for v in range(3):  # O(1) - Константная
        for i in range(v + 1, len(res)):  # O(N) - Линейная
            if res[i][1] > res[v][1]:  # O(1) - Константная
                res[i], res[v] = res[v], res[i]  # O(1) - Константная
    return dict(res[0:3])  # O(1) - Константная


storage = {
    'Пятерочка': 1500,
    'Ашан': 2000,
    'Ярче': 1000,
    'ИП Кузнецов К.В.': 100,
    'Дикси': 900,
    'METRO': 3000,
    'Перекресток': 1450
    }


print(company_one_res(storage))
print(company_two_res(storage))