class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)
        nums = sorted(nums1)  
        if(len(nums)%2==0):
            first_value = (len(nums)//2)-1
            second_value = ((len(nums)//2)+1)-1
            median = (nums[first_value]+nums[second_value])/2
            return median
        else:
            median =nums[((len(nums)+1)//2)-1]
            return float(median)       