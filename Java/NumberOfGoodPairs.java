// Nested for loop to check each value and comapre for equality to next values in the array if it matches increment good pair
// in other words if the element in nums[i] equal to the element in nums[j] increment goodPair (count)





class Solution {
    public int numIdenticalPairs(int[] nums) {
        int goodPairs = 0;
        
        for(int i =0; i < nums.length; i++) {
            for(int j = 0; j < nums.length; j++) {
                if (nums[i] == nums[j] && i < j) {
                    goodPairs++;
                }
            }
        }
        return goodPairs;
    }
}
