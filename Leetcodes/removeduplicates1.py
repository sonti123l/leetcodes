class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def recursion_function(nums):
            for i in range(0,len(nums)):
                if i<len(nums)-1:
                    if i == 0:
                        if nums[i] == nums[i+1]:
                            continue    
                    else:
                        if((nums[i]==nums[i-1])and(nums[i] == nums[i+1])):
                            nums.remove(nums[i]) 
                        else:
                            continue
        recursion_function(nums = nums)  
        recursion_function(nums = nums)     
        recursion_function(nums = nums)                  
        return len(nums)                    