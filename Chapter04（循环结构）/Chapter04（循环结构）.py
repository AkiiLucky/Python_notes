#循环结构

#while循环

#例1：求1+2+3+...+100的值
s=0
i=1
while i<=100:
    s=s+i
    i=i+1
print("1到100的和为：",s)
#例1另解
s=0
i=100
while i>=0:
    s=s+i
    i=i-1
print("1到100的和为：",s)
#例2：有一个阶梯，如果每步跨2阶，最后余1阶，如果每步跨3阶，最后余2阶，如果每步跨5阶，最后余4阶，如果每步跨2阶，最后余1阶，如果每步跨6阶，最后余5阶，如果每步跨7阶，正好达到阶梯顶，问阶梯至少多少阶？
n=0
while True:
    if n%2==1 and n%3==2 and n%5==4 and n%2==1 and n%6==5 and n%7==0 :
       break
    else:
        n=n+1
print("该阶梯至少有{}阶".format(n))
#例3：输入某人英文名字的字母
name="Tom"
x=0
while x<len(name):
    print("第"+str(x+1)+"个字母："+name[x])#name[0]=='T',name[1]=='o',name[2]=='m'
    x=x+1
else:
    print("---拼写结束---")
#例4：某一个应用程序中，注册用户信息时，要求密码是字母和数字的组合，如果输入密码不符合要求，则要求重新输入密码。编写程序实现此功能
string=input("请输入新密码:")
i=0
while i<len(string):
    if not string[i].isalnum():
        msg="密码只能是字母和数字的组合，请重新输入！"
        break
    i+=1
else:
    msg="密码输入成功！"
print(msg)

#for循环
'''for 循环变量 in 遍历结构：
       循环体语句块'''

#例1：计算1-2+3-4+5-6+...+n
n=eval(input("请输入1-2+3-4+5-6+...+n中的n的值:"))
s=0
for x in range(1,n+1):#range(1,n+1)代表[1, 2, 3, 4,...,n]  range()函数常用于for循环结构中
    s=s+pow(-1,x+1)*x
print("1-2+3-4+5-6+...+"+str(n)+"的值为"+str(s))
#例2:输入一串字符，统计空格，数字，字母和其他字符的个数
string=input("请输入要统计的字符串（回车结束）：")
space_n,digit_n,letter_n,other_n=0,0,0,0
for i in range(len(string)):
    if string[i].isspace():
        space_n+=1
    elif string[i].isdigit():
        digit_n+=1
    elif string[i].isalpha():
        letter_n+=1
    else:
        other_n+=1
print('空格的个数是：',space_n)
print('数字的个数是：',digit_n)
print('字母的个数是：',letter_n)
print('其他字母的个数是：',other_n)

#break语句和continue语句

for s in "我是谁":
    if s == "是":
        break      #break代表结束此次循环，不再继续
    print(s)       #结果为"我"
    
for s in "我是谁":
    if s == "是":
        continue   #continue是结束当前这次循环，跳过字符"是"，继续后面的遍历
    print(s,end="")#结果为"我谁"
print()
    
#循环的嵌套

#例1:打印九九乘法表
for i in range(1,10):
    for j in range(1,10):
        print("{0}*{1}={2:<2}".format(i,j,i*j),end=" ")
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print("{0}*{1}={2:<2}".format(i,j,i*j),end=" ")
    print()

for i in range(1,10):
    for j in range(1,i+1):
        print("{0}*{1}={2:<2}".format(j,i,i*j),end=" ")
    print()
#例2：输出2到100之间所有的素数
print("2到100之间所有的素数:",end="")
for x in range(2,101):
    y=2
    while y <= x-1:
        if  x % y == 0:
            break
        y+=1
    else:
        print(x,end=" ")    

    
    


    







