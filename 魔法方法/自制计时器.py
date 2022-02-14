#计时器

import time

class MyTimer:
    
    def __init__(self):
        self.starttime = []
        self.stoptime = []
        self.time = [0,0,0,0,0,0,0,0,0]
        self.period = 0
        self.prompt = ('提示：请先调用start() 开始计时！！') #提示字符

    def start(self):
        self.starttime = list(time.localtime())
        self.prompt = ('提示，请先调用stop() 停止计时！')
        print("计时开始...")
        
    def stop(self):
        if self.starttime == []:
            print("提示：请先调用start() 开始计时！")
        else:
            self.stoptime = list(time.localtime())
            print("计时结束！")

            for i in range(len(self.starttime)):
                self.time[i] = self.stoptime[i] - self.starttime[i]
                
            self.period = self.time[3]*60*60 + self.time[4]*60 + self.time[5]
        
        
    def __str__(self):
        if self.stoptime == []:
            return self.prompt
        else:
            return ('程序总共运行了{}秒'.format(self.period))

    def __repr__(self):
       if self.stoptime == []:
            return self.prompt
       else:
            return ('程序总共运行了{}秒'.format(self.period))


    def __add__(self,other):
        self.period = self.period + other.period
        return ('程序总共运行了{}秒'.format(self.period))

                      
