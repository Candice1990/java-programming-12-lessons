public class PropagationDemo {
    static int parse(String text) { return Integer.parseInt(text); }
    static int doubled(String text) { return 2 * parse(text); }
    public static void main(String[] args) {
        try {
            System.out.println(doubled("bad"));
            System.out.println("not reached");
        } catch (NumberFormatException e) {
            System.out.println("The input is not an integer");
        }
        System.out.println("Finished");
    }
}
