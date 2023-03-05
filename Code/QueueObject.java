package com.mycompany.mavenproject1;

import java.util.Arrays;
import java.util.Scanner;

public class Queue {

    private int capacity;
    private int total = 0, f = -1, r = -1;
    int[] a;

    Queue(int capacity) {
        this.capacity = capacity;
        a = new int[capacity];
    }

    public void push(int n) {
        if (capacity == total) {
            System.out.println("Queue is full");
        }
        r = (r + 1) % capacity;
        a[r] = n;
        total++;

    }

    public int pop() {
        if (total == 0) {
            return -1;
        }
        total--;
        f = (f + 1) % capacity;
        System.out.println(f);
        return a[f];

    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        int n = in.nextInt();
        Queue q = new Queue(n);
        q.push(10);
        System.out.println(Arrays.toString(q.a));
        System.out.println(q.pop());
        System.out.println(q.pop());
        

    }

}
