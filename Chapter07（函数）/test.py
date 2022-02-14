def hanoi(n,x,y,z):
    if n==1:
        print(x,'-->',z)

    else:
        hanoi(n-1,x,z,y)
        print(x,'-->',z)
        hanoi(n-1,y,x,z)

n = eval(input("请输入汉诺塔的层数："))
hanoi(n,1,2,3)#1,2,3代表3根柱子，n代表第1根柱子上初始的圆盘数

