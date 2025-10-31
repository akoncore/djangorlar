# oop_examples.py
# Примеры объектно-ориентированного программирования:
# Классы, инкапсуляция, наследование, полиморфизм.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f'Привет, меня зовут {self.name}'

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self._balance = float(balance)

    def deposit(self, amount):
        """Пополнение счёта."""
        if amount <= 0:
            raise ValueError('Сумма должна быть положительной.')
        self._balance += amount

    def withdraw(self, amount):
        """Снятие денег со счёта."""
        if amount <= 0:
            raise ValueError('Сумма должна быть положительной.')
        if amount > self._balance:
            raise ValueError('Недостаточно средств.')
        self._balance -= amount

    def get_balance(self):
        """Возвращает текущий баланс."""
        return self._balance

# Пример полиморфизма
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        from math import pi
        return pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h,t):
        self.w = w
        self.h = h
        self.t = t
    def area(self):
        return self.w * self.h * self.t

if __name__ == '__main__':
    p = Person('Akon', 20)
    print(p.greet())

    acc = BankAccount('Akon', 100)
    acc.deposit(60)
    acc.withdraw(10)
    print('Баланс:', acc.get_balance())

    shapes = [Circle(2), Rectangle(1, 2, 5)]
    for s in shapes:
        print('Площадь:', s.area())
