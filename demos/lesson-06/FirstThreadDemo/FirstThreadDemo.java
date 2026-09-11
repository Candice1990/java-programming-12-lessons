public class FirstThreadDemo {
    static class Task implements Runnable {
        @Override public void run() {
            System.out.println("Running on " + Thread.currentThread().getName());
        }
    }
    static class NamedThread extends Thread {
        NamedThread() { super("subclass-worker"); }
        @Override public void run() { System.out.println("Thread subclass ran"); }
    }
    public static void main(String[] args) throws InterruptedException {
        Task task = new Task();
        task.run();
        Thread worker = new Thread(task, "worker");
        worker.start();
        worker.join();
        Thread second = new NamedThread();
        second.start();
        second.join();
    }
}
