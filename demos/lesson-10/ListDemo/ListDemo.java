import java.util.ArrayList;
import java.util.List;
public class ListDemo {
    public static void main(String[] args) {
        List<Integer> values = new ArrayList<>();
        values.add(1); values.add(2); values.add(1);
        values.remove(1);
        System.out.println(values);
        values.remove(Integer.valueOf(1));
        System.out.println(values);
        values.set(0, 9);
        System.out.println(values.get(0));
    }
}
