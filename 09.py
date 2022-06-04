class CQueue(object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        #两个栈

    def appendTail(self, value):
        #把value压入stack1
        self.stack1.append(value) 
        """
        :type value: int
        :rtype: None
        """


    def deleteHead(self):
        #若stack2有值，直接从stack2删除
        if self.stack2:
            return self.stack2.pop()
        #若stack2为空， stack1也为空， 返回-1
        elif not self.stack1:   
            return -1
        #若stack1不为空，用循环将stack1中的值依次压入stack2, 再输出stack2顶部的值
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
            
         
        """
        :rtype: int
        """



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
