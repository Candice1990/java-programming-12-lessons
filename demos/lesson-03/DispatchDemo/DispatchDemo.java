class Animal {
    public void speak() { System.out.println("Animal sound"); }
}
class Dog extends Animal {
    @Override
    public void speak() { System.out.println("Woof"); }
}
class Cat extends Animal {
    @Override
    public void speak() { System.out.println("Meow"); }
}
public class DispatchDemo {
    public static void main(String[] args) {
        Animal pet = new Dog();
        pet.speak(); // Woof

        Animal[] animals = {new Dog(), new Cat()};
        for (Animal animal : animals) {
            animal.speak(); // Woof, then Meow
        }
    }
}
