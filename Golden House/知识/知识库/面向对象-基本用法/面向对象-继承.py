class A:
    a = 1

    def __init__(self, aa, aaa):
        self.aa = aa
        self.aaa = aaa

    def ay(self):
        print('A')


class B(A):
    """B继承A，B的对象可以调用A和B的属性和方法"""

    def by(self):
        print('B')


# b=B(1,11)
# b.ay()
# b.by()
# print(b.a)

class C(A):
    """继承父类的构造方法，2种写法，如果继承多个类就不要用super()这种方法了"""

    def __init__(self, aa, aaa, bb):
        # A.__init__(self,aa,aaa)
        super().__init__(aa, aaa)
        self.bb = bb

    def cy(self):
        print('C')


# c=C('aa','aaa','bb')
# c.ay()
# c.cy()
# print(c.aaa)
# print(c.bb)

class D(A):
    """重写父类方法,方法名相同,如果想使用父类被重新的方法，可以使用super().ay()或者A.ay(self)使用"""

    def dy(self):
        print('D')

    def ay(self):
        print('重新父类方法A-D')

    def ay_A(self):
        A.ay(self)
        super().ay()

# d=D('aa','aaa')
# d.ay()
# d.dy()
# d.ay_A()
