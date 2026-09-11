import java.io.IOException;
import java.nio.file.Path;
import java.util.Scanner;
public class FileScannerDemo {
    public static void main(String[] args) {
        int total = 0;
        try (Scanner input = new Scanner(Path.of("scores.txt"))) {
            while (input.hasNext()) {
                if (input.hasNextInt()) total += input.nextInt();
                else System.out.println("Skipped: " + input.next());
            }
            System.out.println("Total: " + total);
        } catch (IOException e) {
            System.err.println("Cannot read scores.txt: " + e.getMessage());
        }
    }
}
