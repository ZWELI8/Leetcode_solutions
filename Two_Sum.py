class Solution:
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = target
        p=0
        for i in range(len(self.nums)):
            for j in range(1,len(self.nums)):
                if(self.nums[i]+self.nums[j] == target and i!=j):
                    return i,j


p=Solution()
x= [2,5,5,11]
print(p.twoSum(x,10))