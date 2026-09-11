package school.model;
public class Student {
    private final String name;
    public Student(String name) { this.name = name; }
    public String name() { return name; }
    String internalLabel() { return "internal"; }
}
