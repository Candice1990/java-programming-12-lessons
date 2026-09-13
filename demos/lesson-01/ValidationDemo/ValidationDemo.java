import java.util.Scanner;
public class ValidationDemo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter an integer:");
        if (input.hasNextInt()) {
            int number = input.nextInt();
            System.out.println("Number: " + number);
        } else {
            System.out.println("That is not an integer.");
        }
    }
}
