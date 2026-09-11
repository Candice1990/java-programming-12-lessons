public class LambdaDemo {
    @FunctionalInterface interface IntOperation { int apply(int value); }
    static int evaluate(int value, IntOperation operation) {
        return operation.apply(value);
    }
    public static void main(String[] args) {
        int factor = 3;
        IntOperation multiply = value -> value * factor;
        IntOperation absolute = Math::abs;
        System.out.println(evaluate(7, multiply));
        System.out.println(evaluate(-4, absolute));
    }
}
