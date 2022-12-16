import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int d1,d2,m1,m2,y1,y2,d,m,y;
        Scanner input=new Scanner(System.in);
     

                d1=input.nextInt();
                m1=input.nextInt();
                y1=input.nextInt();


                d2=input.nextInt();
                m2=input.nextInt();
                y2=input.nextInt();

             d=d1-d2;
             m=m1-m2;
             y=y1-y2;
             if(y<0){
                 System.out.print("0");
             }
            
            else if(d<=0 && m<=0 && y<=0){
                System.out.print("0");
            }
            else if(d>0 && m==0 && y==0){
                System.out.print(d*15);
            }
            else{
                if(m>0 && y==0){
                    System.out.print(500*m);
                }
                else{
                    System.out.print(10000);
                }
                
            }
            input.close();

        
    }
}