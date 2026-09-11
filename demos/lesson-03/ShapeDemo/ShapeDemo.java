abstract class Shape {
    private final String label;
    Shape(String label) { this.label = label; }
    abstract double area();
    void describe() {
        System.out.printf(java.util.Locale.ROOT, "%s: %.2f%n", label, area());
    }
}

class Rectangle extends Shape {
    private final double width, height;
    Rectangle(double width, double height) {
        super("Rectangle"); this.width = width; this.height = height;
    }
    @Override double area() { return width * height; }
}

class Circle extends Shape {
    private final double radius;
    Circle(double radius) { super("Circle"); this.radius = radius; }
    @Override double area() { return Math.PI * radius * radius; }
}

public class ShapeDemo {
    public static void main(String[] args) {
        Shape[] shapes = {new Rectangle(3, 4), new Circle(2)};
        for (Shape shape : shapes) shape.describe();
    }
}
