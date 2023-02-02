import java.util.Scanner;

public class Password {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int k, n;
        n = input.nextInt();
        k = input.nextInt();
        String[] s = new String[n + 1];
        for (int i = 0; i <= n; i++) {
            s[i] = input.next();
        }
        int len = s[n].length(),less=0,geter=0;
        for (int i = 0; i <= n; i++) {
            if (len < s[i].length()) {
                geter++;
            }
            if(len>s[i].length()){
                less++;
            }
        }
        int best=((less/k)*5)+less+1;
        int worst=(((n-geter-1)/k)*5)+(n-geter);
        System.out.print(best+" "+worst);

    }

}
