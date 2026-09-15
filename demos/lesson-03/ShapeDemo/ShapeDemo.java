abstract class Shape {
    public abstract double area();
    public void describe() {
        System.out.printf(java.util.Locale.ROOT, "Area: %.2f%n", area());
    }
}
class Rectangle extends Shape {
    private double width, height;
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    @Override
    public double area() { return width * height; }
}
class Circle extends Shape {
    private double radius;
    public Circle(double radius) { this.radius = radius; }
    @Override
    public double area() { return Math.PI * radius * radius; }
}
public class ShapeDemo {
    public static void main(String[] args) {
        Shape[] shapes = {new Rectangle(3, 4), new Circle(2)};
        for (Shape shape : shapes) {
            shape.describe(); // Area: 12.00, then Area: 12.57
        }
    }
}
