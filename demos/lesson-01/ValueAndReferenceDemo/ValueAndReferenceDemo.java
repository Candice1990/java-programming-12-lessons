public class ValueAndReferenceDemo {
    public static void main(String[] args) {
        int count = 2;
        int copy = count;
        copy = 9;
        int[] values = {10, 20};
        int[] alias = values;
        alias[0] = 99;
        System.out.println("copy = " + copy);
        System.out.println("count = " + count);
        System.out.println("values[0] = " + values[0]);
        System.out.println("same array = " + (values == alias));
    }
}
