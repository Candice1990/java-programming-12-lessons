import java.util.Locale;
import java.util.Scanner;
public class ReadName {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in).useLocale(Locale.ROOT);
        System.out.println("Enter a full name:");
        String name = input.nextLine();
        System.out.println("Enter age, height, and enrolled (true/false):");
        int age = input.nextInt();
        double height = input.nextDouble();
        boolean enrolled = input.nextBoolean();
        System.out.println(name + " | " + age + " | " + height + " | " + enrolled);
    }
}
