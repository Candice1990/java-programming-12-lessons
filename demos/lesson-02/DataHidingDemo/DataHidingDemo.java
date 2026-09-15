class Rectangle {
    private double length, breadth;
    public double getLength() { return length; }
    public double getBreadth() { return breadth; }
    public void setLength(double value) {
        if (value >= 0) length = value;
        else length = 0;
    }
    public void setBreadth(double value) {
        if (value >= 0) breadth = value;
        else breadth = 0;
    }
    public double area() { return length * breadth; }
}
public class DataHidingDemo {
    public static void main(String[] args) {
        Rectangle r = new Rectangle();
        r.setLength(4); r.setBreadth(3);
        System.out.println(r.area());      // 12.0
        r.setLength(-5);
        System.out.println(r.getLength()); // 0.0
        // r.length = -5; // not allowed: length is private
    }
}
