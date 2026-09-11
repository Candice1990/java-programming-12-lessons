class Circle {
    double radius;
    double area() { return Math.PI * radius * radius; }
}

public class ObjectDemo {
    public static void main(String[] args) {
        Circle first = new Circle();
        first.radius = 2;
        Circle alias = first;
        alias.radius = 3;
        System.out.println(first.radius);
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", first.area());
    }
}
