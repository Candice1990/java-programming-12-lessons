import java.util.ArrayDeque;
import java.util.Deque;
import java.util.PriorityQueue;
import java.util.Queue;
public class QueueDemo {
    public static void main(String[] args) {
        Deque<String> tasks = new ArrayDeque<>();
        tasks.addLast("first"); tasks.addLast("second");
        System.out.println(tasks.removeFirst());
        tasks.push("urgent");
        System.out.println(tasks.pop());
        Queue<Integer> priority = new PriorityQueue<>();
        priority.offer(30); priority.offer(10); priority.offer(20);
        while (!priority.isEmpty()) System.out.println(priority.poll());
    }
}
