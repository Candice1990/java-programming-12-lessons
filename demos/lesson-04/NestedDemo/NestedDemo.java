public class NestedDemo {
    private final String name;
    NestedDemo(String name) { this.name = name; }
    class Member { String read() { return name; } }
    static class Helper { String read() { return "no implicit outer"; } }
    public static void main(String[] args) {
        NestedDemo outer = new NestedDemo("classroom");
        Member member = outer.new Member();
        Helper helper = new Helper();
        System.out.println(member.read());
        System.out.println(helper.read());
    }
}
