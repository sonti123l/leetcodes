class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(len(nums)-1):
            for num1 in range(num+1,len(nums)):
                combined_value = int(nums[num]) + int(nums[num1])
                if combined_value == target:
                    return [num,num1]