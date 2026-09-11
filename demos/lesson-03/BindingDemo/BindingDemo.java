class Animal { }

class Dog extends Animal { }

public class BindingDemo {
    static String identify(Animal a) { return "Animal overload"; }
    static String identify(Dog d) { return "Dog overload"; }
    public static void main(String[] args) {
        Animal pet = new Dog();
        System.out.println(identify(pet));
        System.out.println(identify(new Dog()));
    }
}
