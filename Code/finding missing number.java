
package com.mycompany.mavenproject1;

public class MissingNumber {
    public static void main(String[] args) {
        
      int arr[]=new int[]{1,2,3,4,6,7,8,9,10};
      
      int sum=(10*11)/2;
      
      int actualsum=0;
      for(int i=0;i<arr.length;i++){
          actualsum+=arr[i];
      }
      if((sum-actualsum)>0)
      System.out.print("The missing number is :"+(sum-actualsum));
      else
          System.out.print("There is no missing number");
    }
    
    
}
