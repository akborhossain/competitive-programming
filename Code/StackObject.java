
import java.util.Scanner;

public class Stack {

    private int top = -1, capacity;
    private int[] a;

    public Stack(int capacity) {
        this.capacity = capacity;
        a = new int[capacity];
    }

    void push(int n) {
        if (top == capacity - 1) {
            System.out.println("Overflow");
        } else {
            top++;
            a[top] = n;
        }

    }

    int pop() {
        if (top <= 0) {
            return -1;
        }
        int r = a[top];
        top--;
        return r;

    }

    int peek() {
        return a[top];
    }

    void show() {
        for (int i = 0; i <= top; i++) {
            System.out.print(a[i]+" ");
        }
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        Stack s = new Stack(n);
        System.out.println(s.pop());

        s.push(10);
        s.push(11);
        s.push(12);
        s.push(13);
        s.push(14);
        s.push(15);
        s.push(16);
        s.push(17);
        s.show();
        System.out.println(s.pop());
        System.out.println(s.peek());
        s.show();

    }

}
