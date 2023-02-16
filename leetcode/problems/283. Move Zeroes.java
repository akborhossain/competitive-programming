class Solution {
    public void moveZeroes(int[] nums) {

        int n=nums.length,i=0,j=0;
        while(i<n){
            if(nums[i]!=0){
                nums[j]=nums[i];
                j++;
            }
           i++;
         
        }
        for( ; j<n; j++){
            nums[j]=0;
        }

        
        
    }
}