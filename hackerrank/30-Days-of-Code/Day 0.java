import java.util.Scanner;

public class HalloWorld {
    public static void main(String[] args) {
            Scanner input= new Scanner(System.in);
            String inputString;
            
            inputString = input.nextLine();
            System.out.println("Hallo, World.");
            System.out.println(inputString);
    }