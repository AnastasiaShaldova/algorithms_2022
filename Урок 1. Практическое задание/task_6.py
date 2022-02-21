"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class TaskBoard:
    def __init__(self):
        self.elems = []

    def el_insert(self, el):
        self.elems.insert(0, el)

    def el_size(self):
        return len(self.elems)

    def el_pop(self):
        return self.elems.pop()

    def el_remove(self, other, el):
        other.elems.insert(0, el.el_pop())


main = TaskBoard()  # Основные задачи
improvement = TaskBoard()  # Задачи на доработку

main.el_insert('Задача №1')
main.el_insert('Задача №2')

print(main.el_size())
print(improvement.el_size())

improvement.el_insert('Задача №3')
improvement.el_insert('Задача №4')

print(main.el_size())
print(improvement.el_size())

main.el_remove(improvement, main)

print(main.el_size())
print(improvement.el_size())

print(improvement.el_pop())
main.el_remove(improvement, main)

print(main.el_size())
print(improvement.el_size())


