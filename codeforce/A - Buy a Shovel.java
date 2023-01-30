import java.util.Scanner;
 
public class BuyaShovel {
 
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
 
        int k, r, sum = 0;
        k = input.nextInt();
        r = input.nextInt();
        for (int i = 1;; i++) {
            sum += k;
            if (sum % 10 == 0 || sum % 10 == r) {
                System.out.print(i);
                break;
 
            } else {
            }
 
        }
 
    }
 
}
