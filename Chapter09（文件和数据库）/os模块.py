#os(operrating system操作系统)模块
import os
print(os.getcwd())#E:\软件\Python\python save\Chapter09（文件和数据库）        获取当前工作的目录路径
os.chdir('E:\\')
print(os.getcwd())#E:\
print(os.listdir('E:\\'))#列举指定目录下的所有文件和目录名
os.mkdir('E:\\A')#创建单个目录path,当此文件存在时会报错
os.mkdir('E:\\A\\B')
os.makedirs('E:\\C\\D')#递归创建多层目录
#os.remove('E:\\ABC.txt') 删除文件
os.rmdir('E:\\A\\B')#将单级目录删除，如果非空会报错
os.removedirs('E:\\C\\D')#多级目录删除，如果非空会报错
os.rename('E:\\A','123')#重命名

os.system('cmd')#打开系统cmd窗口
os.system('calc')#打开计算器



#os.path模块



