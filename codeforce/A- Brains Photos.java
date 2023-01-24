import java.util.Scanner;

public class BrainsPhotos {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n, m;
        n = input.nextInt();
        m = input.nextInt();
        String[][] ch = new String[n][m];
        boolean color = false;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                ch[i][j] = input.next();
                if (ch[i][j].equals("C") || ch[i][j].equals("Y") || ch[i][j].equals("M")) {
                    color = true;
                }
            }

        }

        if (color) {
            System.out.print("#Color");
        } else {
            System.out.println("#Black&White");
        }
    }

}
