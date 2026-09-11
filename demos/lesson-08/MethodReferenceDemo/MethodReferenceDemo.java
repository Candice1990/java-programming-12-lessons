public class MethodReferenceDemo {
    interface TextLength { int apply(String text); }
    interface Message { void send(String text); }
    interface BuilderFactory { StringBuilder create(); }
    public static void main(String[] args) {
        TextLength length = String::length;
        Message print = System.out::println;
        BuilderFactory factory = StringBuilder::new;
        print.send("Length: " + length.apply("Java"));
        System.out.println(factory.create().append("Ready"));
    }
}
