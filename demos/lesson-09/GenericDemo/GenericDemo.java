public class GenericDemo {
    static class Box<T> {
        private final T value;
        Box(T value) { this.value = value; }
        T get() { return value; }
    }
    static <T> T echo(T value) { return value; }
    static <T extends Number> double twice(T value) {
        return value.doubleValue() * 2;
    }
    public static void main(String[] args) {
        Box<String> text = new Box<>("Java");
        System.out.println(text.get().toUpperCase());
        System.out.println(echo(42));
        System.out.println(twice(3));
        System.out.println(text.getClass() == new Box<Integer>(1).getClass());
    }
}
