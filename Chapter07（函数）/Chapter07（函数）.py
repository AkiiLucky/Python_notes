#函数
def add(num1,num2):
    result = num1 + num2
    print(result)
    
add(5,6) #11

def add(num1,num2):
    return (num1 + num2)#函数的调用过程

print(add(5,5))  #10

def pr(n):#n是形参
    print(n,'--OK')

a=['A','B','C','D']
for i in a:
    pr(i)    #i是实参

def back():
    return [1,'天山',4.13]

print(back())#[1, '天山', 4.13]

#关键字参数
def F(a,b):
    print('a='+ str(a) , 'b='+ str(b))

F(1,2)    #a=1 b=2
F(b=1,a=2)#a=2 b=1  a,b根据形参来表明为哪个形参传递什么值

#默认值参数
def app(a='海绵宝宝',b='是动画角色'):
    print(a+b)

app()         #海绵宝宝是动画角色
app('派大星') #派大星是动画角色
app(b='是派大星的好朋友')#海绵宝宝是派大星的好朋友
app(1,2)#3

#收集参数（可变长度参数）:在参数名前加*，可以接受多个实参并将其放入一个元组中
def F(*num):
    print('参数的长度是',len(num))

F(2,3,4,5,6)#参数的长度是 5

#局部变量与全局变量
def discounts(price,rate):
    final_price = price * rate#这里的final_price，price，rate是局部变量
    return final_price

old_price = float(input('该商品的原价：'))
rate = float(input('折扣率：'))
new_price = discounts(old_price,rate)#这里的new_price，old_price,rate是全局变量
print('该商品打折后的价格：',new_price)

count = 5
def count():
    global count#利用global关键字可以将局部变量改变为全局变量
    count = 10
    print(10)
count()#10
print(count)#10

#内嵌函数
def fun1():
    print('fun1()正在被调用...')
    def fun2():
        print('fun()正在被调用...')
    fun2()
    
fun1()

#闭包
def fun1(a,b):
    def fun2(x):
        return a * x - b
    return fun2

fun2 = fun1(2,3)
print(fun2(5))#7
print(fun1(2,3)(5))#7  两种调用闭包的方法

#nonlocal 关键字
def fun1():
    x = [5]
    def fun2():
        x[0] *= x[0]
        return x[0]
    return fun2()

print(fun1())#25

def fun1():
    x = 5
    def fun2():
        nonlocal x#此时 x 不是局部变量
        x *= x
        return x
    return fun2()

print(fun1())#25

#匿名函数 lambda
g = lambda x: 5*x + 3*x*x + 1
print(g(5))
f = lambda x,y: 5 * x + 6 * y + x * y
print(f(3,4))

#filter过滤器
print(list(filter(None,[1,0,True,False])))#[1, True]

def fun1(n):
    return n % 2
print(list(filter(fun1,range(10))))#[1, 3, 5, 7, 9]

print(list(filter(lambda n: n % 2,range(10))))#[1, 3, 5, 7, 9]  筛选出0到10之间的奇数

#map()函数
print(list(map(lambda n: n*2,range(10))))#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]  分别对原序列中各个位置的元素进行函数运算，并将结果放入原位置

#递归函数
def fun1(n):
    sum1 = 1
	
    if n >= 0:
	    
            for i in range(1,n+1):
                
                    sum1 = sum1 * i
		
    elif n == 0:

            sum1 = 1
	
    else:
            
        print('n必须大于等于0')
            
    print('n!=',sum1)#用迭代的方法计算 n!

def fun2(n):
    
    if n == 0:
        
        return 1
    
    else:

        return n * fun2(n-1)#用递归函数算 n!
    
#利用递归函数求斐波那契数列
def fab(n):
    if n==1 or n==2:
        return 1
    
    else:
        return fab(n-1) + fab(n-2)
        
for n in range(1,20):
    print(fab(n),end=' ')
    if (n % 10 == 0):   #每10个换行
        print()
        
print()

#用迭代方法求斐波那契数列
def fab1(n):
    n1 = 1
    n2 = 1
    n3 = 1
    
    if n==1 or n==2:
        return 1

    elif n <= 0:
        print('输入有误')
        return -1
    
    else:
        while n >2:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            n = n - 1
        return n3

for n in range(1,20):
    print(fab(n),end=' ')
    if (n % 10 == 0):   #每10个换行
        print()

print()

#利用递归函数求汉诺塔移动路径
def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)

    else:
        hanoi(n-1,x,z,y)
        print(x,'-->',z)
        hanoi(n-1,y,x,z)

n = eval(input("请输入汉诺塔的层数："))
hanoi(n,1,2,3)#1,2,3代表3根柱子，n代表第1根柱子上初始的圆盘数

        


