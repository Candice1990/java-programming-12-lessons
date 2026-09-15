class Circle {
    public double radius;
    public double area() { return Math.PI * radius * radius; }
    public double perimeter() { return 2 * Math.PI * radius; }
    public double circumference() { return perimeter(); }
}
public class CircleDemo {
    public static void main(String[] args) {
        Circle first = new Circle();
        Circle second = new Circle();
        first.radius = 2;
        second.radius = 5;
        Circle alias = first;
        alias.radius = 3;
        System.out.println(first.radius);  // 3.0: same object as alias
        System.out.println(second.radius); // 5.0: separate object
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", first.area()); // 28.27
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", first.circumference()); // 18.85
    }
}
