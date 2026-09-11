import java.util.ArrayList;
import java.util.List;
public class WildcardDemo {
    static double sum(List<? extends Number> values) {
        double total = 0;
        for (Number value : values) total += value.doubleValue();
        return total;
    }
    static void addDefaults(List<? super Integer> values) {
        values.add(0); values.add(1);
    }
    public static void main(String[] args) {
        List<Integer> ints = new ArrayList<>();
        ints.add(10); ints.add(20);
        List<Number> numbers = new ArrayList<>();
        addDefaults(numbers);
        System.out.println(sum(ints));
        System.out.println(numbers);
    }
}
