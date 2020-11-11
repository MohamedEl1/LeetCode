/**
 Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

0 <= i < j < k < arr.length
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
Where |x| denotes the absolute value of x


How to approach:
1. just follow the condition above and write it in code. To find the absolute value we used Math.abs()
2. I have j = i + 1 and k = j + 1 because in the question it says i < j < k
*/



class Solution {
    public int countGoodTriplets(int[] arr, int a, int b, int c) {
        
        
        int count = 0;
        for(int i = 0; i < arr.length; i++) {
            for(int j = i+1; j < arr.length; j++) {
                // for little optimisation we check if the condition statifies then continue to loop if it does
                if(Math.abs(arr[j] - arr[i])  <= a) {
                for(int k = j+1; k < arr.length; k++) {
                       if( Math.abs(arr[k] - arr[j]) <= b && Math.abs(arr[k] - arr[i]) <=c) {
                         
                              count++;
                
                    }  
                }
                 
            }
                
                
                
            
        }
        }
        
        return count;
    }
}