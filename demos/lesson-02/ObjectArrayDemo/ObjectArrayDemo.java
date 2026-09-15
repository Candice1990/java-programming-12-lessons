class Subject {
    private final String id, name;
    private int maxMarks, marks;
    public Subject(String id, String name, int maxMarks) {
        this.id = id; this.name = name;
        setMaxMarks(maxMarks);
    }
    public String getId() { return id; }
    public String getName() { return name; }
    public int getMaxMarks() { return maxMarks; }
    public int getMarks() { return marks; }
    public void setMaxMarks(int value) {
        maxMarks = Math.max(1, value);
        marks = Math.min(marks, maxMarks);
    }
    public void setMarks(int value) { marks = Math.max(0, Math.min(value, maxMarks)); }
    public boolean isQualified() { return marks >= maxMarks * 0.4; }
    @Override
    public String toString() { return id + " " + name + ": " + marks; }
}
class Student {
    private final String rollNo, name;
    private String department;
    private Subject[] subjects = new Subject[0];
    public Student(String rollNo, String name, String department) {
        this.rollNo = rollNo; this.name = name; this.department = department;
    }
    public String getRollNo() { return rollNo; }
    public String getName() { return name; }
    public String getDepartment() { return department; }
    public void setDepartment(String value) { department = value; }
    public Subject[] getSubjects() { return subjects; }
    public void setSubjects(Subject... subjects) { this.subjects = subjects; }
}
public class ObjectArrayDemo {
    public static void main(String[] args) {
        Subject[] subjects = new Subject[2];
        System.out.println(subjects[0] == null); // true
        subjects[0] = new Subject("S01", "Java", 100);
        subjects[1] = new Subject("S02", "Databases", 100);
        subjects[0].setMarks(80);
        subjects[1].setMarks(35);
        Student student = new Student("ST01", "Ada", "Computing");
        student.setSubjects(subjects[0], subjects[1]);
        for (Subject subject : student.getSubjects()) {
            System.out.println(subject); // S01 Java: 80, then S02 Databases: 35
        }
        System.out.println(subjects[0].isQualified()); // true
        System.out.println(subjects[1].isQualified()); // false
    }
}
