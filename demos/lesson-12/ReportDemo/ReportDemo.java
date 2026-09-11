import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
public class ReportDemo {
    static class Student {
        private final String name;
        private final int score;
        Student(String name, int score) { this.name = name; this.score = score; }
        String name() { return name; }
        int score() { return score; }
    }
    public static void main(String[] args) {
        Map<Integer, Student> byId = new LinkedHashMap<>();
        byId.put(1, new Student("Ada", 92));
        byId.put(2, new Student("Grace", 85));
        byId.put(3, new Student("Linus", 45));
        List<String> report = byId.values().stream()
            .filter(student -> student.score() >= 60)
            .sorted(Comparator.comparingInt(Student::score).reversed())
            .map(student -> student.name() + " = " + student.score())
            .toList();
        report.forEach(System.out::println);
        String first = report.stream().findFirst().orElseGet(() -> "No passing students");
        System.out.println("Top: " + first);
        int sum = byId.values().stream().map(Student::score).reduce(0, Integer::sum);
        System.out.println("Total: " + sum);
    }
}
