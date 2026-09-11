public class SlotDemo {
    static class Slot {
        private int value;
        private boolean full;
        synchronized void put(int next) throws InterruptedException {
            while (full) wait();
            value = next;
            full = true;
            notifyAll();
        }
        synchronized int take() throws InterruptedException {
            while (!full) wait();
            int result = value;
            full = false;
            notifyAll();
            return result;
        }
    }
    public static void main(String[] args) throws InterruptedException {
        Slot slot = new Slot();
        Thread producer = new Thread(new Runnable() {
            public void run() {
                try { for (int i = 1; i <= 3; i++) slot.put(i); }
                catch (InterruptedException e) { Thread.currentThread().interrupt(); }
            }
        });
        Thread consumer = new Thread(new Runnable() {
            public void run() {
                try { for (int i = 1; i <= 3; i++) System.out.println(slot.take()); }
                catch (InterruptedException e) { Thread.currentThread().interrupt(); }
            }
        });
        producer.start(); consumer.start();
        producer.join(); consumer.join();
    }
}
