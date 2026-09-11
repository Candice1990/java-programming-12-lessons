class Animal { String speak() { return "sound"; } }

class Dog extends Animal {
    @Override String speak() { return "woof"; }
}

public class DispatchDemo {
    static void show(Animal animal) { System.out.println(animal.speak()); }
    public static void main(String[] args) {
        Animal pet = new Dog();
        show(pet);
        show(new Animal());
    }
}
