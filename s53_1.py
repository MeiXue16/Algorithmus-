class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(para):                   #定义一个二分函数
            left,right =0, len(nums)-1  
            while left<=right:
                mid =(left+ right) //2 
                if nums[mid]< para:    #注意函数内参数是tar
                    left = mid +1
                else: 
                    right =mid-1
            return left
        return bs(target+1)-bs(target)
