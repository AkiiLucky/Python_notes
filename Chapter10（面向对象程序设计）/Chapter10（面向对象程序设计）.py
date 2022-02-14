#类和对象
class Ball:#Ball是类名，冒号后面的是类体
    
    name = '球'     #定义属性
    color = '红色'  
    
    def setname(self,name):#定义方法
        self.name = name
    def kick(self):
        print('我是{0}的{1}，该死的，谁踢我。。。'.format(self.color,self.name))


#下面的 a 和 b 是同属Ball类的不同对象
        
a = Ball()#创建实例对象
print(a.name)
print(a.color)
a.color = '绿色'#调用属性
a.setname('球A')#调用方法
a.kick()
print(a.name)
print(a.color)


b = Ball()#创建另一个实例对象
print(b.name)
print(b.color)
b.color = '蓝色'#调用属性
b.name = '球B'  #调用属性
b.kick()
print(b.name)
print(b.color)


#__init__(self,param1,param2...)
class character:

    def __init__(self,name='动漫角色'):#当创建一个实例对象后自动调用此函数
        self.name = name

    def say(self):
        print('我是{}，欢迎来到二次元！！！'.format(self.name))
        
role = character()
role.say()
role = character('小埋')
role.say()#我是小埋，欢迎来到二次元！！！

#公有和私有（伪）
class person:
    __name = '土间埋'#将name隐藏
    def setname(self):
        return self.__name

role = person()
print(role.setname())#可以从内部调用name
print(role._person__name)#也可以这样调用name，但是用role.__name 或 role.name 都是无法调用name的


#继承
class parent:
    
    name = "保罗"

    def hello(self):
        print("正在调用父类的方法...")

class child(parent):#子类继承父类的属性和方法
    pass

g = child()
g.hello()#正在调用父类的方法...
print(g.name)#保罗

class child(parent):#子类中定义与父类同名的属性和方法会将父类中同名的属性和方法代替
    
    name = "鲁迪乌斯"

    def hello(self):
        print("正在调用子类的方法...")

g = child()
g.hello()#正在调用子类的方法...
print(g.name)#鲁迪乌斯


#多重继承
class cha1:
    def say1(self):
        print("我是日向创")

class cha2:
    def say2(self):
        print("我是苗木诚")

class cha(cha1,cha2):
    pass

CHA = cha()
CHA.say1()
CHA.say2()
    
#类的组合
class Turtle:
    def __init__(self,x):
        self.num = x

class Fish:
    def __init__(self,y):
        self.num = y

class Pool:
    def __init__(self,x,y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_num(self):
        print('水池中乌龟有 %d 只，小鱼有 %d 只' % (self.turtle.num,self.fish.num))

pool = Pool(2,10)
pool.print_num()

#类，类对象，实例对象
class C:#定义一个类
    count = 0

a = C()
b = C()

print(a.count)#0
print(b.count)#0

print(C.count)#0

b.count += 10
print(b.count)#10
print(a.count)#0
print(C.count)#0

C.count += 100 #这里的 C 指类对象
print(C.count)#100
print(a.count)#100
print(b.count)#10  这里的b是实例对象，b.count已经赋值了

#新定义的属性如果与方法同名，则会替代原方法
class C:
    def fun(self):
        print("abd")

c = C()
c.fun()#abd
c.fun = 123
print(c.fun)#123  如果调用c.fun()会报错，因为这个函数已经被属性代替

#删除类对象后，实例对象依旧能调用类对象的属性和方法
class Cat:
    def say(self,x):
        print('喵喵喵，我是%s！' %(str(x)))

cat = Cat()
cat.say('巧克力')

del Cat
cat.say('香子兰')

#一些与类相关的BIF
#issubclass(class,classinfo)  检查class是否为classinfo的子类，是则返回True，否则返回False
class A:
    pass

class B(A):
    pass

class C:
    pass

print(issubclass(B,A))#True
print(issubclass(B,B))#True

print(issubclass(B,object))#True object是基类，所有类都是它的子类
print(issubclass(A,object))#True
print(issubclass(C,object))#True

print(issubclass(A,B))#False
print(issubclass(C,B))#False
print(issubclass(B,C))#False
print(issubclass(A,C))#False

#isinstance(object,classinfo)  检查object是否为classinfo的一个子类
class A:
    pass

class B(A):
    pass

class C:
    pass

b1 = B()
print(isinstance(b1,B))#True
print(isinstance(b1,A))#True
print(isinstance(b1,C))#False
print(isinstance(b1,(A,B,C)))#True b1是(A,B,C)其中一个类的的子类则返回True

print()

#hasattr(object,name)判断object是否含有name属性
#getattr(object,name[,default])获得object的属性值
#setattr(object,name,value)设置object的属性值
#delattr(object,name)删除object的属性
class Person:
    def __init__(self,name='小埋'):
        self.name = name
        
person = Person()

print(hasattr(person,'name'))#True
print(hasattr(person,'age'))#False

print(getattr(person,'name'))# '小埋'
print(getattr(person,'age','你访问的属性不存在...'))#'你访问的属性不存在...'

setattr(person,'age','17岁')
print(getattr(person,'age','你访问的属性不存在...'))#'17岁'

delattr(person,'age')
print(getattr(person,'age','你访问的属性不存在...'))#'你访问的属性不存在...'

#property()
class Cat:
    def __init__(self,size=10):
        self.size = size
    def getsize(self):
        return self.size
    def setsize(self,value):
        self.size = value
    def delsize(self):
        del self.size  
    x = property(getsize,setsize,delsize)

cat = Cat()
print(cat.x)#10
print(cat.size)#10
cat.x = 20
print(cat.x)#20
print(cat.size)#20
del cat.x
print(getattr(cat,'size','你访问的属性不存在...'))#你访问的属性不存在...
