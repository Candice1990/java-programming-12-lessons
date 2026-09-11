import java.util.Iterator;
import java.util.NoSuchElementException;
public class IterableDemo {
    static class Range implements Iterable<Integer> {
        private final int end;
        Range(int end) { this.end = end; }
        public Iterator<Integer> iterator() {
            return new Iterator<Integer>() {
                private int next = 0;
                public boolean hasNext() { return next < end; }
                public Integer next() {
                    if (!hasNext()) throw new NoSuchElementException();
                    return next++;
                }
            };
        }
    }
    public static void main(String[] args) {
        for (int value : new Range(3)) System.out.println(value);
    }
}
