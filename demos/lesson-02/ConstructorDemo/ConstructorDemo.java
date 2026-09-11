class Person {
    private final String name;
    Person(String name) {
        this.name = name;
        System.out.println("Person constructor");
    }
    String name() { return name; }
}

class Student extends Person {
    private final int id;
    Student(String name, int id) {
        super(name);
        this.id = id;
        System.out.println("Student constructor");
    }
    String describe() { return name() + " #" + id; }
}

public class ConstructorDemo {
    public static void main(String[] args) {
        System.out.println(new Student("Ada", 7).describe());
    }
}
