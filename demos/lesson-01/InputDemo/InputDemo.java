import java.util.Scanner;
public class InputDemo {
    public static void main(String[] args) {
        Scanner input = new Scanner("20\nAda\n");
        int age = input.nextInt();
        String rest = input.nextLine();
        String name = input.nextLine();
        System.out.println("Age: " + age); // Age: 20
        System.out.println("Rest: [" + rest + "]"); // Rest: []
        System.out.println("Name: " + name); // Name: Ada
        input.close();
    }
}
