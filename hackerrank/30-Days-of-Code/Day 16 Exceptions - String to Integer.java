import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        String S = bufferedReader.readLine();
        
        try {
            int i=Integer.parseInt(S);
            System.out.println(i);
        }
        catch(Exception e) {
            System.out.println("Bad String");

    }

        bufferedReader.close();
    }
}
