import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;
import java.util.Arrays;


public class Solution {
    public static void main(String[] args) throws IOException {
        Scanner input= new Scanner(System.in);

       int[][] arr =new int[6][6];
       for(int i=0;i<6;i++){
           
           for(int j=0;j<6;j++){
               arr[i][j]=input.nextInt();
           }
       }
       int max=-9*9;
       for(int i=0;i<4;i++){
           for(int j=0;j<4;j++){
               
               int sum=0;
               sum=arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+
               arr[i+2][j+1]+arr[i+2][j+2];
               if(sum>max){
                   max=sum;
               }
           }
           
       }
       System.out.print(max);

        
       
       
        input.close();
    }
}
