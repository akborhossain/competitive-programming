package com.mycompany.mavenproject1;

import java.util.Arrays;

public class BubbleSort {

    public static void main(String[] args) {
        int[] arr = new int[]{2, 5, 1, 9, 3, 10, 8, 2};
        
        int n = arr.length;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - i-1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int tem = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = tem;
                }

            }
            

        }
        System.out.print(Arrays.toString(arr));
    }

}
