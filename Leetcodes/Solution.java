public class Solution {
    public int majorityElement(int[] nums) {
        int count = 0;
        for(int i =0;i<nums.length;i++){
            int value = 0;
            int target = nums[i];
            for(int j=i;j<nums.length;j++){
                if(target == nums[j]){
                    value += 1;
                }
                count = value;
            }
            if(count>nums.length/2){
                return nums[i];
            }
        }
        return 1;
    }
} {
    
}
