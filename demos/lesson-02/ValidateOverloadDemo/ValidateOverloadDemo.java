public class ValidateOverloadDemo {
    static boolean validate(String name) {
        return name != null && !name.isEmpty();
    }
    static boolean validate(int age) {
        return age >= 3 && age <= 15;
    }
    public static void main(String[] args) {
        System.out.println(validate("Ada"));          // true
        System.out.println(validate(""));             // false
        System.out.println(validate(10));             // true
        System.out.println(validate(20));             // false
    }
}
