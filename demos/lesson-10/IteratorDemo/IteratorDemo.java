import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
public class IteratorDemo {
    public static void main(String[] args) {
        List<Integer> scores = new ArrayList<>();
        scores.add(40); scores.add(80); scores.add(55);
        Iterator<Integer> iterator = scores.iterator();
        while (iterator.hasNext()) {
            int score = iterator.next();
            if (score < 50) iterator.remove();
        }
        System.out.println(scores);
    }
}
