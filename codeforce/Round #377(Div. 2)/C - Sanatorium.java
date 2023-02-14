import java.util.Scanner;
 
public class Sanatorium {
 
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        long bf = in.nextLong(), di = in.nextLong(), su = in.nextLong(), max = 0, count = 0;
        if (bf >= di && bf >= su) {
            max = bf;
 
        } else if (di >= bf && di >= su) {
            max = di;
        } else {
            max = su;
        }
        if (max - 1 > bf) {
            count += (max - 1 - bf);
        }
        if (max - 1 > di) {
            count += (max - 1 - di);
        }
        if (max - 1 > su) {
            count += (max - 1 - su);
        }
        System.out.println(count);
  
    }
 
}
