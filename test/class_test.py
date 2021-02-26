# -*- coding: UTF-8 -*-


class People:
    age = 6

    def __init__(self):
        self.name = 'xiaoming'

    def rename(self, name):
        self.name = name
        self.age = 10


class Man(People):
    pass


people1 = People()
print(people1.name)
people1.rename('aaa')
print(people1.name)
p2 = Man()
print(p2.name)
p2.rename('man')
print(p2.name)
print(People.age)
print(people1.age)
