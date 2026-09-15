class Rectangle {
    private double length, breadth;
    public Rectangle() { this(1, 1); }
    public Rectangle(double side) { this(side, side); }
    public Rectangle(double length, double breadth) {
        this.length = Math.max(0, length);
        this.breadth = Math.max(0, breadth);
    }
    public double area() { return length * breadth; }
}
public class ConstructorDemo {
    public static void main(String[] args) {
        System.out.println(new Rectangle().area());     // 1.0
        System.out.println(new Rectangle(4).area());    // 16.0
        System.out.println(new Rectangle(4, 3).area());  // 12.0
        System.out.println(new Rectangle(-4, 3).area()); // 0.0
    }
}
