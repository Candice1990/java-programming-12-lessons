class Animal {
    public void eat() { System.out.println("Eating"); }
}
class Dog extends Animal {
    public void bark() { System.out.println("Woof"); }
}
public class InheritanceDemo {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.eat();  // Eating: inherited from Animal
        dog.bark(); // Woof: defined in Dog
    }
}
