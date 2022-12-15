import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. */
        Scanner input=new Scanner(System.in);
        int t;
        t=input.nextInt();
        for(int i=0;i<t;i++){
            if(isPrime(input.nextInt())){
                System.out.println("Prime");
            }
            else{
                System.out.println("Not prime");
            }
        }
        input.close();
        
    }
    public static boolean isPrime(int n){
        if(n<2)
        return false;
        else if(n<4)
        return true;
        else{
            boolean prime=true;
            for(int i=2;i<=Math.sqrt(n);i++){
                if(n%i==0)
                prime=false;
            }
            return prime;
        }
    }
}



