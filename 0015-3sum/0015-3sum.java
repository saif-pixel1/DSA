class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        int k = 0;
        List<List<Integer>> res = new ArrayList<>();

        while(k<nums.length-2){
            if (nums[k] > 0){
                break;
            }
            if (k > 0 && nums[k] == nums[k-1]){
                k+=1;
                continue;
            }

            int l= k+1;
            int r = nums.length-1;

            while(l<r){
                int sum = nums[l] + nums[r] + nums[k];
                if(sum==0){
                    res.add(Arrays.asList(nums[k], nums[l], nums[r]));
                    l+=1;
                    r-=1;

                    while(l<r && nums[l] ==nums[l-1]){
                        l++;
                    }
                    while(l<r && nums[r] == nums[r+1]){
                        r--;
                    }

                }
                else if(sum>0){
                    r-=1;
                }
                else{
                    l+=1;
                }
            }

        k+=1;  
        }
    return res;
    }
}