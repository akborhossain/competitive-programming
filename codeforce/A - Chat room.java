import java.util.Scanner;

public class ChatRoom {

    @SuppressWarnings("empty-statement")
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String ch = input.next();
        char[] s = ch.toCharArray();
        String h = "hello";
        char[] s1 = h.toCharArray();
        int i = 0, count = 0;
        for (char c : s) {
            if (s1[i] == c && count <= 5 && i<5) {
                count++;
                i++;
            }
            if(count==5)
                break;

        }
        if (count == 5) {
            System.out.print("YES");
        } else {
            System.out.print("NO");
        }

    }

}
