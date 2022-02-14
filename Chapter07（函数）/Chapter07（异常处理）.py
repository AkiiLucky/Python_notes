try:
    f = open('我是个文件.txt')
    print(f.read())
    f.close()
except OSError:
    print('文件出错啦！')


try:
    f = open('我是个文件.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错啦！\n错误的原因是：' + str(reason))


try:
    sum = 1 + '1'
    f = open('我是个文件.txt')
    print(f.read())
    f.close()
except OSError as reason:
    print('文件出错啦！\n错误的原因是：' + str(reason))
except TypeError as reason:
    print('类型出错啦！\n错误的原因是：' + str(reason))


try:
    sum = 1 + '1'
    f = open('我是个文件.txt')
    print(f.read())
    f.close()
except (OSError,TypeError) as reason:
    print('出错啦！\n错误的原因是：' + str(reason))


try:
    sum = 1 + '1'
    f = open('我是个文件.txt')
    print(f.read())
    f.close()
except :
    print('出错啦！')#这种不推荐


try:
    f = open('我是个文件.txt','w')
    print(f.write('我存在了'))
    sum = 1 + '1'
except (OSError,TypeError) as reason:
    print('出错啦！\n错误的原因是：' + str(reason))
finally:#finally语句后面加的是必须要执行的，不管出没出现异常
    f.close()

    
try:
    with open('我是个文件.txt','w') as f:#利用with语句可以自动关闭已打开的文件
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错啦！\n错误的原因是：' + str(reason))


try:
    a = int(123.2)
    print(a)
except ValueError as reason:
    print('出错啦！')
else:#如果没有任何异常则运行else: 后面的语句
    print('没有任何异常')


#引发一个异常
raise ZeroDivisionError('除数为零的异常')
