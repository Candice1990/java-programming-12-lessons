import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class StringScanner {
    public static void main(String[] args) throws FileNotFoundException {
        try (Scanner text = new Scanner("10 20")) {
            System.out.println("String sum: " + (text.nextInt() + text.nextInt()));
        }
        try (Scanner file = new Scanner(new File("numbers.txt"))) {
            System.out.println("File sum: " + (file.nextInt() + file.nextInt()));
        }
    }
}
