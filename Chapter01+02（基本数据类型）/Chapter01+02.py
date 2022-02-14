print("ABC")                 #输出ABC
print(1+2)                   #输出1+2的结果
a,b=1,2
a,b=b,a                      #a,b数值互换
print(a,b)
print(0b101011001)           #将二进制转换为十进制
print(0o15762)               #将八进制转换为十进制
print(0x15FE2)               #将十六进制转换为十进制
print(int(1.37e3))           #输出1370
print(complex(5,3))          #创建复数5+3j
x=5+2j
print(x.real)                #输出x的实部
print(x.imag)                #输出x的虚部
print(type(x.real))          #输出x的实部类型
print(type(x.imag))          #输出x的虚部类型
y=1.32
print(int(y))                #将浮点数转换为整数
y=1
print(float(y))              #将整数转换为浮点数
print("ABC")                 #输出ABC
print('''Jack says:"Let's go to School."''')#Jack says:"Let's go to School."
print('Aa'+'Bb'+'Cc')        #输出AaBbCc
print('abc'*5)               #输出abcabcabcabcabc
print('They\'re students.')  #\'为转义字符单引号，单引号里还有单引号时必须用转义字符
print("d:\computer\nlp")
print(r"d:\computer\nlp")    #\n为换行符，若不需要转义，在字符串前加r或R
print("\\")                  #\\代表一个反斜杠
print(R"\\")
print("This is a Python \
Program.")                   #反斜杠可作续航符，表示下一行是上一行的延续
print(len("四川大学a15"))    #返回字符串的个数
s="aBc"
print(s.upper())
print(s.lower())             #大小写转换
print(s.capitalize())        #首字母大写
print("zzuczq".count("z"))   #搜索字符串"z"出现的次数
print("*scu*".strip("*"))    #删除两边的字符
print("*scu*".rstrip("*"))   #删除右边的字符
print("*scu*".lstrip("*"))   #删除左边的字符
s="*scu*"
print(s.replace("scu","四川大学"))#将scu替换为四川大学
a,b=9,2
print(a**2)                  #**为乘幂
print(a//b)                  #//为整除
print(a%b)                   #%为取余数
print(a==b)                  #False
print(a!=b)                  #True
print(a>b)                   #True
print(a<b)                   #False
print(a>=b)                  #True
print(a<=b)                  #False
a,b=1,0
print(a and b)               #0
print(a or b)                #1
print(not a)                 #False
print(not b)                 #True
print(2 and 3)               #3
print(2 or 3)                #2
print(abs(-3.7))             #返回数字的绝对值 
print('1+1')                 #输出1+1
print(eval('1+1'))           #输出2 eval函数用来执行一个字符串表达式，并返回表达式的值
print(int('11',2))           #将二进制的11转换为十进制的3
print(int(11.0))             #将浮点数转换为整数
print(pow(2,4))              #2的4次幂
print(list(range(0,10,2)))   #创建一个从0到10的等差数列（不包括10），步长为2
print(round(3.1415926,2))    #保留小数点后两位
str(10)                      #'10' 把对象转换为字符型

#print输出函数----基本格式：print([object1,...][, sep=''][,end='\n'])
print(12,34,56,78,sep='@')   #sep为分隔符，可指定"@"为分隔符(替代其中的逗号），不指定sep则分隔符为空格
print("score",end="=");print(95)#end表示结尾符号，用来设定以什么为结尾，输出为一行
print("score");print(95)     #若省略end，则相当与换行符\n,即输出为两行
#print格式化输出
age=19
print("Jack的年龄:%d岁"%age)                          #%d是格式化符号，代表十进制整数(%o为八进制整数，%x为十六进制整数）
age=20
print("%s的年龄:%d岁"%("Lucy",age))                   #格式化符号%s代表字符串，其他：%f或%F代表浮点数，
print("%6s的2月份工资：%8.2f元"%("Jack",3566))
print("%6s的2月份工资：%8.2f元"%("Peter",1363.126))
print("%6s的2月份工资：%8.2f元"%("Tom",35663.1))
'''%6s表示字符串的宽度为6，如果字符个数少于6个，在字符串左边补空格使上下人名右对齐。
%8.2f表示浮点数的宽度为8，小数占2位，小数点占1位，当浮点数小于8位时，在浮点数左边补空格使上下行的工资数额右对齐'''
result=1284841848.255
print("计算结果为%E"%result)                          #%E表示指数形式的浮点数
print("{}是我们的数学老师。".format("张三"))          #{}内用format()里面的自变量替换
print("{}的大学计算机成绩为{}分".format("李四",90))   #{}为空时，按顺序填入
print("{0}的大学计算机成绩为{1}分".format("李四",90)) #{0}表示使用的第一个自变量，{1}表示使用的第二个自变量
print("{name}的大学计算机成绩为{score}分".format(name="李四",score=90))#以上三式结果均为：李四的大学计算机成绩为90分
print("{0:.4}".format(31.1415926))                    #保留4位有效数字（在数字编号后面加冒号，可以指定参数格式）
print("{0:6}的期末总分为{1:<8}".format("Peter",187))  #{0:6}代表字符串的宽度为6，<代表左对齐
print("{0:6}的期末总分为{1:@>8}".format("Jack",258))  #{1:@>8}中>代表右对齐，@代表填充空格
print("{0:6}的期末总分为{1:*^8}".format("Jerry",356)) #{1:*^8}中8代表字符宽度为8，^代表居中对齐，*为填充字符

#input输入函数----基本格式：变量=input("提示字符串")
x=eval(input("请输入数据："))#在程序执行时，遇到input函数回先等待用户输入数据，用户输入数据并按Enter键之后，input()函数将用户按Enter键之前的全部输入数据以字符串格式返回，使用eval()函数可以计算字符串中表达式的值并返回存入变量中
print(x)       #x    x为字符型
x=input("请输入数据：")
print(x)       #'x'  x为字符串，两者有区别
print(float(x))#float()函数可以将字符串转换为浮点型
y=eval(input("Jack的一月份的工资："))
z=eval(input("Peter的一月份的工资："))
print("Jack的一月份工资为{0:.2f}".format(y))#保留小数点后两位
print("Peter的一月份工资为{0:.2f}".format(z))

x=eval(input("请输入Jack的一月份工资："))
y=eval(input("请输入Peter的一月份工资："))
z=eval(input("请输入Jerry的一月份工资："))
print("{0:<6}的一月份工资为{1:*>8.2f}".format("Jack",x))
print("{0:<6}的一月份工资为{1:*>8.2f}".format("Peter",y))
print("{0:<6}的一月份工资为{1:*>8.2f}".format("Jerry",z))

x,y,z=eval(input("请输入x,y,z的值:"))#注意数字要用英文输入法的逗号隔开
print("x,y,z,的值分别为:{0}，{1}，{2}".format(x,y,z))

#math库
import math     #使用前先导入math库
x=math.fabs(-19)#math.fabs()代表返回原来数值的绝对值
print(x)        #其他math函数可通过网络查找

#random模块
import random
print(random.choice([1,3,5,7,9,])) #从序列中随机取一个元素
print(random.random())             #随机产生[0,1)范围内的一个实数
print(random.randint(1,100))       #随机产生[1,100]范围内的一个整数
print(random.uniform(1,100))       #随机产生[1,100]范围内的一个实数
print(random.randrange(1,100,2))   #随机产生[1,100]范围内的一个奇数
print(random.randrange(0,100,2))   #随机产生[0,100]范围内的一个偶数（后面的2是步长，如果变为3就代表每隔3个数取一个，也就是[0，3，6，9....96，99]中取一个）
print(random.sample('abcdef',3))   #从abcdef中随机提取3个元素
x=[2,8,15,23]
random.shuffle(x)                  #将原先顺序打乱
print(x)                           #注意x是一组数，不能用print(random.shuffle(x))
