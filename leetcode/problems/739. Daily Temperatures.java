class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n= temperatures.length;
        int [] result= new int[n];
        int i,j,count;
        for( i=0;i<n-1;i++){
             j=i+1;
             count=0;
            while(j<n){
                if(temperatures[i]<temperatures[j]){
                    count++;
                    result[i]=count;
                    count=0;
                    break;
                }
                else if(i>0 && temperatures[i]==temperatures[i-1]){
                    if(result[i-1]==0){
                        result[i]=0;
                    }
                    else{
                        result[i]=result[i-1]-1;
                    }

                    break;
                }
                else{
                    count++;
                }

                j++;               
            }
            if(count!=0)
            result[i]=0;
            }
            
        result[n-1]=0;
        return result;
        
    }
}