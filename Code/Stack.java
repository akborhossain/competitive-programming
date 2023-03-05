
import java.util.Scanner;

public class Stack {

    static int top = -1, capacity = 20;
    static int[] a = new int[capacity];

    static void push(int n) {
        if (top == capacity - 1) {
            System.out.println("Overflow");
        }
        top++;
        a[top] = n;

    }

    static int pop() {
        if (top <= 0) {
            return -1;
        }
        int r = a[top];
        top--;
        return r;

    }

    static int peek() {
        return a[top];
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println(pop());

        push(10);
        push(11);
        push(12);
        push(13);
        push(14);
        push(15);
        push(16);
        push(17);
        System.out.println(pop());
        System.out.println(peek());

    }

}
