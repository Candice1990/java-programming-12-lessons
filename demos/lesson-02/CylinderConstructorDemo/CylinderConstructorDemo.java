class Cylinder {
    private double radius, height;
    public Cylinder() { this(0, 0); }
    public Cylinder(double radius) { this(radius, 1); }
    public Cylinder(double radius, double height) {
        setRadius(radius); setHeight(height);
    }
    public double getRadius() { return radius; }
    public double getHeight() { return height; }
    public void setRadius(double value) { radius = Math.max(0, value); }
    public void setHeight(double value) { height = Math.max(0, value); }
    public double volume() { return Math.PI * radius * radius * height; }
}
public class CylinderConstructorDemo {
    public static void main(String[] args) {
        Cylinder c = new Cylinder(2, 3);
        System.out.println(new Cylinder().getHeight());  // 0.0
        System.out.println(new Cylinder(2).getHeight()); // 1.0
        System.out.println(c.getRadius());               // 2.0
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", c.volume()); // 37.70
    }
}
