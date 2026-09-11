public class CounterDemo {
    static class Counter {
        private int value;
        synchronized void increment() { value++; }
        synchronized int value() { return value; }
    }
    static class Task implements Runnable {
        private final Counter counter;
        Task(Counter counter) { this.counter = counter; }
        @Override public void run() {
            for (int i = 0; i < 10000; i++) counter.increment();
        }
    }
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        ThreadGroup group = new ThreadGroup("counters");
        Thread[] workers = new Thread[4];
        for (int i = 0; i < workers.length; i++) {
            workers[i] = new Thread(group, new Task(counter), "worker-" + i);
        }
        for (Thread worker : workers) worker.start();
        for (Thread worker : workers) worker.join();
        System.out.println(counter.value());
    }
}
