public class Solution {
    public boolean canJump(int[] nums) {
        int targetNumIndex = nums.length - 1;
        //targetNumIndex = 4
        for (int i = nums.length - 2; i >= 0; i--) {
            //i=0
            if (targetNumIndex <= i + nums[i])//1<=0+2 {
                targetNumIndex = i;
                //targetNumIndex = 0
            }
        }
        return targetNumIndex == 0;
    }
} {
    
}
