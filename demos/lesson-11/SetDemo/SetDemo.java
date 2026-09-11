import java.util.HashSet;
import java.util.Set;
public class SetDemo {
    static class Student {
        private final int id;
        private final String name;
        Student(int id, String name) { this.id = id; this.name = name; }
        @Override public boolean equals(Object other) {
            if (this == other) return true;
            if (!(other instanceof Student)) return false;
            Student student = (Student) other;
            return id == student.id;
        }
        @Override public int hashCode() { return Integer.hashCode(id); }
    }
    public static void main(String[] args) {
        Set<Student> students = new HashSet<>();
        System.out.println(students.add(new Student(7, "Ada")));
        System.out.println(students.add(new Student(7, "Ada updated")));
        System.out.println(students.size());
    }
}
