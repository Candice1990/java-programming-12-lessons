import java.util.Set;
import java.util.TreeSet;
public class NaturalOrderDemo {
    static final class Ticket implements Comparable<Ticket> {
        private final int number;
        Ticket(int number) { this.number = number; }
        public int compareTo(Ticket other) { return Integer.compare(number, other.number); }
        @Override public boolean equals(Object other) {
            return other instanceof Ticket && number == ((Ticket) other).number;
        }
        @Override public int hashCode() { return Integer.hashCode(number); }
        @Override public String toString() { return "T" + number; }
    }
    public static void main(String[] args) {
        Set<Ticket> tickets = new TreeSet<>();
        tickets.add(new Ticket(3)); tickets.add(new Ticket(1));
        tickets.add(new Ticket(3));
        System.out.println(tickets);
    }
}
