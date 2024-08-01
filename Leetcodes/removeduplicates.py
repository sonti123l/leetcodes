class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_duplicate = []
        for i in range(0,len(nums)):
            if i<len(nums)-1:
                if nums[i] == nums[i+1]:
                    nums_duplicate.append(nums[i])
                    nums.remove(nums[i]) 
        for i in nums_duplicate:
            count = 0                                               
            for j in nums:
                if i==j:
                    count += 1    
            if count>1:
                nums.remove(i)
        return len(nums)                                                      
        