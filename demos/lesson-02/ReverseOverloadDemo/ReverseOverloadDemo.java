import java.util.Arrays;
public class ReverseOverloadDemo {
    static int reverse(int number) {
        int result = 0;
        while (number > 0) {
            result = result * 10 + number % 10;
            number = number / 10;
        }
        return result;
    }
    static int[] reverse(int[] values) {
        int[] result = new int[values.length];
        for (int i = 0; i < values.length; i++) {
            result[i] = values[values.length - 1 - i];
        }
        return result;
    }
    public static void main(String[] args) {
        System.out.println(reverse(237)); // 732
        int[] values = {2, 3, 7};
        System.out.println(Arrays.toString(reverse(values))); // [7, 3, 2]
        System.out.println(Arrays.toString(values));          // [2, 3, 7]
    }
}
