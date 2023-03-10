class Solution {
    public int missingNumber(int[] nums) {
        int n=nums.length;
        n=(n*(n+1))/2;
        for(int x:nums){
            n-=x;         
        }
        return n;
        
    }
}