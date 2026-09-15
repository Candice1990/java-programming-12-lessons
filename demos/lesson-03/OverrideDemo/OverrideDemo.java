class Animal {
    public void speak() { System.out.println("Animal sound"); }
}
class Dog extends Animal {
    @Override
    public void speak() { System.out.println("Woof"); }
}
public class OverrideDemo {
    public static void main(String[] args) {
        Animal animal = new Animal();
        Dog dog = new Dog();
        animal.speak(); // Animal sound
        dog.speak();    // Woof
    }
}
