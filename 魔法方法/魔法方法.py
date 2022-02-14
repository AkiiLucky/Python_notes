#魔法方法

#__init__()
#__del__()
class C:
    def __init__(self):
        print('我是__init__方法，我被调用了...')
    def __del__(self):
        print('我是__del__方法，我被调用了...')

c1 = C()#当创建实例对象时自动调用__init__方法
c2 = c1
c3 = c2
del c3
del c2
del c1 #当一个对象的所有标签都被删除后，启动垃圾回收机制，调用__del__方法

#__new__(cls[, ...]) 目前没有搞懂
class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)

a = CapStr("dark frame master")
print(a)#DARK FRAME MASTER

#基本
# 实例__new__ , __init__ , __del__
# 表现__str__ , __repr__ , __bytes__ , __format__ , __bool__ , __hash__
# 序关系

# 属性访问
# __getattr__(self,name)
# __getattribute__(self,name)
# __setattr__(self,name,value)
# __delattr__(self,name)

# 模仿行为
# Callable(类似函数) __call__
# Container(如list) __getitem__ , __len__ , __reversed__ , __iter__
# 上下文模拟器  __enter__ , __exit__




