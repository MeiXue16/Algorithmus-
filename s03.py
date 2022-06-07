class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        rep = 0
        set1 = set()  #创建一个空集合，set中不能有重复元素
        for i in nums:
            if i in set1:
                return i 
            set1.add(i)   #把元素加进集合
        return 0
