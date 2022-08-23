# 需求1:
# 计算两个整数的和, 当和等于10的时候,显示10,等和大于10的时候,显示太大了
# 当和小于10的时候,显示太小了

# 需求2:
# 计算两个整数的和, 当和等于100的时候,显示100,等和大于100的时候,显示太大了
# 当和小于100的时候,显示太小了

# def my_sum(a, b):
#     c = a + b
#     if c == 100:
#         print(c)
#     elif c > 100:
#         print("太大了")
#     else:
#         print("太小了")
#
# my_sum(4, 5)

def my_sum(a, b):
    return a + b

a = my_sum(4, 5)
if a == 100:
    print(a)
elif a < 100:
    print("太小了")
else:
    print("太大了")

# 程序设计有个原则,需求是不停的变化的,
# 可以修改函数外部的代码,但函数定义后,不应该修改函数内部的代码