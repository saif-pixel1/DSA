class Solution {
    public int[] sortedSquares(int[] nums) {
        int l = 0; 
        int r = nums.length - 1;
        int i = nums.length - 1;
        int[] res = new int[nums.length];

        while(l<=r){
            if(nums[l]*nums[l] > nums[r]*nums[r]){
                res[i] = nums[l]*nums[l];
                l+=1;
            }
            else{
                res[i] = nums[r]*nums[r];
                r-=1;
            }
        i-=1;

        }

    return res;
    }
}