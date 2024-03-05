class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        sum=arr[0]
        subsum=0
        for num in arr:
            if subsum<0:
                subsum=0
            subsum+=num
            sum=max(sum,subsum)
        return sum