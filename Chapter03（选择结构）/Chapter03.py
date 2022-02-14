#选择结构----{单分支，双分支（例1，例2），多分支（例3）}
#例1：如果分数达到1000则闯关成功，如果没达到1000则闯关失败
point=eval(input("本关卡的得分为："))
if point>=1000:
   point=0            #这两行是同一个语句块，缩进要一致
   print('闯关成功')  #这两行是同一个语句块，缩进要一致
else:
   print('闯关失败')  #这个语句块也要缩进
print("本关卡结束")
#例1的简化表达
point=eval(input("本关卡的得分为："))
print('闯关成功' if point>=1000 else '闯关失败')
print("本关卡结束")
#例2：已知某书店图书均九折销售，一次购书100元以上（包括100元）打八折。根据输入的购书金额计算并输出应付款。
x=eval(input("请输入购书金额："))
if x>=100:
   y=x*0.8
else:
   y=x*0.9
print("优惠后应付金额是{0:.1f}".format(y))
#例3：根据学生成绩给出相应评价
mark=eval(input("请输入您的成绩："))
if  mark>=90:
    grade='优'
elif mark>=80:
    grade='良'
elif mark>=70:
    grade='中'
elif mark>=60:
    grade='及格'
else:
    grade='不及格'
print("此学生的评价是：",grade)
#选择结构的嵌套
#例4：输入平面坐标系里某个点的坐标值（x,y)，判定输出该点在第几象限。
import random
x=random.randint(-100,100)
y=random.randint(-100,100)
print("随机生成的坐标点为：",x,",",y,end="\n")
if  x==0 or y==0:
    print("该点在坐标轴上，不在任何象限")
elif  x>0:
    if  y>0:
        print("该点在第一象限")
    else:
        print("该点在第四象限")
else:
    if  y<0:
        print("该点在第三象限")
    else:
        print("该点在第二象限")
print("判断完成！")


    





