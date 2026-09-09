class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap <>();
        
        for(int i = 0 ; i < nums.length ; i++){
            int lookup = target - nums[i];
            if (map.containsKey(lookup)){
                int l[] = {
                    i,
                    map.get(lookup)
                };return l;
            
            };
            map.put(nums[i],i);
        };
    return new int[]{-1,-1};
    }
}