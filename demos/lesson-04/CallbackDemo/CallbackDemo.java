public class CallbackDemo {
    interface ClickListener { void onClick(); }
    static class Button {
        private final ClickListener listener;
        Button(ClickListener listener) { this.listener = listener; }
        void click() { listener.onClick(); }
    }
    public static void main(String[] args) {
        String message = "Saved"; // effectively final
        Button button = new Button(new ClickListener() {
            @Override public void onClick() { System.out.println(message); }
        });
        button.click();
    }
}
