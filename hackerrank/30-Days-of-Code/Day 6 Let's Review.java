import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan= new Scanner(System.in);
        int t;
        
        t=scan.nextInt();
        scan.nextLine();
        for(int i=0;i<t;i++){
            String s;
            s=scan.nextLine();
            char ch []= s.toCharArray();
            for(int j=0;j<s.length();j++){
                System.out.print(ch[j]);
                j++;
                
            }
            System.out.print(" ");
            for(int j=1;j<s.length();j++){
                System.out.print(ch[j]);
                j++;
                
            }
            System.out.println();
            
        }
        scan.close();
    }
}
