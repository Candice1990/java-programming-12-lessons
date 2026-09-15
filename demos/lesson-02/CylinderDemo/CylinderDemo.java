class Cylinder {
    public double radius, height;
    public double lidArea() { return Math.PI * radius * radius; }
    public double circumference() { return 2 * Math.PI * radius; }
    public double surfaceArea() { return 2 * lidArea() + circumference() * height; }
    public double volume() { return lidArea() * height; }
}
public class CylinderDemo {
    public static void main(String[] args) {
        Cylinder c = new Cylinder();
        c.radius = 2;
        c.height = 3;
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", c.lidArea());     // 12.57
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", c.surfaceArea()); // 62.83
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", c.volume());      // 37.70
    }
}
