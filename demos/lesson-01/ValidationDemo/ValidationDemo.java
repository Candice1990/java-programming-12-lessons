import java.util.Scanner;
public class ValidationDemo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter an age (0 or greater):");
        while (input.hasNext()) {
            if (!input.hasNextInt()) {
                String skipped = input.next();
                System.out.println("Not an int: " + skipped);
                continue;
            }
            int age = input.nextInt();
            if (age < 0) {
                System.out.println("Age cannot be negative: " + age);
                continue;
            }
            System.out.println("Accepted age: " + age);
            return;
        }
        System.out.println("No valid age supplied");
    }
}
