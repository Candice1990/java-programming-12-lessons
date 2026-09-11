public class CatchDemo {
    public static void main(String[] args) {
        String[] inputs = {"12", "oops", "4"};
        for (String text : inputs) {
            try {
                int value = Integer.parseInt(text);
                System.out.println("Accepted: " + value);
            } catch (NumberFormatException e) {
                System.out.println("Rejected: " + text);
            }
        }
    }
}
