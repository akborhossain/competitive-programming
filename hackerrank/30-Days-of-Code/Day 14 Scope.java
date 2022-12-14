import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


class Difference {
  	private int[] elements;
  	public int maximumDifference;
    
    public Difference(int[] a)
    {
        this.elements=a;
    }
    void computeDifference(){
        int n=elements.length;
        for(int i=0;i<n;i++){
            for(int j=i+1;j<n;j++){
                int sum= Math.abs(elements[i]-elements[j]);
                if(sum>maximumDifference){
                    maximumDifference=sum;
                }
            }
        }
    }

} // End of Difference class

public class Solution {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        sc.close();

        Difference difference = new Difference(a);

        difference.computeDifference();

        System.out.print(difference.maximumDifference);
    }
}