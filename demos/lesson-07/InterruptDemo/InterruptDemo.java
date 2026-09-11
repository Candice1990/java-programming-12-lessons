public class InterruptDemo {
    static class Sleeper implements Runnable {
        @Override public void run() {
            try {
                Thread.sleep(10000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.out.println("Cancellation acknowledged");
            }
        }
    }
    public static void main(String[] args) throws InterruptedException {
        Thread worker = new Thread(new Sleeper());
        worker.start();
        worker.interrupt();
        worker.join();
        System.out.println("Terminated: " + !worker.isAlive());
    }
}
