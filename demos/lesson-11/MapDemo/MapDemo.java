import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;
public class MapDemo {
    public static void main(String[] args) {
        Map<Integer, String> insertion = new LinkedHashMap<>();
        insertion.put(3, "Grace"); insertion.put(1, "Ada");
        insertion.put(3, "Grace Hopper");
        System.out.println(insertion);
        Map<Integer, String> sorted = new TreeMap<>(insertion);
        for (Map.Entry<Integer, String> entry : sorted.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }
    }
}
