class Student {
    public String rollNo, name, course;
    public int m1, m2, m3;
    public int total() { return m1 + m2 + m3; }
    public double average() { return total() / 3.0; }
    public char grade() {
        if (average() >= 60) return 'A';
        return 'B';
    }
}
public class StudentDemo {
    public static void main(String[] args) {
        Student student = new Student();
        student.rollNo = "S01";
        student.name = "Ada";
        student.course = "Java";
        student.m1 = 70; student.m2 = 80; student.m3 = 90;
        System.out.println(student.total());   // 240
        System.out.println(student.average()); // 80.0
        System.out.println(student.grade());   // A
    }
}
