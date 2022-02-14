#文件的打开
f = open('E:\\test01.txt',encoding='UTF-8')
print(f.read(5))#读取前五个字符
print(f.tell())#15  返回当前文件的指针位置
print(f.seek(45,0))#根据参考点设置文件的位置，参考点：0为文件开头，1为当前位置，2为文件末尾；偏移量为45字节
print(f.tell())#45
print(f.readline())#从文件指针所在行中读取前（）行字符串，默认参数为读取一行

f.seek(0,0)#先将指针定位到文本开头
lines = list(f)#先将整个文本转换为列表，然后在逐个元素（逐行）打印,但是这个方法效率不高
for each_line in lines:
    print(each_line)

f.seek(0,0)
for each_line in f:#这种方法效率高
    print(each_line)#逐行打印

f.close()#已经打开的文件要及时关闭

#写入文件
f = open('E:\\test02.txt','w')
f.write('四川大学欢迎你！！！')
f.close()

f = open('E:\\test02.txt','a')
f.write('欢迎加入我们的大家庭！！')
f.close()




