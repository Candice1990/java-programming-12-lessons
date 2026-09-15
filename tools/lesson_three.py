"""Lesson 3 follows inheritance through to abstract classes."""
def rewrite(lesson, demo):
    lesson.update(title='Inheritance, Overriding, Polymorphism & Abstract Classes',
        subtitle='Build a subclass, change its behavior, and use different objects through one common type.',
        goals=['Use extends to create a subclass', 'Override an inherited instance method', 'Explain why a parent reference can run child behavior', 'Define an abstract class and implement its abstract methods'],
        sections=[], visuals=[], demos=[])
    def section(title,*paragraphs):
        lesson['sections'].append(dict(title=title,paragraphs=list(paragraphs)))
    def example(part,name,title,code,output,*explain):
        demo(lesson,name,title,code,output,list(explain))
        lesson['demos'][-1].update(after=part,concept_example=True,output_in_comments=True)
    section('Inheritance',
        'Inheritance lets a class build on another class. Animal is the parent class (superclass); Dog is the child class (subclass). class Dog extends Animal expresses an is-a relationship: a Dog is an Animal.',
        'A child can use inherited methods and add its own methods. Here, Dog inherits eat() and adds bark(). We have not changed the parent’s behavior yet.')
    example(1,'InheritanceDemo','A Dog inherits eat() and adds bark().','''
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
''','Eating\nWoof','extends connects the classes. The Dog object can use both methods.')
    section('Method overriding',
        'Overriding gives an inherited instance method a new implementation in the child class. In this example, both classes define public void speak(), but Dog supplies its own body.',
        'Use @Override above the child method so the compiler checks that it really overrides a parent method. Keep the same name and parameter types; the examples also keep the same return type and public access.',
        'Overloading was covered in Lesson 2. The table below is the one comparison to remember before moving on.')
    lesson['visuals'].append(dict(after=2,kind='table',title='Overloading vs overriding',columns=['','Overloading','Overriding'],rows=[
        ['Purpose','Offer different parameter lists under one name','Provide child behavior for an inherited method'],
        ['Parameters','Must differ in number or types','Same parameter types'],
        ['Example','max(int, int) and max(double, double)','Animal.speak() and Dog.speak()'],
        ['Selection','Compiler uses declared types and arguments','Actual object determines the overridden implementation']]))
    example(2,'OverrideDemo','The same method has a different body in Dog.','''
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
''','Animal sound\nWoof','Dog replaces the inherited speak() behavior for Dog objects. Animal objects still use Animal.speak().')
    section('Polymorphism',
        'A parent-type variable can refer to a child object. In Animal pet = new Dog(), Animal is the variable’s declared type, while Dog is the actual object’s type. No extra Animal object is created.',
        'The declared type determines which methods you may call through the variable. The actual object determines which overridden instance-method body runs. Therefore pet.speak() runs Dog.speak(). This runtime choice is called dynamic method dispatch.',
        'The useful result: one loop can call speak() on different Animal objects. Each object supplies its own behavior, so the loop needs no separate test for Dog or Cat.')
    example(3,'DispatchDemo','One loop, two different responses.','''
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
''','Woof\nWoof\nMeow','Every array element is an Animal reference. The objects are a Dog and a Cat; their overrides determine the output.')
    section('Abstract classes and abstract methods',
        'An abstract class is a base class that cannot be instantiated directly. An abstract method declares an operation without a body. A concrete child class must implement the abstract methods it inherits.',
        'Every shape should have an area, but there is no single formula for all shapes. Shape declares area(); Rectangle and Circle provide their own formulas.',
        'An abstract class can also contain fields, constructors and ordinary methods with bodies. Here describe() is shared, while its call to area() uses the actual shape’s implementation. You can write Shape s = new Circle(2), but not new Shape().')
    example(4,'ShapeDemo','A shared method uses each shape’s area formula.','''
abstract class Shape {
    public abstract double area();
    public void describe() {
        System.out.printf(java.util.Locale.ROOT, "Area: %.2f%n", area());
    }
}
class Rectangle extends Shape {
    private double width, height;
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    @Override
    public double area() { return width * height; }
}
class Circle extends Shape {
    private double radius;
    public Circle(double radius) { this.radius = radius; }
    @Override
    public double area() { return Math.PI * radius * radius; }
}
public class ShapeDemo {
    public static void main(String[] args) {
        Shape[] shapes = {new Rectangle(3, 4), new Circle(2)};
        for (Shape shape : shapes) {
            shape.describe(); // Area: 12.00, then Area: 12.57
        }
    }
}
''','Area: 12.00\nArea: 12.57','Shape supplies describe(); each concrete subclass supplies area(). The example uses positive dimensions.')
    lesson['demos'][-1]['explain'].append('The main idea is reuse: callers work with Shape, and each subclass supplies the required formula.')
    lesson['sections'][-1]['html']='''<details class="teaching-note"><summary>Optional reference: additional inheritance rules</summary><ul>
<li>super.method() calls the inherited parent implementation. super(...) calls a parent constructor; constructors are not inherited or overridden.</li>
<li>A final method cannot be overridden. A private parent method is not inherited as an overridable method.</li>
<li>Static methods are hidden, not dynamically overridden. Field access also depends on the declared reference type.</li>
<li>An override cannot reduce accessibility. A reference return type may be more specific, and checked exceptions cannot be broadened beyond the parent declaration.</li>
<li>Assigning a child object to a parent reference is upcasting. Downcasting requires a compatible actual object or it fails at runtime; use polymorphic methods when possible.</li>
</ul></details>'''
