
import java.util.LinkedList;
import java.util.Scanner;

public class JapaneseCrossword {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int count = 0;
        LinkedList<Integer> out = new LinkedList<>();

        char[] ch = new char[n];
        String s = input.next();
        ch = s.toCharArray();

        for (int i = 0; i < n; i++) {
            if (ch[i] == 'B') {
                count++;
            }
            if (ch[i] == 'W' && count != 0) {
                out.add(count);
                count = 0;

            }
        }
        if (count != 0) {
            out.add(count);
        }
        if (out.isEmpty()) {
            System.out.println(0);
        }

        if (!out.isEmpty()) {
            System.out.println(out.size());
            for (int x : out) {
                System.out.print(x + " ");
            }

        }

    }

}
