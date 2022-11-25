import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());
        char [] binary =Integer.toBinaryString(n).toCharArray();
        int result=0,count=0;
        for(int i=0;i<binary.length;i++){
            if(binary[i]=='0'){
                count=0;
            }
            else{
                count++;
                if(result<count){
                    result=count;
                }
            }
        }
        System.out.print(result);

        bufferedReader.close();
    }
}
