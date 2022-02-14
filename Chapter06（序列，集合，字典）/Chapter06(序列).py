  #列表
#从列表添加元素
member = ['北京','天津','上海','重庆']
member.append('广州')
print(member)#['北京', '天津', '上海', '重庆', '广州']
member.extend(['山东','河南'])
print(member)#['北京', '天津', '上海', '重庆', '广州', '山东', '河南']
member.insert(0,'河北')
print(member)#['河北', '北京', '天津', '上海', '重庆', '广州', '山东', '河南']

#改变列表中元素的位置
member = ['北京','天津','上海','重庆']
print(member[0])
print(member[1])
a = member[0]
member[0] = member[1]
member[1] = a   #将列表中第一个和第二个元素位置互换
print(member)#['天津', '北京', '上海', '重庆']

#从列表删除元素
member = ['北京','天津','上海','重庆']
member.remove('北京')
print(member)#['天津', '上海', '重庆']
member = ['北京','天津','上海','重庆']
del member[1]
print(member)#['北京', '上海', '重庆']
member = ['北京','天津','上海','重庆']
del member   #将整个列表删除
member = ['北京','天津','上海','重庆']
print(member.pop())#删除列表中最后一个元素，并返回最后一个元素的值
print(member)

#列表分片
member = ['北京','天津','上海','重庆']
print(member [1:3])#['天津', '上海']
print(member[1:])  #['天津', '上海', '重庆']
print(member[:3])  #['北京', '天津', '上海']
print(member[:])   #['北京', '天津', '上海', '重庆']

#列表操作符
list1 = [123,456]
list2 = [456,789]
print(list1 * 3)    #[123, 456, 123, 456, 123, 456]
print(list1 > list2)#False
print(123 in list1) #True
print(456 not in list2)#False
list3 = list1 +list2
print(list3)#[123, 456, 456, 789]
list4 = [123,456]
print((list2 > list1) and (list1 == list4))#True
list5 = [123,['北京',789],456]
print('北京' in list5)   #False
print('北京' in list5[1])#True
print(list5[1][0])#'北京'
list4 *= 5
print(list4)#[123, 456, 123, 456, 123, 456, 123, 456, 123, 456]
print(list4.count(123))#5  索引123在list4中的个数
print(list4.index(123))#0  索引123的位置
print(list4.index(123,1,3))#2  索引123在位置1与位置3之间的位置
list6 = [3,1,5,2,8,11,32,25]
list6.reverse()#将列表中所有元素的位置顺序颠倒
print(list6)   #[25, 32, 11, 8, 2, 5, 1, 3]
list6.sort()   #将列表中的元素从小到大排序
print(list6)   #[1, 2, 3, 5, 8, 11, 25, 32]
list6.sort(reverse = True)#将列表中的元素从大到小排序)
print(list6)   #[32, 25, 11, 8, 5, 3, 2, 1]


#元组
tuple1 = (1,2,3,4,5,6,7,8)
print(tuple1[1])#2)
print(tuple1[4:])#(5, 6, 7, 8)
print(tuple1[:4])#(1, 2, 3, 4)
tuple2 = tuple1[:]
print(tuple2)#(1, 2, 3, 4, 5, 6, 7, 8)
print(8 * (8))#64
print(8 * (8,))#(8, 8, 8, 8, 8, 8, 8, 8)
tuple3 = 1,2,3
print(type(tuple3))#<class 'tuple'>

#元组的增删
tuple1 = ('北京','天津','上海','重庆')
tuple1 = tuple1[:2] + ('广州',) + tuple1[2:]
print(tuple1)   #('北京', '天津', '广州', '上海', '重庆')
del tuple1

#元组操作符（+ * < > == and or not）

#字符串内置函数
str1 = 'peter'
print(str1.capitalize())#首字母大写
str2 = 'PYTHon'
print(str2.casefold())#python     将字符串中所有字符小写
print(str2.swapcase())#pythON     将字符串中大小写反转
str3 = 'python'
print(str3.center(20))#将字符串居中，并用空格填充至长度20的新字符串
str4 = 'DAXIExiaoxie'
print(str4.count('xi'))#2  索引 'xi'在 str4 中的个数
print(str4.endswith('ie'))#True  检验 str4 是否以 'ie' 结尾
str5 = 'how\tare\tyou'
print(str5.expandtabs(4))#how are you   #将tab(\t)转换为空格
print(str5.find('a'))#4   查找 'a' 在str5中的位置,若'a'不在str5中，则返回—1
print(str5.index('a'))#4  查找 'a' 在str5中的位置,若'a'不在str5中，则出现报错
str6 = 'python'
print(str6.join('12345'))#1python2python3python4python5
print(str6.partition('th'))#('py', 'th', 'on') 将str6分为3个元组
print(str6.replace('pyt','PYT'))#PYThon
str7 = 'he is a silly boy'
print(str7.split())#['he', 'is', 'a', 'silly', 'boy']   以空格为分格符切片字符串
print(str7.split('i'))#['he ', 's a s', 'lly boy']      以'i'为分隔符切片字符串
str8 = 'ssssaaaassss'
print(str8.translate(str.maketrans('s','b')))#bbbbaaaabbbb  将str8中的's'替换成'b'

#list()函数：将一个可迭代对象转换为列表
a = 'shdaj ajajn'
print(list(a))#['s', 'h', 'd', 'a', 'j', ' ', 'a', 'j', 'a', 'j', 'n']
b = (1,1,2,3,21,35)
print(list(b))#[1, 1, 2, 3, 21, 35]

#tuple()函数：将一个可迭代对象转换为元组
a = 'shdaj ajajn'
print(tuple(a))
b = [1, 1, 2, 3, 21, 35]#('s', 'h', 'd', 'a', 'j', ' ', 'a', 'j', 'a', 'j', 'n')
print(tuple(b))#(1, 1, 2, 3, 21, 35)

#str()函数
a = 250
print(str(a))#将对象转换为字符串

numbers = [1,7,3,5,8,15,-6]
print(max(numbers))#返回集合或序列中的最大值
print(min(numbers))#返回集合或序列中的最小值
print(sum(numbers))#33  将集合或序列中的所有数据相加，注意其中所有数据的数据类型要相同
print(sum(numbers,10))#43 将集合或序列中的所有数据相加,再加上10
print(sorted(numbers))#[-6, 1, 3, 5, 7, 8, 15]将序列从小到大排列
print(list(reversed(numbers)))#[-6, 15, 8, 5, 3, 7, 1]将序列从大到小排列
print(list(enumerate(numbers)))#[(0, 1), (1, 7), (2, 3), (3, 5), (4, 8), (5, 15), (6, -6)]
a = [1,2,3,4,5,6,7,8]
b = ['北京','天津','上海','重庆']
print(list(zip(a,b)))#[(1, '北京'), (2, '天津'), (3, '上海'), (4, '重庆')]







