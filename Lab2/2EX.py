# 2.  Создайте класс сотрудника Employee. При инициализации класса задается имя сотрудника name и его текущая
# зарплата salary. Напишите следующие методы:
# Метод up, который увеличивает зарплату сотрудника на 100
# Метод print, который выводит на экран текущую зарплату сотрудника в формате "Сотрудник Иван, зарплата 100"

class Employee():
    def __init__(self, name, salary):
        """
        :param name: str
        :param salary: int
        """
        self.name = name
        self.salary = salary


    def up(self):
        """
        Raises the salary by 100
        """
        self.salary += 100

    def print(self):
        """
        Prints "Emloyee 'Name', salary 'Salary'"
        """
        print(f"Emloyee {self.name}, salary {self.salary}")


Vasilii = Employee("Vasilii Ivanovich", 4000)
Vasilii.up()
Vasilii.print()