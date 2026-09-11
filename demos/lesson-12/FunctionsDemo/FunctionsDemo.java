import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;
public class FunctionsDemo {
    public static void main(String[] args) {
        Predicate<String> nonBlank = text -> !text.isBlank();
        Function<String, String> normalize = text -> text.trim().toUpperCase(java.util.Locale.ROOT);
        Consumer<String> display = System.out::println;
        Supplier<String> fallback = () -> "UNKNOWN";
        String value = " Ada ";
        display.accept(nonBlank.test(value) ? normalize.apply(value) : fallback.get());
        display.accept(fallback.get());
    }
}
