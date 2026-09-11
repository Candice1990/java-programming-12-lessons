package school.app;
import school.model.Student;
public class PackageDemo {
    public static void main(String[] args) {
        Student student = new Student("Ada");
        System.out.println(student.name());
        // student.name = "Grace"; // private: does not compile
        // student.internalLabel(); // package-private: does not compile here
    }
}
