"""一个类的属性是另外一个类的对象"""


class Skill:
    def Q(self):
        print('哈撒k')

    def W(self):
        print('风墙')

    def E(self):
        print('踏前斩')

    def R(self):
        print('狂风觉息斩')


class Hero:
    def __init__(self, name):
        self.name = name
        self.skill = Skill()


'''需求：亚索放技能
2Q，EQ双风W接R
'''

ya_sou = Hero('亚索')
ya_sou.skill.Q()
ya_sou.skill.Q()
ya_sou.skill.E()
ya_sou.skill.Q()
ya_sou.skill.W()
ya_sou.skill.R()

'''
圆环是由两个圆组成的，圆环的面积是外面圆的面积减去内部圆的面积。圆环的周长是内部圆的周长加上外部圆的周长。
这个时候，我们就首先实现一个圆形类，计算一个圆的周长和面积。然后在"环形类"中组合圆形的实例作为自己的属性来用
'''
from math import pi


# 圆
class Circle:
    def __init__(self, r):
        self.r = r

    # 周长
    def perimeter(self):
        return 2 * pi * self.r

    # 面积
    def area(self):
        return pi * self.r * self.r


# 圆环
class CircularRing:
    def __init__(self, inside_r, outer_r):
        # 内圈 圆
        self.inside_track = Circle(inside_r)
        # 外圈 圆
        self.outer_ring = Circle(outer_r)

    # 周长 外圈圆的周长+外圈圆的周长
    def perimeter(self):
        return self.inside_track.perimeter() + self.outer_ring.perimeter()

    # 面积 外圈圆的面积-外圈圆的面积
    def area(self):
        return self.outer_ring.area() - self.inside_track.area()


cr = CircularRing(3, 5)
print(cr.perimeter())
print(cr.area())
