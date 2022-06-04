class MinStack(object):

    def __init__(self):
        self.stack =[]
        self.minstack =[float('inf')]
        #准备两个栈
        """
        initialize your data structure here.
        """


    def push(self, x):
        self.stack.append(x)
        self.minstack.append(min(x, self.minstack[-1]))
        #存放min的栈：每次加入的值与栈顶的值比较，例如3，-2，那么栈顶加入-2
        """
        :type x: int
        :rtype: None
        """


    def pop(self):
        self.stack.pop()
        self.minstack.pop()
        #栈顶推出一个值，min栈跟着推出一个值
        """
        :rtype: None
        """


    def top(self):
        return self.stack[-1]        
        """
        :rtype: int
        """


    def min(self):
        return self.minstack[-1]
              
        """
        :rtype: int
        """



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
