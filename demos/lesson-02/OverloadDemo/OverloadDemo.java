public class OverloadDemo {
    static int max(int x, int y) {
        if (x > y) return x;
        return y;
    }
    static float max(float x, float y) {
        if (x > y) return x;
        return y;
    }
    static int max(int x, int y, int z) {
        return max(max(x, y), z);
    }
    public static void main(String[] args) {
        System.out.println(max(10, 15));      // 15
        System.out.println(max(5.5f, 7.5f));  // 7.5
        System.out.println(max(8, 10, 3));    // 10
    }
}
