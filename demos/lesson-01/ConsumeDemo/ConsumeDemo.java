import java.util.Scanner;
public class ConsumeDemo {
    public static void main(String[] args) {
        Scanner input = new Scanner("hello 20");
        System.out.println(input.hasNextInt()); // false: sees hello
        System.out.println(input.hasNextInt()); // false: still sees hello
        System.out.println(input.next());       // hello: read past it
        System.out.println(input.nextInt());    // 20: now read the integer
        input.close();
    }
}
