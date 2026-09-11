class Student {
    private final String name;
    Student(String name) { this.name = name; }
    String name() { return name; }
}

public class ObjectArrayDemo {
    public static void main(String[] args) {
        Student[] students = new Student[2];
        System.out.println(students[0] == null);
        students[0] = new Student("Ada");
        students[1] = new Student("Grace");
        for (Student student : students) System.out.println(student.name());
    }
}
