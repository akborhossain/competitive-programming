package com.mycompany.mavenproject1;

import java.util.Arrays;

public class InsertionSort {

    public static void main(String[] args) {
        int[] arr = new int[]{2, 5, 1, 9, 3, 10, 8, 2};
        int n = arr.length;
        int j = 0;
        for (int i = 1; i < n; i++) {
            int tem = arr[i];
            j = i - 1;
            for(; j >=0; j--) {
                if (arr[j]>tem) {
                    
                    arr[j+1] = arr[j];
                }
                else
                    break;

            }
            arr[j + 1] = tem;
      
        }
        System.out.print(Arrays.toString(arr));
    }

}
