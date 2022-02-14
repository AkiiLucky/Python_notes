#鲨鱼吃小鱼小游戏
import random as r

class Shark:

    HP=100
    
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def movex(self,direction):
        if direction == 1:
            self.x += 1
            self.HP -= 1
        if direction == 0:
            self.x -= 1
            self.HP -= 1
            
        if self.x > 10:
            self.x = 10 - (self.x - 10)
        if self.x < 0:
            self.x = 10 - (self.x + 10)
    
            
    def movey(self,direction):
        if direction == 1:
            self.y += 1
            self.HP -= 1       
        if direction == 0:
            self.y -= 1
            self.HP -= 1
            
        if self.y > 10:
            self.y = 10 - (self.y - 10)
        if self.y < 0:
            self.y = 10 - (self.y + 10)

    def HPlook(self):
        print("当前的HP为：",self.HP)

    def place(self):
        print("鲨鱼当前的位置为：({},{})".format(self.x,self.y))


class Fish:

    
    def __init__(self):
        self.x = r.randint(0,10)
        self.y = r.randint(0,10)

    def movex(self,direction):
        if direction == 1:
            self.x += 1
        if direction == 0:
            self.x -= 1
            
        if self.x > 10:
            self.x = 10 - (self.x - 10)
        if self.x < 0:
            self.x = 10 - (self.x + 10)
    def movey(self,direction):
        if direction == 1:
            self.y += 1      
        if direction == 0:
            self.y -= 1
            
        if self.y > 10:
            self.y = 10 - (self.y - 10)
        if self.y < 0:
            self.y = 10 - (self.y + 10)
            
    def place(self):
        print("小鱼当前的位置为：({},{})".format(self.x,self.y))


class Autofish(Fish):
    def automovex(self):
        self.x = self.x + r.choice([-1,0,1])
        if self.x > 10:
            self.x = 10 - (self.x - 10)
        if self.x < 0:
            self.x = 10 - (self.x + 10)
    def automovey(self):
        self.y = self.y + r.choice([-1,0,1])
        if self.y > 10:
            self.y = 10 - (self.y - 10)
        if self.y < 0:
            self.y = 10 - (self.y + 10)

    def place(self):
        print("自动鱼当前的位置为：({},{})".format(self.x,self.y))
        
class Yellowfish(Fish):
    def __init__(self):
        Fish.__init__(self)#继承父类中默认的（__init__）属性和方法，并且对其增加
        self.color = 'yellow'

    def place(self):
        print("小黄鱼当前的位置为：({},{})".format(self.x,self.y))
        
class Goldfish(Fish):
    def __init__(self):
        super().__init__()
        self.color = 'gold'

    def place(self):
        print("小金鱼当前的位置为：({},{})".format(self.x,self.y))


#创造实例对象        
shark = Shark()
fishlist = []
for fish in range(2):
    fish = Fish()
    fishlist.append(fish)
goldfish = Goldfish()
fishlist.append(goldfish)
yellowfish = Yellowfish()
fishlist.append(yellowfish) 
autofish = Autofish()
fishlist.append(autofish)    


def eat():
    i = 0
    while i < len(fishlist):
        if (shark.x,shark.y)==(fishlist[i].x,fishlist[i].y):
            shark.HP += 20
            fishlist.remove(fishlist[i])
            print("吃掉一只小鱼，HP+20")
            break
        i += 1
            
    else:
        shark.HP -= 5
        print("什么也没吃到T_T，HP-5")
            
    if shark.HP <= 0:
        print("游戏失败！你被饿死了！")
    if len(fishlist) == 0:
        print("游戏胜利！所有鱼都被你吃光了！")

def move(direction,times=1): #times指次数
    if direction == '右':
        for i in range(times):
            shark.movex(1)
        print("向右移动{}格，当前的位置为：({},{})".format(str(times),shark.x,shark.y))
    if direction == '左':
        for i in range(times):
            shark.movex(0)
        print("向左移动{}格，当前的位置为：({},{})".format(str(times),shark.x,shark.y))
    if direction == '上':
        for i in range(times):
            shark.movey(1)
        print("向上移动{}格，当前的位置为：({},{})".format(str(times),shark.x,shark.y))
    if direction == '下':
        for i in range(times):
            shark.movey(0)
        print("向下移动{}格，当前的位置为：({},{})".format(str(times),shark.x,shark.y))
        
    autofish.automovex()
    autofish.automovey()
    
    if shark.HP <= 0:
        print("游戏失败！你被饿死了！")

    

        
    
    
#测试
print("游戏规则：")
print("1.现在是一条鲨鱼，你需要把池塘里的所有小鱼吃掉才能获得游戏胜利。")
print("2.你的初始血量为100，每移动一步血量减1。每吃掉一只鱼，血量加20。")
print("3.池塘的大小是10*10的方格，你和小鱼的初始位置是随机的，一旦碰到墙壁会按原方向弹回。")
print('''4.移动：move(direction,times)；direction代表移动的方向，可取"上","下","左","右"；times代表移动的步数,一次可以移动任意步，如果不填默认是一步。''')
print("5.吃：eat()，注意没有吃到小鱼的话，血量会减少哦！")
print("7.查看自己的当前的血量：shark.HPlook()")
print("8.查看自己的当前的位置：shark.place()")
print("9.池塘里有一只自动鱼，你每移动一次，它也会跟着移动，你需要靠你的智慧来抓住它！")
print("10.让我们愉快的开始吧！")
print()

shark.place()
for n in range(len(fishlist)):
    fishlist[n].place()


        


        
