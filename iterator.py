#可迭代对象：list/ tuple/ dict / set/ str/ range/ filter/ map
#for ... in.. 可迭代对象
import time
from collections.abc import Iterable

class Demo(object):
    def __init__(self,x):
        self.x =x
        self.count =0

    def __iter__(self):
        return self
    # __iter__方法决定了这个类是否可迭代

    def __next__(self):
        self.count += 1
        if self.count <= self.x:
            return self.count-1
        else:
            raise StopIteration #停止打印

    #每次for..in都会调用一次__next__方法，获取返回值
d= Demo(10)
print(isinstance(d, Iterable))
#isinstance：判断一个实例对象d是否有指定的类Iterable创建出来的
# for i in d: #for in 循环本质是调用可迭代对象d 的__ietr__方法， 获取到这个方法的返回值
#     #这个返回值需要是一个对象，然后再调用这个方法的__next__方法
#     print(i)

#names =['nana', 'miya']
names =list(('nana', 'miya'))
print(isinstance(names, Iterable))
# for i in Demo(10):
#     print(i)

#迭代器的使用
print(d.__iter__().__next__())
print(d.__iter__().__next__())
print(d.__iter__().__next__())
print(d.__iter__().__next__())

#等价于
#i =d.__iter__()
#print(i.__next__())
i= iter(d) #内置函数iter 可以获取到可迭代对象的迭代器
print(next(i))

class Fibonacci(object):
    def __init__(self,n):
        self.n =n
        self.num0 =0
        self.num1 =1
        self.count =0

    def __iter__(self):
        return self

    def __next__(self):
        self.count +=1
        if self.count <= self.n:
            x= self.num1
            self.num0, self.num1 =self.num1, self.num0 +self.num1
            time.sleep(0.03)
            return x
        else:
            raise StopIteration

f =Fibonacci(12)
for i in f:
    print(i)

#既然有列表了，为什么还要有生成器呢？
nums =[1, 2, 3, 4, 5,6,7,8,9] #占空间，不占时间
f =Fibonacci(12) #占时间，不占用空间
