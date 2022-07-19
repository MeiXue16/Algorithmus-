class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i , j = 0, len(nums)-1
        while i< j:
            if nums[i]%2 ==0 and nums[j]%2 ==1:
                nums[i], nums[j]= nums[j], nums[i]
                i+=1
                j-=1
            if nums[i]%2 ==1 : i+=1
            if nums[j]%2 ==0 : j-=1
        return nums
      
 #method 2
class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i , j = 0, len(nums)-1
        while i< j:
            while i<j and nums[i]%2 ==1:
                i+=1
            while i<j and nums[j]%2 ==0 : 
                j-=1
            nums[i], nums[j]= nums[j], nums[i]
        return nums
