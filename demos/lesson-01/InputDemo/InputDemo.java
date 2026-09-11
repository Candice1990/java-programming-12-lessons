import java.util.Scanner;
public class InputDemo {
    public static void main(String[] args) {
        try (Scanner input = new Scanner("20\nAda Lovelace\n")) {
            System.out.println("Check 1: " + input.hasNextInt());
            System.out.println("Check 2: " + input.hasNextInt());
            int age = input.nextInt();
            String remainder = input.nextLine();
            String name = input.nextLine();
            System.out.println("Age: " + age);
            System.out.println("Line remainder: [" + remainder + "]");
            System.out.println("Name: " + name);
        }
    }
}
