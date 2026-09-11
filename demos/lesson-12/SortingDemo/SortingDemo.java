import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
public class SortingDemo {
    static class Student {
        private final String name;
        private final int score;
        Student(String name, int score) { this.name = name; this.score = score; }
        String name() { return name; }
        int score() { return score; }
        @Override public String toString() { return name + ":" + score; }
    }
    public static void main(String[] args) {
        int[] numbers = {3, 1, 2};
        Arrays.sort(numbers);
        System.out.println(Arrays.toString(numbers));
        List<String> names = new ArrayList<>(Arrays.asList("Grace", "Ada"));
        Collections.sort(names);
        System.out.println(names);
        List<Student> students = new ArrayList<>();
        students.add(new Student("Grace", 90));
        students.add(new Student("Ada", 90));
        students.add(new Student("Linus", 80));
        students.sort(Comparator.comparingInt(Student::score).reversed()
                                .thenComparing(Student::name));
        System.out.println(students);
    }
}
