import java.util.Scanner;

public class TheBestFriendOfaMan {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt(), k = in.nextInt(), count = 0;
        int[] a = new int[n];
        int[] b = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = in.nextInt();
        }
        b[0] = a[0];
        for (int i = 1; i <n; i++) {
            if (k - a[i - 1] > a[i]) {
                b[i] = k - a[i - 1];
                count += (b[i] - a[i]);
                a[i] = k - a[i - 1];
            } else {
                b[i] = a[i];
            }

        }
        System.out.println(count);
        for (int i = 0; i < n; i++) {
            if (i == (n - 1)) {
                System.out.println(b[i]);
            } else {
                System.out.print(b[i]+" ");
            }
        }
    }
}
