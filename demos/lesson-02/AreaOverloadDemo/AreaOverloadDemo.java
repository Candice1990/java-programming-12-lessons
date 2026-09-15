public class AreaOverloadDemo {
    static double area(double radius) {
        return Math.PI * radius * radius;
    }
    static double area(double length, double breadth) {
        return length * breadth;
    }
    static double area(double a, double b, double height) {
        return (a + b) * height / 2;
    }
    public static void main(String[] args) {
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", area(2)); // 12.57
        System.out.println(area(4, 3));       // 12.0: rectangle
        System.out.println(area(4, 6, 3));    // 15.0: trapezium
    }
}
