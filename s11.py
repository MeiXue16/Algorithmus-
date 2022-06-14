class Solution:
    def minArray(self, numbers: List[int]) -> int:
        i, j =0 ,len(numbers)-1
        while i < j:
            m = (i+j)//2             #分为左数组（升序），右数组（降序）
            if numbers[m] <numbers[j]:
                j =m
            elif numbers[m] >numbers[j]:
                i =m+1
            else: j =j-1
        return numbers[i]
