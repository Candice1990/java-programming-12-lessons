import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;
public class StreamDemo {
    public static void main(String[] args) {
        List<Integer> scores = List.of(85, 42, 90, 68);
        Stream<Integer> passing = scores.stream().filter(score -> {
            System.out.println("Testing " + score);
            return score >= 60;
        });
        System.out.println("Pipeline created");
        List<Integer> result = passing.sorted().toList();
        System.out.println(result);
        int total = scores.stream().mapToInt(Integer::intValue).sum();
        System.out.println("Total: " + total);
        List<String> labels = scores.stream().filter(score -> score >= 60)
            .sorted().map(score -> "Pass: " + score)
            .collect(Collectors.toCollection(ArrayList::new));
        labels.add("Report complete");
        System.out.println(labels);
    }
}
