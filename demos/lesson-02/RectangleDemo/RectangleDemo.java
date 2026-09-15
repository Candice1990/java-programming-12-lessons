class Rectangle {
    public double length, breadth;
    public double area() { return length * breadth; }
    public double perimeter() { return 2 * (length + breadth); }
    public boolean isSquare() { return length == breadth; }
}
public class RectangleDemo {
    public static void main(String[] args) {
        Rectangle r = new Rectangle();
        r.length = 4;
        r.breadth = 3;
        System.out.println(r.area());      // 12.0
        System.out.println(r.perimeter()); // 14.0
        System.out.println(r.isSquare());  // false
    }
}
