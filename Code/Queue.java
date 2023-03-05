
import java.util.Arrays;
import java.util.Scanner;

public class Queue {

    static int capacity = 10;
    static int total = 0, f = 0, r = -1;
    static int[] a = new int[capacity];

    public static void push(int n) {
        if (capacity == total) {
            System.out.println("Queue is full");
        }
        r = (r + 1) % capacity;
        a[r] = n;
        total++;

    }

    public static int pop() {
        if (total == 0) {
            return -1;
        }
        total--;
        f = (f + 1) % capacity;
        return a[f];

    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        push(n);
        System.out.println(Arrays.toString(a));
        System.out.println(pop());
        pop();

    }

}
