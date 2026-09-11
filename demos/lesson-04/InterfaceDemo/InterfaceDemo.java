public class InterfaceDemo {
    interface Printable { void print(); }
    interface Named { String name(); }
    static class Report implements Printable, Named {
        @Override public String name() { return "Results"; }
        @Override public void print() { System.out.println(name()); }
    }
    public static void main(String[] args) {
        Printable document = new Report();
        document.print();
    }
}
