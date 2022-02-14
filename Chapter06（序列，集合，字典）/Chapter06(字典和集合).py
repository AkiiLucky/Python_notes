#字典
#创建字典
dict1 = {'四川':'成都','河南':'郑州','湖北':'武汉','湖南':'长沙'}
print(dict1['四川'])#成都
print(dict1['河南'])#郑州
print(dict1['湖北'])#武汉
print(dict1['湖南'])#长沙

dict2 = {1:'one',2:'two',3:'three'}
print(dict2[1])#one
print(dict2[2])#two
print(dict2[3])#three

dict3 = {}#空字典
print(dict3)

#另一种创建字典的方法
dict3 = dict((('F',70),('i',105),('s',115),('h',104),('C',67)))
print(dict3)#{'F': 70, 'i': 105, 's': 115, 'h': 104, 'C': 67}

dict4 = dict(一='one',二='two',四川='成都')
print(dict4)#{'一': 'one', '二': 'two', '四川': '成都'}

#改变字典内的键的值
dict1 = {'四川':'成都','河南':'郑州','湖北':'武汉','湖南':'长沙'}
dict1['四川'] = '绵阳'
print(dict1)#{'四川': '绵阳', '河南': '郑州', '湖北': '武汉', '湖南': '长沙'}

dict1 = {'四川':'成都','河南':'郑州','湖北':'武汉','湖南':'长沙'}
dict1['中国'] = '北京'
print(dict1)#{'四川': '成都', '河南': '郑州', '湖北': '武汉', '湖南': '长沙', '中国': '北京'}

#fromkeys
dict1 = {}
print(dict1.fromkeys((1,2,3),'number'))#{1: 'number', 2: 'number', 3: 'number'}
print(dict1)#{}
print(dict1.fromkeys((1,3),'数字'))#{1: '数字', 3: '数字'}

#keys, values, items
dict1 = dict1.fromkeys(range(10),'赞')
for eachkeys in dict1.keys():
    print(eachkeys,end=' ')#0 1 2 3 4 5 6 7 8 9
print()
for eachvalues in dict1.values():
    print(eachvalues,end=' ')#赞 赞 赞 赞 赞 赞 赞 赞 赞 赞
print()
for eachitems in dict1.items():
    print(eachitems,end=' ')#(0, '赞') (1, '赞') (2, '赞') (3, '赞') (4, '赞') (5, '赞') (6, '赞') (7, '赞') (8, '赞') (9, '赞')
print()
print(dict1.get(10))#None    print(dict1[10])会报错
print(dict1.get(10,'木有哦！'))#木有哦！
print(dict1.get(9,'木有哦！'))#赞
print(10 in dict1)#False
print(9  in dict1)#True
dict1.clear()#把字典清空
print(dict1)#{}

a = {1:'one',2:'two',3:'three'}
b = a.copy()#浅拷贝
c = a
print(id(a))#1877873746560
print(id(b))#1877864679936
print(id(c))#1877873746560
a[4] = 'two'
print(a)#{1: 'one', 2: 'two', 3: 'three', 4: 'two'}
print(b)#{1: 'one', 2: 'two', 3: 'three'}
print(c)#{1: 'one', 2: 'two', 3: 'three', 4: 'two'}
print(a.pop(2))#根据键把对应项移除，并且返回对应的值
print(a)#{1: 'one', 3: 'three', 4: 'two'}
print(a.popitem())#(4, 'two')    随机删除一项，并返回该项的值
print(a)#{1: 'one', 3: 'three'}
a.setdefault(5)
print(a)#{1: 'one', 3: 'three', 5: None}
a.setdefault(4,'four')
print(a)#{1: 'one', 3: 'three', 5: None, 4: 'four'}
b = {5:'five'}
a.update(b)#根据b更新a
print(a)#{1: 'one', 3: 'three', 5: 'five', 4: 'four'}

#集合
num1 = {1,2,7,4,5,5,1,6,3}
print(num1)#{1, 2, 3, 4, 5, 6, 7}  集合会自动删除重复的元素，并且集合具有无序性

list1 = [1,2,7,4,5,5,1,6,3]
list2 = []
for each in list1:
    if each not in list2:
        list2.append(each)
print(list2)#[1, 2, 7, 4, 5, 6, 3]  去除列表里的重复元素

list1 = [1,2,7,4,5,5,1,6,3]
list2 = []
list2 = list(set(list1))#利用set()工厂函数将列表转换为集合
print(list2)#[1, 2, 3, 4, 5, 6, 7]  去除列表里的重复元素，但是顺序被打乱

num2 = {1,2,3,4,5,6,7,8}
print(1 in num2)#True
print('1' in num2)#False
num2.add(9)
print(num2)#{1, 2, 3, 4, 5, 6, 7, 8, 9}
num2.remove(1)
print(num2)#{2, 3, 4, 5, 6, 7, 8, 9}

num3 = frozenset([1,2,3,4,5])#创建一个不可变集合

