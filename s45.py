class Solution:
    def minNumber(self, nums: List[int]) -> str:
        #使用快速排序
        strnum =[str(i) for i in nums]

        def quick_sort(left, right):
            if left >= right : return
            i, j= left, right
            while i < j:
                while strnum[j] + strnum[left] >= strnum[left] + strnum[j] and i<j:
                    j -= 1  #从后往前找比基准strnum[left]小的数
                while strnum[i] + strnum[left] <= strnum[left] + strnum[i] and i<j:
                    i += 1  #从前往后找比基准strnum[left]大的数
                #交换这两个数,所以现在strnum[i]比基准小，strnum[j]比基准大
                strnum[i], strnum[j] =strnum[j], strnum[i] 
            #交换strnum[i]和基准的值   
            strnum[i], strnum[left] = strnum[left], strnum[i] 
            quick_sort(left , i-1) #再对i之前的数组进行快速排序
            quick_sort(i+1, right) #再对i之后的数组进行快速排序, 不能写i,否则i>=right的判断可能会超出递归范围

        quick_sort(0, len(nums)-1)
        return ''.join(strnum)


