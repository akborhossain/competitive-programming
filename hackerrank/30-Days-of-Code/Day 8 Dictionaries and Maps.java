//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

class Solution{
    public static void main(String []argh){
        Scanner in = new Scanner(System.in);
        Map<String ,Integer> PhoneBook=new HashMap<String, Integer>();

        int n = in.nextInt();
        for(int i = 0; i < n; i++){
            String name = in.next();
            int phone = in.nextInt();
            // Write code here
            PhoneBook.put(name, phone);
        }
        while(in.hasNext()){
            String s = in.next();
            // Write code here
            Integer number=PhoneBook.get(s);
            System.out.println(
                (number != null) 
                ? s + "=" + number 
                : "Not found"
            );
                
            
        }
        in.close();
    }
}