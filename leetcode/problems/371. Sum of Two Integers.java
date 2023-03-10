class Solution {
    public int getSum(int a, int b) {
        int tem;
        while(b!=0){

            tem= (a&b)<<1;
            a=a^b;
            b=tem;
        }
        return a;  
    }
}