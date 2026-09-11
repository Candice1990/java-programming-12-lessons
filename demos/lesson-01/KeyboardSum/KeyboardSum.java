import java.util.Scanner;
public class KeyboardSum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter two integers:");
        int first = input.nextInt();
        int second = input.nextInt();
        System.out.println("Sum: " + (first + second));
    }
}
