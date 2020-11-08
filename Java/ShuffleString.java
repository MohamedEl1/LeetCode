/**
 LeetCode Problem #1528

 Given a string s and an integer array indices of the same length.
 The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Explanation:
// check if value i equal to a value in the indices if it does then grab indices index number and use it for shuffling the string from beginning (smallest to largest)

Big O Run Time Complexity: O(n^2) (Can be optimised)
 */

class Solution {
    public String restoreString(String s, int[] indices) {
        
         String suffledString = "";
        for(int i = 0; i < indices.length; i++) {
            for (int j = 0; j < indices.length; j++) {

                // check if value i equal to a value in the indices if it does then grab its                        index number and use it for shuffling the string from beginning
                if (i==indices[j]) {
                    suffledString += s.charAt(j);
                }
            }
          

        }
        return suffledString;
}
}