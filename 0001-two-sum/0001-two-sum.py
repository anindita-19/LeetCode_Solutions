class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        d={}
        for j in range(len(nums)):
            if target-nums[j] in d:
                return [j,d[target-nums[j]]]
            d[nums[j]]=j       
             
            