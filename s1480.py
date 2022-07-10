class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        temp= 0
        for i in range(len(nums)):
            nums[i] += temp
            temp = nums[i]
        return nums
