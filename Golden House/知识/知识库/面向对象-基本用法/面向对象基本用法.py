#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: R.
# email: sy.mailbox@foxmail.com
class Person:
    role = 'person'

    def __init__(self, name, attack, hp):
        self.name = name
        self.attack = attack
        self.hp = hp

    def hit(self, dog):
        # self 代表人类的对象，dog代表狗类的对象
        dog.hp -= self.attack


class Dog:
    role = 'dog'

    def __init__(self, name, breed, attack, hp):
        self.name = name
        self.breed = breed  # 品种
        self.attack = attack
        self.hp = hp

    def bite(self, person):
        # self 代表狗类的对象，person代表人类的对象
        person.hp -= self.attack


# 实例一个人和一只狗
xiao_wang = Person('小王', 10, 1000)
re_ha = Dog('二哈', '哈士奇', 3, 500)

# 开打前双方血量展示
print('小王的血条={}'.format(xiao_wang.hp))
print('二哈的血条={}'.format(re_ha.hp))
# 小王的血条=1000
# 二哈的血条=500

# 攻击开始
'''小王连续踢了三下狗'''
for i in range(3):
    xiao_wang.hit(re_ha)

'''二哈咬了一下小王'''
re_ha.bite(xiao_wang)

# 打完后双方血量展示
print('小王的血条={}'.format(xiao_wang.hp))
print('二哈的血条={}'.format(re_ha.hp))
# 小王的血条=997
# 二哈的血条=470
