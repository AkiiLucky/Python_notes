#冒泡排序
a = [5,3,9,1,7,6]
print('原始列表是：',a)
n = len(a)
for i in range(0,n-1):
    for j in range(0,n-1-i):
        if a[j] > a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
print("从小到大排序后的结果为：",a)




