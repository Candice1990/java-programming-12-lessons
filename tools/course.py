import json, textwrap
from pathlib import Path
BASE=json.loads((Path(__file__).parent/'base-content.json').read_text())
LESSONS=[]
def lesson(title,subtitle,goals):
 d=dict(number=len(LESSONS)+1,title=title,subtitle=subtitle,goals=goals,sections=[],visuals=[],demos=[]);LESSONS.append(d);return d
def section(d,title,*paragraphs,note=None):
 s=dict(title=title,paragraphs=list(paragraphs))
 if note:s['note']=note
 d['sections'].append(s)
def reuse(d,key,*ids):
 for i in ids:
  s=BASE['STUDY_CHAPTERS'][key]['sections'][i]
  section(d,s['title'],*s['paragraphs'],note=s.get('note'))
def visual(d,key,*ids):
 d['visuals'].extend(BASE['STUDY_VISUALS'][key][i] for i in ids)
def flow(d,title,items):
 d['visuals'].append(dict(kind='flow',title=title,items=[dict(label=a,detail=b) for a,b in items]))
def table(d,title,columns,rows):d['visuals'].append(dict(kind='table',title=title,columns=columns,rows=rows))
def demo(d,name,title,code,output,explain,*,stdin='',files=None,variable=False):
 d['demos'].append(dict(name=name,title=title,code=textwrap.dedent(code).strip()+'\n',output=output,explain=explain,stdin=stdin,files=files or {},variable=variable))

# 01
x=lesson('Input, Methods & First Objects','Turn input into values, give behavior a name, and model a simple object.', ['Explain source → bytecode → JVM','Read and validate tokens and lines','Choose an overloaded method by its parameters','Distinguish a class, an object and a reference'])
reuse(x,'java-platform-ide',0,3)
section(x,'A class contains methods; a method contains statements','The conventional entry point is public static void main(String[] args). The class name and public source filename must match. Braces group the class body and method body; a semicolon ends most simple statements. Java names are case-sensitive.','A declaration such as int score = 85 creates a variable with a type, name and initial value. Java checks operations against declared types before the program runs. int represents whole numbers, double represents floating-point values, boolean represents true or false, and String represents text.','Compile with javac First.java and run with java First. Do not pass First.class as the class name. An IDE performs these steps for you; its configured JDK determines the compiler and runtime available to the project.')
reuse(x,'java-platform-ide',2,5,6,7,9)
section(x,'Method overloading: same name, different parameters','Overloading means defining methods in the same class with the same name but different parameter lists. Start with one simple change: the number of parameters.',note='A parameter list can differ in number, types, or the order of types. Changing only parameter names or only the return type is not overloading.')
x['sections'][-1]['html']='<figure class="code-example"><figcaption>Same name: add · Different parameters: two integers or three</figcaption><pre><code>static int add(<mark>int a, int b</mark>) {\n    return a + b;\n}\n\nstatic int add(<mark>int a, int b, int c</mark>) {\n    return a + b + c;\n}</code></pre></figure><div class="trace-grid"><div class="expected"><b>Two arguments → first method</b><pre>add(2, 3) → 5</pre></div><div class="expected"><b>Three arguments → second method</b><pre>add(2, 3, 4) → 9</pre></div></div><p>Both methods are named <code>add</code>. The highlighted parameter lists tell them apart. In this example, <code>static int</code> stays the same so you can focus on that difference.</p>'
section(x,'Class, object and reference','A class declares a type with fields for state and methods for behavior. An object is an instance created at runtime with new. A reference is a value that identifies an object; it is not the object itself. Two reference variables can point to the same object, so a mutation through either reference is visible through the other.','An instance method uses a particular object. In circle.area(), circle supplies that object. Creating two Circle instances gives each its own radius field. Calling a method through null fails because null identifies no object. Public fields below make the first example easy to trace; the next lesson will protect state with encapsulation.')
visual(x,'java-platform-ide',0,2,3);visual(x,'object-oriented-programming',0)
demo(x,'InputDemo','Token input, validation and the pending newline',r'''
import java.util.Scanner;
public class InputDemo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter an integer age:");
        while (input.hasNext() && !input.hasNextInt()) {
            System.out.println("Discarded: " + input.next());
        }
        if (!input.hasNextInt()) {
            System.out.println("No age supplied");
            return;
        }
        int age = input.nextInt();
        input.nextLine(); // consume the remainder of the age line
        System.out.println("Enter a full name:");
        String name = input.hasNextLine() ? input.nextLine() : "Unknown";
        System.out.println(name + " is " + age);
    }
}
''','Enter an integer age:\nDiscarded: oops\nEnter a full name:\nAda Lovelace is 20',['hasNextInt() inspects the next token without consuming it; next() discards invalid input.','nextLine() after the age consumes the rest of that line before the full name is read.','The program deliberately leaves shared standard input open. File ownership is handled in lesson 6.'],stdin='oops 20\nAda Lovelace\n')
demo(x,'OverloadDemo','Run it: add two numbers or three','''
public class OverloadDemo {
    static int add(int a, int b) { return a + b; }
    static int add(int a, int b, int c) { return a + b + c; }
    public static void main(String[] args) {
        System.out.println(add(2, 3));
        System.out.println(add(2, 3, 4));
    }
}
''','5\n9',['add(2, 3) calls the method with two parameters and returns 5.','add(2, 3, 4) calls the method with three parameters and returns 9.','Same method name; different parameter lists.'])
demo(x,'ObjectDemo','Two references, one object','''
public class ObjectDemo {
    static class Circle {
        double radius;
        double area() { return Math.PI * radius * radius; }
    }
    public static void main(String[] args) {
        Circle first = new Circle();
        first.radius = 2;
        Circle alias = first;
        alias.radius = 3;
        System.out.println(first.radius);
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", first.area());
    }
}
''','3.0\n28.27',['new creates one Circle; assigning first to alias does not create a copy.','Updating alias.radius changes the same object later read through first.'])

# 02
x=lesson('Encapsulation, Constructors & Inheritance','Protect valid state, construct complete objects, and specialize a parent type.', ['Design private state and controlled properties','Trace this() and super() constructor calls','Understand arrays of object references','Use inheritance for an is-a relationship'])
reuse(x,'object-oriented-programming',0,1)
section(x,'A property is an access policy','A property is a useful way to describe what clients may read or change. A read-only ID has a getter but no setter. A write-only input may be accepted without exposing its stored representation. A computed property such as area can be calculated from other fields instead of being stored.','Encapsulation protects invariants: statements that must remain true for every valid object. A setter that blindly assigns any value is not automatically a good design. For a non-negative balance or a bounded score, validate before committing the change. Constructor validation prevents an invalid object from being created in the first place.')
section(x,'Constructors establish the first valid state','A constructor has the class name and no return type. It runs during object creation and is not an ordinary method. If a class declares no constructor, the compiler supplies a default constructor; once you declare a constructor, an automatic no-argument constructor is no longer supplied.','Overloaded constructors offer several ways to establish an object. this(...) delegates to another constructor in the same class. Under the Java 21 syntax used in these examples, this(...) or super(...) must be the first constructor statement. Delegation avoids duplicating initialization rules.')
section(x,'Object arrays contain references','new Student[3] creates an array with three null references, not three Student objects. Assign a separately created Student to each occupied element before using its methods. An enhanced for loop can read each reference, but assigning a different object to the loop variable does not replace the array element.','The array length is fixed. Track which elements are occupied or initialize all elements before traversal. Arrays are useful for understanding reference storage before collection classes introduce variable-size containers.')
reuse(x,'object-oriented-programming',2)
section(x,'Superclass construction and this versus super','An extends relationship places inherited behavior in a parent and specialized behavior in a child. A Student is a Person; a Student is not an arbitrary container that happens to reuse Person code. The child object contains its inherited state as well as its own fields.','this refers to the current object. super selects the parent implementation or constructor rather than creating another parent object. Constructors are not inherited. If the parent has no accessible no-argument constructor, the child must explicitly call a suitable parent constructor. A private parent field remains accessible through the parent’s methods, not by direct child field access.')
visual(x,'object-oriented-programming',1)
flow(x,'Construction follows a chain',[('new Student(...)','Allocate one object'),('super(name)','Initialize the Person part'),('Student body','Initialize child fields'),('Ready to use','All invariants established')])
demo(x,'EncapsulationDemo','Validate state at the boundary','''
public class EncapsulationDemo {
    static class Student {
        private final int id;
        private int score;
        Student(int id) { this(id, 0); }
        Student(int id, int score) {
            this.id = id;
            setScore(score);
        }
        int getId() { return id; }
        int getScore() { return score; }
        void setScore(int score) {
            if (score < 0 || score > 100) {
                throw new IllegalArgumentException("score must be 0..100");
            }
            this.score = score;
        }
    }
    public static void main(String[] args) {
        Student student = new Student(7, 80);
        student.setScore(92);
        System.out.println(student.getId() + ": " + student.getScore());
    }
}
''','7: 92',['The ID is assigned once and exposed without a setter.','this(id, 0) delegates to the full constructor. The guard rejects an invalid score; exception handling is studied later.'])
demo(x,'ObjectArrayDemo','Initialize each array position','''
public class ObjectArrayDemo {
    static class Student {
        private final String name;
        Student(String name) { this.name = name; }
        String name() { return name; }
    }
    public static void main(String[] args) {
        Student[] students = new Student[2];
        System.out.println(students[0] == null);
        students[0] = new Student("Ada");
        students[1] = new Student("Grace");
        for (Student student : students) System.out.println(student.name());
    }
}
''','true\nAda\nGrace',['The first print proves that allocating the array did not construct its elements.','The loop is safe after both positions have been assigned objects.'])
demo(x,'ConstructorDemo','Observe parent-before-child initialization','''
public class ConstructorDemo {
    static class Person {
        private final String name;
        Person(String name) {
            this.name = name;
            System.out.println("Person constructor");
        }
        String name() { return name; }
    }
    static class Student extends Person {
        private final int id;
        Student(String name, int id) {
            super(name);
            this.id = id;
            System.out.println("Student constructor");
        }
        String describe() { return name() + " #" + id; }
    }
    public static void main(String[] args) {
        System.out.println(new Student("Ada", 7).describe());
    }
}
''','Person constructor\nStudent constructor\nAda #7',['super(name) supplies the parent constructor’s required argument.','The inherited name() method reads private parent state without exposing its field.'])

# 03
x=lesson('Overriding, Polymorphism & Abstract Classes','Separate the reference contract from the implementation chosen at runtime.', ['Distinguish overload selection from method dispatch','Write valid overrides','Use parent references to call child behavior','Design an abstract class with shared state'])
section(x,'Overriding preserves a method contract','A subclass overrides an inherited instance method by supplying the same name and parameter types with a compatible return type. The override must not reduce accessibility or broaden checked exceptions. A covariant reference return type may be more specific. Use @Override so that the compiler checks your intention.','Overloading is resolved at compile time from method signatures and argument types. Overriding selects the implementation at runtime from the actual object. Calling both mechanisms “polymorphism” must not hide this timing difference.')
section(x,'Dynamic method dispatch','In Animal pet = new Dog(), Animal is the declared reference type and Dog is the runtime object type. The compiler permits operations available through Animal. When an overridden instance method is invoked, the Dog implementation runs. A method that exists only on Dog cannot be called through pet without a suitable cast.','The object does not change when assigned to a parent reference. Upcasting merely changes the view available to the compiler. Downcasting is a runtime assertion about the object’s type; an incorrect cast fails. Prefer polymorphic operations to long chains of casts.')
section(x,'What is not ordinary overriding','A static method belongs to its class and can be hidden rather than dynamically overridden. Fields are also selected according to the reference expression’s type. A private parent method is not inherited as an overridable method, and a final method cannot be overridden. Constructors participate in construction, not overriding.','super.method() deliberately invokes inherited parent behavior. It is useful when the child extends an operation rather than replacing it completely. Use it to preserve a meaningful parent contract, not merely to silence an error.')
section(x,'Abstract classes combine contracts and implementation','An abstract class cannot be instantiated directly. It may contain fields, constructors, concrete methods and abstract methods. An abstract method states a required operation without providing its body. A concrete subclass must implement every remaining abstract method.','Shared state belongs in the abstract base when it is genuinely common to all specializations. For shapes, the base might store a label and require area(). A method in the base can call area(); that call still dispatches to the child implementation.')
section(x,'Design around substitutability','Code that accepts Shape should remain meaningful for every valid Shape implementation. An overridden method should preserve the meaning promised by the parent: if area() returns a non-negative measurement, a subclass should not reinterpret it as a formatted message or an unrelated identifier.','Keep the public contract small. The benefit of polymorphism is that a caller can work with the abstraction while new implementations are added independently. The loop in the demonstration does not need to know whether the next object is a rectangle or a circle.')
visual(x,'object-oriented-programming',2,3)
flow(x,'An overridden call has two checks',[('Compile time','Is speak() available on Animal?'),('Runtime object','pet refers to a Dog'),('Dispatch','Choose Dog.speak()'),('Result','Execute the child body')])
demo(x,'DispatchDemo','Reference type permits; object type dispatches','''
public class DispatchDemo {
    static class Animal { String speak() { return "sound"; } }
    static class Dog extends Animal {
        @Override String speak() { return "woof"; }
    }
    static void show(Animal animal) { System.out.println(animal.speak()); }
    public static void main(String[] args) {
        Animal pet = new Dog();
        show(pet);
        show(new Animal());
    }
}
''','woof\nsound',['show receives an Animal reference in both calls.','Only the runtime object changes, so dispatch selects a different speak() body.'])
demo(x,'BindingDemo','Overload selection happens before dispatch','''
public class BindingDemo {
    static class Animal { }
    static class Dog extends Animal { }
    static String identify(Animal a) { return "Animal overload"; }
    static String identify(Dog d) { return "Dog overload"; }
    public static void main(String[] args) {
        Animal pet = new Dog();
        System.out.println(identify(pet));
        System.out.println(identify(new Dog()));
    }
}
''','Animal overload\nDog overload',['The declared type of pet is Animal, so the Animal overload is selected.','These static overloads do not dynamically switch based on the object stored in pet.'])
demo(x,'ShapeDemo','One abstract contract, two implementations','''
public class ShapeDemo {
    abstract static class Shape {
        private final String label;
        Shape(String label) { this.label = label; }
        abstract double area();
        void describe() {
            System.out.printf(java.util.Locale.ROOT, "%s: %.2f%n", label, area());
        }
    }
    static class Rectangle extends Shape {
        private final double width, height;
        Rectangle(double width, double height) {
            super("Rectangle"); this.width = width; this.height = height;
        }
        @Override double area() { return width * height; }
    }
    static class Circle extends Shape {
        private final double radius;
        Circle(double radius) { super("Circle"); this.radius = radius; }
        @Override double area() { return Math.PI * radius * radius; }
    }
    public static void main(String[] args) {
        Shape[] shapes = {new Rectangle(3, 4), new Circle(2)};
        for (Shape shape : shapes) shape.describe();
    }
}
''','Rectangle: 12.00\nCircle: 12.57',['The base constructor initializes common state, even though Shape itself cannot be instantiated.','describe() is inherited, but its area() call dispatches to the concrete shape. Dimensions are positive constants in this focused demo.'])

# 04
x=lesson('Interfaces & Nested Classes','Express capabilities independently of inheritance and place helper types in the right scope.', ['Implement interface contracts','Explain callback control flow','Distinguish four nested-class forms','Understand outer-instance access and local capture'])
section(x,'An interface describes a capability','An interface declares a contract that different classes can implement. A class extends at most one class but may implement several interfaces. A variable of an interface type can refer to any object implementing it, allowing the caller to depend on the capability rather than the implementation.','Ordinary interface abstract methods are public, so their class implementations must be public. Interface fields are public static final constants, not per-object state. Interfaces may also have default and static methods; private helper methods support interface implementations. A default method provides behavior, but does not give the interface ordinary instance fields.')
section(x,'Abstract class or interface?','Use an abstract class when related types share state, construction rules and partial implementation. Use an interface to express a role that otherwise unrelated classes can adopt. A class can combine both: extend a shared base and implement several capabilities.','If unrelated interfaces provide conflicting defaults with the same signature, the implementing class must resolve the conflict explicitly. Java’s multiple interface inheritance does not mean that it inherits multiple independent parent-class object states.')
section(x,'Callbacks reverse who chooses the behavior','A callback is an operation supplied to another component so that the component can invoke it at the appropriate time. A Button can know how to signal a click without knowing whether the application will save, print or navigate. The caller provides the action through an interface.','The callback is still an ordinary method invocation. The useful distinction is responsibility: the component decides when to call; the supplied object decides what happens. Anonymous classes provide a compact implementation before Lambda syntax is introduced.')
reuse(x,'inner-classes',0,1,2,3)
visual(x,'inner-classes',0)
flow(x,'A callback separates timing from behavior',[('Application','Supplies a ClickListener'),('Button','Stores the interface reference'),('click()','Invokes listener.onClick()'),('Listener','Runs application-specific behavior')])
demo(x,'InterfaceDemo','Program to a capability','''
public class InterfaceDemo {
    interface Printable { void print(); }
    interface Named { String name(); }
    static class Report implements Printable, Named {
        @Override public String name() { return "Results"; }
        @Override public void print() { System.out.println(name()); }
    }
    public static void main(String[] args) {
        Printable document = new Report();
        document.print();
    }
}
''','Results',['Report satisfies two interfaces while still extending only Object implicitly.','The Printable reference exposes print(), not every method declared by Report.'])
demo(x,'NestedDemo','Member inner versus static nested','''
public class NestedDemo {
    private final String name;
    NestedDemo(String name) { this.name = name; }
    class Member { String read() { return name; } }
    static class Helper { String read() { return "no implicit outer"; } }
    public static void main(String[] args) {
        NestedDemo outer = new NestedDemo("classroom");
        Member member = outer.new Member();
        Helper helper = new Helper();
        System.out.println(member.read());
        System.out.println(helper.read());
    }
}
''','classroom\nno implicit outer',['outer.new Member() binds the inner instance to a specific enclosing object.','Helper has no implicit outer object; it could access one only through an explicit reference.'])
demo(x,'CallbackDemo','Local capture in an anonymous callback','''
public class CallbackDemo {
    interface ClickListener { void onClick(); }
    static class Button {
        private final ClickListener listener;
        Button(ClickListener listener) { this.listener = listener; }
        void click() { listener.onClick(); }
    }
    public static void main(String[] args) {
        String message = "Saved"; // effectively final
        Button button = new Button(new ClickListener() {
            @Override public void onClick() { System.out.println(message); }
        });
        button.click();
    }
}
''','Saved',['The anonymous class implements ClickListener without a separate class name.','message is captured and must remain final or effectively final; the callback runs only when click() calls it.'])

# 05
x=lesson('Packages, Access & Exception Foundations','Organize types into boundaries and distinguish a failure from its handling policy.', ['Match package names to project layout','Apply access modifiers across files','Classify Java failures and exception types','Trace try/catch and exception propagation'])
reuse(x,'java-platform-ide',4)
reuse(x,'object-oriented-programming',5,6)
section(x,'Access is checked at the declaration boundary','public members are accessible wherever their enclosing type is accessible. A member with no modifier is package-private and is available within its package. private members are restricted to their enclosing top-level class’s nest of nested types. protected permits package access and controlled access from subclasses outside the package.','Across packages, protected instance access from a subclass is not a general permission to inspect any arbitrary parent object. The qualifying reference must satisfy the subclass access rule. Importing a type only shortens its name; it never bypasses access checks. Top-level classes can be public or package-private, not private or protected.')
reuse(x,'exception-handling',0,1,2)
section(x,'Read a stack trace from the failure outward','An exception stack trace identifies the exception type and message, followed by call frames. Find the first frame in your own code and inspect the operation at that line. The caller frames show how execution arrived there. A cause chain may explain an underlying file or parsing failure.','A catch block runs only for a compatible exception. Once a throw occurs, the remaining statements in that try path are skipped. If the method cannot handle the failure, propagation unwinds the call stack until a handler is found; otherwise the thread ends with an uncaught exception.')
section(x,'Specific recovery belongs before general recovery','Order catch blocks from more specific types to broader types. A broad catch placed first may make a later specific catch unreachable. Multi-catch combines unrelated exception alternatives when the recovery policy is identical. A nested try is useful only when an inner operation has a distinct recovery policy.','Do not confuse guarding expected user input with catching every failure. hasNextInt() can avoid an ordinary invalid-token exception; catching a domain exception can report a rule violation. Neither technique justifies hiding all exceptions or continuing with incomplete state.')
visual(x,'object-oriented-programming',4);visual(x,'exception-handling',0,1,2)
demo(x,'PackageDemo','A package is a real compilation boundary','''
package school.app;
import school.model.Student;
public class PackageDemo {
    public static void main(String[] args) {
        Student student = new Student("Ada");
        System.out.println(student.name());
        // student.name = "Grace"; // private: does not compile
        // student.internalLabel(); // package-private: does not compile here
    }
}
''','Ada',['The public type and its public method cross the package boundary.','The commented lines illustrate illegal accesses; imports do not change their visibility.'],files={'school/model/Student.java':'''package school.model;
public class Student {
    private final String name;
    public Student(String name) { this.name = name; }
    public String name() { return name; }
    String internalLabel() { return "internal"; }
}
'''})
demo(x,'CatchDemo','A failed conversion transfers control','''
public class CatchDemo {
    public static void main(String[] args) {
        String[] inputs = {"12", "oops", "4"};
        for (String text : inputs) {
            try {
                int value = Integer.parseInt(text);
                System.out.println("Accepted: " + value);
            } catch (NumberFormatException e) {
                System.out.println("Rejected: " + text);
            }
        }
    }
}
''','Accepted: 12\nRejected: oops\nAccepted: 4',['Only the invalid record takes the catch path.','The loop can continue because each iteration has an independent result and a clear rejection policy.'])
demo(x,'PropagationDemo','The caller chooses a recovery boundary','''
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
''','The input is not an integer\nFinished',['The exception passes through parse() and doubled(), neither of which handles it.','The println inside the try is never completed; the compatible catch in main handles the failure.'])

# 06
x=lesson('Exceptions, Resources & First Threads','Make failure contracts explicit, close owned resources, and start concurrent work.', ['Distinguish throw from throws','Create and handle a checked domain exception','Read files with Scanner and automatic cleanup','Compare Thread.start() with an ordinary run() call'])
reuse(x,'exception-handling',3,4)
section(x,'Custom exceptions give a failure a domain name','A custom checked exception extends Exception. Its constructor normally passes a meaningful message to super; a second constructor can preserve an underlying cause. A method declaring throws InvalidScoreException requires its caller to catch or declare that checked failure.','An exception object carries evidence, not a repair strategy. The method that detects the invalid value may be unable to ask a user for another value. The caller at the interaction boundary can decide whether to reject the record, retry or stop.')
section(x,'finally observes both success and failure','A finally block executes as control leaves its try/catch, including an ordinary return. It is not an absolute guarantee against JVM termination or a process crash. Returning or throwing an unrelated exception from finally can replace an earlier result or failure and should be avoided.','Use finally when a cleanup action is not represented by an AutoCloseable resource. For files and streams, prefer try-with-resources: it closes resources in reverse declaration order and preserves close failures as suppressed exceptions when the body has already failed.')
reuse(x,'java-platform-ide',8)
section(x,'File input combines token rules with ownership','A file-backed Scanner uses the same token and line operations as keyboard input. Choose whether each record is a token, a full line or several fields. hasNextInt() alone stops at the first non-integer token, so a robust importer must deliberately reject or skip malformed content rather than silently treating it as end of file.','The file path is resolved from the process working directory unless an absolute path is supplied. try-with-resources owns and closes the file scanner. That ownership differs from a shared Scanner around System.in. Error messages should identify the input record or path without discarding the original cause.')
reuse(x,'multithreading',0)
section(x,'A task describes work; a thread executes it','A Runnable supplies a run() method describing work. A Thread manages an execution path. Extending Thread also works, but implementing Runnable keeps the task reusable and avoids consuming the class’s single superclass slot. The next lesson will coordinate several threads safely.','Calling start() schedules a new thread that will invoke run(). Calling run() directly is an ordinary method call on the current thread. A Thread instance can be started only once. Output order between independent threads is not a dependable indication of program correctness.')
flow(x,'Failure and cleanup travel together',[('Read a record','Scanner supplies text'),('Validate','Accept or throw a domain exception'),('Handle','Caller chooses recovery'),('Close','Owned file resource is released')])
table(x,'Sequential call versus thread start',['Expression','Where run() executes','Meaning'],[['task.run()','Current thread','Ordinary method call'],['worker.run()','Current thread','Does not start a new thread'],['worker.start()','New thread','Schedules one execution'],['worker.join()','Calling thread waits','Wait for worker completion']])
demo(x,'DomainExceptionDemo','Declare a checked failure and handle it','''
public class DomainExceptionDemo {
    static class InvalidScoreException extends Exception {
        private static final long serialVersionUID = 1L;
        InvalidScoreException(String message) { super(message); }
    }
    static int validate(int score) throws InvalidScoreException {
        if (score < 0 || score > 100) {
            throw new InvalidScoreException("Score outside 0..100: " + score);
        }
        return score;
    }
    public static void main(String[] args) {
        try {
            System.out.println(validate(120));
        } catch (InvalidScoreException e) {
            System.out.println(e.getMessage());
        } finally {
            System.out.println("Validation finished");
        }
    }
}
''','Score outside 0..100: 120\nValidation finished',['throw raises one exception; throws advertises the method’s checked failure.','finally runs after the handled failure, but does not replace it with a return value.'])
demo(x,'FileScannerDemo','Read all tokens without hiding malformed data','''
import java.io.IOException;
import java.nio.file.Path;
import java.util.Scanner;
public class FileScannerDemo {
    public static void main(String[] args) {
        int total = 0;
        try (Scanner input = new Scanner(Path.of("scores.txt"))) {
            while (input.hasNext()) {
                if (input.hasNextInt()) total += input.nextInt();
                else System.out.println("Skipped: " + input.next());
            }
            System.out.println("Total: " + total);
        } catch (IOException e) {
            System.err.println("Cannot read scores.txt: " + e.getMessage());
        }
    }
}
''','Skipped: bad\nTotal: 170',['The loop checks for any remaining token, then chooses integer conversion or explicit rejection.','The scanner closes automatically when the try exits, including exceptional exits.'],files={'scores.txt':'80 bad 90\n'})
demo(x,'FirstThreadDemo','The same task can run on different threads','''
public class FirstThreadDemo {
    static class Task implements Runnable {
        @Override public void run() {
            System.out.println("Running on " + Thread.currentThread().getName());
        }
    }
    static class NamedThread extends Thread {
        NamedThread() { super("subclass-worker"); }
        @Override public void run() { System.out.println("Thread subclass ran"); }
    }
    public static void main(String[] args) throws InterruptedException {
        Task task = new Task();
        task.run();
        Thread worker = new Thread(task, "worker");
        worker.start();
        worker.join();
        Thread second = new NamedThread();
        second.start();
        second.join();
    }
}
''','Running on main\nRunning on worker\nThread subclass ran',['The first call is sequential; start() creates the separate execution path.','join() makes this demonstration’s output order repeatable; lifecycle and coordination come next.'])

# 07
x=lesson('Thread Lifecycle, Synchronization & Coordination','Make shared-state rules explicit and use one monitor to enforce them.', ['Explain thread states and completion','Handle interruption cooperatively','Protect an entire shared invariant','Use condition loops for wait/notifyAll'])
reuse(x,'multithreading',2,3)
section(x,'Start workers together; wait for all results','A group of workers can be stored in a Thread array before collections have been introduced. Start every worker in one loop, then join every worker in a second loop. Joining immediately after each start would serialize those tasks and prevent the intended overlap.','A ThreadGroup can associate named platform threads for organizational purposes, but it does not make shared data safe or replace explicit completion. Priority and yield are scheduling hints, not ordering rules. Never use a guessed sleep duration as proof that another task has completed.')
reuse(x,'thread-synchronization',0,1,2,3,4,5)
section(x,'Interrupt is a request, not a forced kill','A thread blocked in sleep(), join() or wait() may receive InterruptedException. It should stop, propagate the exception, or restore the interrupted status if it cannot complete the cancellation decision itself. An empty catch loses the cancellation request.','When a loop does CPU work rather than calling interruptible blocking methods, it can periodically inspect the interrupted status. Do not rely on daemon threads to finish important writes: the JVM may terminate once no non-daemon threads remain.')
visual(x,'multithreading',1);visual(x,'thread-synchronization',0,1)
# A state relationship rather than a misleading linear lifecycle.
x['visuals'].append(dict(kind='tree',title='Thread states are branches, not a fixed checklist',root='NEW → start() → RUNNABLE',branches=[dict(label='BLOCKED',detail='Waiting to acquire an intrinsic monitor',children=['Lock acquired → RUNNABLE']),dict(label='WAITING / TIMED_WAITING',detail='wait, join, sleep or another waiting operation',children=['Signal, completion, timeout or interruption → resume when eligible']),dict(label='TERMINATED',detail='run() returns or ends with an uncaught failure',children=['The same Thread cannot be started again'])]))
demo(x,'CounterDemo','One monitor protects every update','''
public class CounterDemo {
    static class Counter {
        private int value;
        synchronized void increment() { value++; }
        synchronized int value() { return value; }
    }
    static class Task implements Runnable {
        private final Counter counter;
        Task(Counter counter) { this.counter = counter; }
        @Override public void run() {
            for (int i = 0; i < 10000; i++) counter.increment();
        }
    }
    public static void main(String[] args) throws InterruptedException {
        Counter counter = new Counter();
        ThreadGroup group = new ThreadGroup("counters");
        Thread[] workers = new Thread[4];
        for (int i = 0; i < workers.length; i++) {
            workers[i] = new Thread(group, new Task(counter), "worker-" + i);
        }
        for (Thread worker : workers) worker.start();
        for (Thread worker : workers) worker.join();
        System.out.println(counter.value());
    }
}
''','40000',['All tasks share one Counter, so every synchronized method locks the same object.','ThreadGroup names an organizational group; synchronization supplies safety and join supplies completion.','Without synchronization, lost updates are possible but not guaranteed on every run.'])
demo(x,'InterruptDemo','Cancellation remains visible','''
public class InterruptDemo {
    static class Sleeper implements Runnable {
        @Override public void run() {
            try {
                Thread.sleep(10000);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                System.out.println("Cancellation acknowledged");
            }
        }
    }
    public static void main(String[] args) throws InterruptedException {
        Thread worker = new Thread(new Sleeper());
        worker.start();
        worker.interrupt();
        worker.join();
        System.out.println("Terminated: " + !worker.isAlive());
    }
}
''','Cancellation acknowledged\nTerminated: true',['An interrupt requested before sleep is reached is still noticed by the interruptible operation.','The catch restores status and the task finishes; the main thread waits for that completion.'])
demo(x,'SlotDemo','A finite producer-consumer protocol','''
public class SlotDemo {
    static class Slot {
        private int value;
        private boolean full;
        synchronized void put(int next) throws InterruptedException {
            while (full) wait();
            value = next;
            full = true;
            notifyAll();
        }
        synchronized int take() throws InterruptedException {
            while (!full) wait();
            int result = value;
            full = false;
            notifyAll();
            return result;
        }
    }
    public static void main(String[] args) throws InterruptedException {
        Slot slot = new Slot();
        Thread producer = new Thread(new Runnable() {
            public void run() {
                try { for (int i = 1; i <= 3; i++) slot.put(i); }
                catch (InterruptedException e) { Thread.currentThread().interrupt(); }
            }
        });
        Thread consumer = new Thread(new Runnable() {
            public void run() {
                try { for (int i = 1; i <= 3; i++) System.out.println(slot.take()); }
                catch (InterruptedException e) { Thread.currentThread().interrupt(); }
            }
        });
        producer.start(); consumer.start();
        producer.join(); consumer.join();
    }
}
''','1\n2\n3',['wait() releases the Slot monitor; returning from wait requires reacquiring it.','The while loops recheck the condition after every wake-up. notifyAll() signals a change but does not hand over the lock immediately.','This finite demonstration assumes both tasks complete normally. Coordinated cancellation requires a shared close/cancel protocol so that a partner cannot remain waiting.'])

# 08
x=lesson('Reflection, Annotations & Lambda Expressions','Inspect runtime type information, attach metadata, and pass behavior through an interface.', ['Inspect and invoke a known public method','Read runtime annotations','Give a lambda a functional-interface target','Use capture and method-reference forms'])
reuse(x,'reflection-annotations',0,1,2,3,4)
section(x,'Reflection shifts some checks to runtime','A direct call such as service.greet() is checked by the compiler against a known type. Looking up getMethod("greet") depends on a string and can fail at runtime if the name or parameter signature is wrong. Method.invoke may also wrap an exception thrown by the invoked method.','The cost and optimizations of reflection depend on the operation and runtime. Do not assume one fixed slowdown factor. Prefer a normal interface for routine application behavior; use reflection where runtime discovery is the purpose. Access checks and module boundaries still apply.')
section(x,'A functional interface gives behavior a type','A functional interface has one abstract operation after inherited method rules are taken into account. Default and static methods do not add abstract operations; public methods matching Object methods do not create an extra functional obligation. @FunctionalInterface asks the compiler to verify the contract.','A lambda supplies the implementation of that operation. Its target interface determines parameter types and result type. It is not a free-standing unnamed method that can be assigned to any arbitrary type. The first demonstrations use custom interfaces so the syntax can be understood before generic library interfaces.')
reuse(x,'lambda-stream-api',1)
section(x,'Expression body or block body','An expression lambda returns the expression value when its target requires a result: x -> x * 2. A block lambda uses braces; a value-returning block must explicitly return along every normal result path. A void-compatible callback can perform an action without returning a value.','The lambda uses the enclosing this rather than introducing the anonymous class’s separate this. Captured local variables cannot be reassigned after initialization if that would make them no longer effectively final. An object referenced by such a variable may still be mutable; capture does not make the object immutable or thread-safe.')
visual(x,'reflection-annotations',0,1,2)
table(x,'Read method references by their shape',['Form','Example','Equivalent intent'],[['Static method','Integer::parseInt','text -> Integer.parseInt(text)'],['Bound instance','printer::print','text -> printer.print(text)'],['Unbound instance','String::length','text -> text.length()'],['Constructor','StringBuilder::new','() -> new StringBuilder()']])
demo(x,'ReflectionDemo','Read metadata and invoke a named method','''
import java.lang.annotation.*;
import java.lang.reflect.Method;
public class ReflectionDemo {
    @Retention(RetentionPolicy.RUNTIME)
    @Target(ElementType.METHOD)
    @interface Topic { String value(); }
    public static class Service {
        @Topic("greeting")
        public String greet() { return "Hello"; }
    }
    public static void main(String[] args) throws ReflectiveOperationException {
        Class<Service> type = Service.class;
        Method method = type.getMethod("greet");
        Topic topic = method.getAnnotation(Topic.class);
        System.out.println(topic.value());
        System.out.println(method.invoke(new Service()));
    }
}
''','greeting\nHello',['RUNTIME retention keeps the annotation available to getAnnotation().','The annotation contributes data; the reflection code explicitly chooses to invoke the method.','Class<Service> preserves type information; a full treatment of generic type parameters follows in lesson 9.'])
demo(x,'LambdaDemo','Replace boilerplate with a target-typed lambda','''
public class LambdaDemo {
    @FunctionalInterface interface IntOperation { int apply(int value); }
    static int evaluate(int value, IntOperation operation) {
        return operation.apply(value);
    }
    public static void main(String[] args) {
        int factor = 3;
        IntOperation multiply = value -> value * factor;
        IntOperation absolute = Math::abs;
        System.out.println(evaluate(7, multiply));
        System.out.println(evaluate(-4, absolute));
    }
}
''','21\n4',['factor is effectively final and is captured by multiply.','Math::abs matches int -> int here because IntOperation supplies the target signature.'])
demo(x,'MethodReferenceDemo','Bound, unbound and constructor references','''
public class MethodReferenceDemo {
    interface TextLength { int apply(String text); }
    interface Message { void send(String text); }
    interface BuilderFactory { StringBuilder create(); }
    public static void main(String[] args) {
        TextLength length = String::length;
        Message print = System.out::println;
        BuilderFactory factory = StringBuilder::new;
        print.send("Length: " + length.apply("Java"));
        System.out.println(factory.create().append("Ready"));
    }
}
''','Length: 4\nReady',['String::length receives the String instance as its lambda argument.','System.out::println binds one existing output object; StringBuilder::new creates a new object on each call.'])

# 09
x=lesson('Generics & the Collection Landscape','Carry type information through reusable code before choosing a container.', ['Declare generic classes and methods','Explain bounds, invariance and wildcards','Recognize erasure and its restrictions','Distinguish Collection interfaces from implementations'])
reuse(x,'generics',0,1)
section(x,'Type parameters belong to declarations','A class-level T is available throughout the instance API of Box<T>. A static method cannot refer to that instance type parameter unless it declares an independent parameter of its own. A generic method places <T> before its return type, for example static <T> T echo(T value).','Use descriptive type names when they improve clarity, such as Key and Value. Generic type arguments must be reference types; use Integer rather than int. Autoboxing can convert primitive values at API boundaries, but unboxing a null wrapper throws NullPointerException.')
reuse(x,'generics',2,3,4)
section(x,'Erasure does not mean all type information disappears','A type parameter generally erases to Object or its leftmost bound. The compiler inserts casts where necessary and may generate bridge methods so overriding continues to work after erasure. Different parameterizations such as Box<String> and Box<Integer> ordinarily share one runtime class.','Generic signatures may still be recorded as metadata and inspected through reflection. Erasure means that an individual object does not generally carry a reified list element type that can enforce instanceof List<String>. Two overloads whose signatures become identical after erasure are illegal. A static field belongs to the erased class, not separately to each type argument.')
section(x,'Collections organize groups of values','A collection framework separates contracts from storage strategies. List promises sequence and positional access; Set promises no duplicates under its equality rule; Queue describes processing order. Map associates keys with values and is part of the framework, but does not extend Collection.','Declare a variable using the smallest interface that expresses the operations needed. List<String> names the contract while new ArrayList<>() selects storage. Generics preserve the element type through add, get and iteration, reducing casts and catching mismatched values at compilation.')
section(x,'Choose by required behavior before performance','Ask whether duplicates are allowed, whether positions matter, whether keys identify values, and whether processing order is required. Then choose an implementation. A linked structure is not automatically faster merely because insertion is mentioned: locating an insertion point also costs time.','The next lessons study operations and implementation trade-offs in detail. For now, read List<E> extends Collection<E> extends Iterable<E> as a type relationship that carries the same element parameter forward. This is interface inheritance, separate from invariance between List<Integer> and List<Number>.')
visual(x,'generics',0,1);visual(x,'collections',0)
demo(x,'GenericDemo','A generic class and an independent generic method','''
public class GenericDemo {
    static class Box<T> {
        private final T value;
        Box(T value) { this.value = value; }
        T get() { return value; }
    }
    static <T> T echo(T value) { return value; }
    static <T extends Number> double twice(T value) {
        return value.doubleValue() * 2;
    }
    public static void main(String[] args) {
        Box<String> text = new Box<>("Java");
        System.out.println(text.get().toUpperCase());
        System.out.println(echo(42));
        System.out.println(twice(3));
        System.out.println(text.getClass() == new Box<Integer>(1).getClass());
    }
}
''','JAVA\n42\n6.0\ntrue',['The diamond lets the compiler infer the constructor’s type argument.','The bound makes doubleValue() available without a cast.','The final comparison illustrates one runtime class for both parameterizations.'])
demo(x,'WildcardDemo','Read from a producer and write to a consumer','''
import java.util.ArrayList;
import java.util.List;
public class WildcardDemo {
    static double sum(List<? extends Number> values) {
        double total = 0;
        for (Number value : values) total += value.doubleValue();
        return total;
    }
    static void addDefaults(List<? super Integer> values) {
        values.add(0); values.add(1);
    }
    public static void main(String[] args) {
        List<Integer> ints = new ArrayList<>();
        ints.add(10); ints.add(20);
        List<Number> numbers = new ArrayList<>();
        addDefaults(numbers);
        System.out.println(sum(ints));
        System.out.println(numbers);
    }
}
''','30.0\n[0, 1]',['The sum method accepts both integer and other numeric lists without adding to them.','A consumer of Integer may be a List<Integer>, List<Number> or List<Object>.','The unknown exact producer type prevents adding a specific non-null number safely; null is the limited exception.'])
demo(x,'GenericInheritanceDemo','Carry a parameter through an interface','''
public class GenericInheritanceDemo {
    interface Repository<T> { void save(T value); T load(); }
    static class MemoryRepository<T> implements Repository<T> {
        private T value;
        public void save(T value) { this.value = value; }
        public T load() { return value; }
    }
    static class TextRepository extends MemoryRepository<String> { }
    public static void main(String[] args) {
        Repository<String> repository = new TextRepository();
        repository.save("Typed storage");
        System.out.println(repository.load());
    }
}
''','Typed storage',['MemoryRepository forwards T; TextRepository fixes it to String.','The interface still controls the public contract. This one-value example does not yet implement a multi-record database.'])

# 10
x=lesson('Lists, Iterators & Queues','Manipulate ordered data and make traversal rules explicit.', ['Use Collection and List operations','Choose ArrayList or LinkedList deliberately','Traverse and remove through an Iterator','Distinguish FIFO queues, deques and priority queues'])
section(x,'Collection defines common operations','Collection<E> defines operations such as add, remove, contains, size, isEmpty and clear. Bulk operations include addAll, removeAll and retainAll. These are contracts: some implementations do not support every mutation, and optional operations may throw UnsupportedOperationException.','contains and remove(Object) use equality rather than reference identity. List adds positional access, permits duplicate values and defines equality in terms of the same elements in the same order. Set is a different contract and does not gain indexed get simply because it is a collection.')
section(x,'ArrayList is a resizable array','ArrayList stores references in an internal array and resizes that storage as needed. get(index) gives constant-time indexed access. Appending is amortized constant time, while inserting or removing near the beginning requires shifting later elements. Size is the number of stored elements; capacity is an internal storage allocation.','remove(1) on a List<Integer> removes the element at index 1. remove(Integer.valueOf(1)) removes the first equal value. This is an important overload distinction. Index bounds run from zero through size - 1 for reading existing elements.')
section(x,'LinkedList trades indexing for links','LinkedList stores elements in linked nodes and also implements Deque. Indexed get must traverse nodes, so repeated get(i) inside a large loop can perform much more work than expected. Use an iterator or enhanced for loop for sequential traversal.','Insertion through a positioned list iterator and operations at the ends can update links efficiently. Finding a value or index still takes time. The choice between ArrayList and LinkedList must include access patterns and memory overhead, not just the word “insertion”.')
reuse(x,'collections',2,4)
section(x,'Iterable produces iterators; an iterator tracks progress','Iterable<E> supplies iterator(), which returns a cursor over elements. Iterator<E> supplies hasNext() and next(), and may support remove(). An enhanced for loop over an Iterable is syntactic convenience for obtaining and using such an iterator. Arrays are also supported by enhanced for through a separate language translation.','A fresh iterator should represent an independent traversal. next() must throw NoSuchElementException when exhausted, not return an arbitrary null sentinel. Iterator.remove(), when supported, removes the last element returned by next(); it cannot be called twice without another next().')
section(x,'Queue and Deque describe processing order','Queue offers add/remove/element methods that can throw on failure and offer/poll/peek alternatives that signal ordinary failure with a special return value. poll and peek return null for an empty queue, which is one reason implementations such as ArrayDeque forbid null elements.','Deque supports both ends. addLast and removeFirst implement a FIFO queue; push and pop use the front for a LIFO stack. ArrayDeque is a useful general starting point for stack or queue behavior when null elements and concurrent access are not required.')
section(x,'A PriorityQueue is not a sorted list','PriorityQueue chooses its head by priority, using natural order or an explicit comparator. poll repeatedly removes the smallest remaining element under that ordering. Ties need not preserve insertion order. Iterating or printing the queue does not promise sorted order.','Queue priority does not mean operating-system thread priority. One is an ordering rule for stored elements, the other is a scheduling hint. Keep the concepts separate. For sorted output from a priority queue, deliberately poll until it is empty or copy its elements and sort the copy.')
visual(x,'collections',1)
flow(x,'Iterator traversal is a protocol',[('iterator()','Create a cursor'),('hasNext()','Check whether an element remains'),('next()','Read and advance'),('remove()','Optionally remove the returned element')])
table(x,'Queue method pairs',['Operation','Exception-based','Special-value form'],[['Insert','add(e)','offer(e): false on capacity failure'],['Read head','element()','peek(): null if empty'],['Remove head','remove()','poll(): null if empty']])
demo(x,'ListDemo','Distinguish index removal from value removal','''
import java.util.ArrayList;
import java.util.List;
public class ListDemo {
    public static void main(String[] args) {
        List<Integer> values = new ArrayList<>();
        values.add(1); values.add(2); values.add(1);
        values.remove(1);
        System.out.println(values);
        values.remove(Integer.valueOf(1));
        System.out.println(values);
        values.set(0, 9);
        System.out.println(values.get(0));
    }
}
''','[1, 1]\n[1]\n9',['The first removal selects remove(int index), deleting 2.','Wrapping the argument as Integer selects remove(Object), deleting one matching value.'])
demo(x,'IteratorDemo','Remove through the active iterator','''
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
public class IteratorDemo {
    public static void main(String[] args) {
        List<Integer> scores = new ArrayList<>();
        scores.add(40); scores.add(80); scores.add(55);
        Iterator<Integer> iterator = scores.iterator();
        while (iterator.hasNext()) {
            int score = iterator.next();
            if (score < 50) iterator.remove();
        }
        System.out.println(scores);
    }
}
''','[80, 55]',['Removal is performed by the cursor currently traversing the collection.','Calling scores.remove(...) during this traversal could invalidate the iterator. Fail-fast detection is best effort, not a concurrency safety mechanism.'])
demo(x,'IterableDemo','Build a small independent cursor','''
import java.util.Iterator;
import java.util.NoSuchElementException;
public class IterableDemo {
    static class Range implements Iterable<Integer> {
        private final int end;
        Range(int end) { this.end = end; }
        public Iterator<Integer> iterator() {
            return new Iterator<Integer>() {
                private int next = 0;
                public boolean hasNext() { return next < end; }
                public Integer next() {
                    if (!hasNext()) throw new NoSuchElementException();
                    return next++;
                }
            };
        }
    }
    public static void main(String[] args) {
        for (int value : new Range(3)) System.out.println(value);
    }
}
''','0\n1\n2',['iterator() constructs a new cursor each time, so traversals do not share a position.','The enhanced for loop uses the Iterable contract; it does not require a List.'])
demo(x,'QueueDemo','FIFO, LIFO and priority order','''
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.PriorityQueue;
import java.util.Queue;
public class QueueDemo {
    public static void main(String[] args) {
        Deque<String> tasks = new ArrayDeque<>();
        tasks.addLast("first"); tasks.addLast("second");
        System.out.println(tasks.removeFirst());
        tasks.push("urgent");
        System.out.println(tasks.pop());
        Queue<Integer> priority = new PriorityQueue<>();
        priority.offer(30); priority.offer(10); priority.offer(20);
        while (!priority.isEmpty()) System.out.println(priority.poll());
    }
}
''','first\nurgent\n10\n20\n30',['addLast/removeFirst uses opposite ends for FIFO; push/pop uses the same end for LIFO.','Repeated poll follows priority order; the queue iterator makes no such promise.'])

# 11
x=lesson('Sets, Maps & Natural Ordering','Define identity, choose an order, and index data by a stable key.', ['Keep equals and hashCode consistent','Compare HashSet, LinkedHashSet and TreeSet','Implement Comparable correctly','Choose a Map contract and traverse its entries'])
section(x,'Hashing narrows the search; equality confirms it','A hash-based collection uses hashCode() to choose a candidate region, then equals() to determine whether the key or element matches. A collision occurs when different objects share a hash value; collisions are legal. Equal objects must have equal hash codes, but equal hash codes do not prove equality.','For a custom Student, decide what defines identity. If ID defines equality, both equals() and hashCode() must use that rule. Do not mutate equality-relevant fields while an object is stored in a hash set or used as a map key. The bucket selected during insertion may no longer match the new hash.')
section(x,'Three Set implementations, three ordering promises','HashSet rejects duplicates using equality and offers no iteration-order guarantee. LinkedHashSet also uses equality but preserves insertion order. TreeSet uses comparison to maintain order, and regards elements that compare as zero as equivalent for set membership.','A TreeSet of students ordered only by score may retain just one of two different students sharing that score. Add a tie-breaker when those students must both be stored. Keep natural ordering consistent with equals where possible so the sorted set also satisfies ordinary Set expectations.')
section(x,'Comparable defines the type’s natural order','Comparable<T> declares compareTo(T other). Return a negative value when this comes before other, zero when they are equivalent in ordering, and a positive value when this comes after other. The magnitude is unimportant. The ordering must be transitive and its sign must reverse when arguments are swapped.','Use Integer.compare or an appropriate comparison method instead of subtracting integers, because subtraction can overflow. A natural order belongs to the type. Alternate caller-selected orders will be expressed with Comparator in the next lesson.')
reuse(x,'maps-ordering-utilities',2,3)
section(x,'Map keys are unique; values need not be','put(key, value) inserts an association or replaces the value for an equal key. get(key) returns the associated value or null if none is mapped; in maps permitting null values, containsKey distinguishes absence from a present null mapping. remove(key) deletes the association.','keySet(), values() and entrySet() are backed views, not independent snapshots. Removing through a supported view removes the corresponding mapping. Traverse entrySet when both key and value are needed. A Map is not directly Iterable, but its views are collections that can be traversed.')
section(x,'Choose lookup and order independently','HashMap provides no iteration-order guarantee. LinkedHashMap preserves insertion order by default and can optionally maintain access order. TreeMap stores keys in comparison order and supports sorted-range operations. Null handling differs between implementations; do not assume that all Map implementations accept a null key.','Expected constant-time hash lookup assumes a suitable hash distribution. TreeMap operations such as get and put are logarithmic in entry count. These performance models help choose a starting point; actual workload and memory behavior still matter.')
section(x,'An access-ordered map can express a bounded cache','In access-order mode, successful access operations update encounter order. Overriding removeEldestEntry can evict the eldest entry when insertion grows the map beyond a limit. With insertion order instead, the policy evicts the oldest insertion rather than the least recently accessed entry.','This is a small local cache demonstration, not a complete concurrent cache design. Ordinary LinkedHashMap operations are not automatically thread-safe. Keep the cache’s ordering policy separate from the equality rule used to find keys.')
visual(x,'maps-ordering-utilities',0,1)
flow(x,'Hash lookup uses two different tests',[('Key object','A stable identity rule'),('hashCode()','Find candidate bucket'),('equals()','Confirm the matching key'),('Result','Read or replace its value')])
demo(x,'SetDemo','Make logical equality agree with hashing','''
import java.util.HashSet;
import java.util.Set;
public class SetDemo {
    static class Student {
        private final int id;
        private final String name;
        Student(int id, String name) { this.id = id; this.name = name; }
        @Override public boolean equals(Object other) {
            if (this == other) return true;
            if (!(other instanceof Student)) return false;
            Student student = (Student) other;
            return id == student.id;
        }
        @Override public int hashCode() { return Integer.hashCode(id); }
    }
    public static void main(String[] args) {
        Set<Student> students = new HashSet<>();
        System.out.println(students.add(new Student(7, "Ada")));
        System.out.println(students.add(new Student(7, "Ada updated")));
        System.out.println(students.size());
    }
}
''','true\nfalse\n1',['This model defines identity only by ID, so a different name does not create a new set element.','The final ID cannot change after insertion. For extensible equality models, also consider inheritance and symmetry.'])
demo(x,'NaturalOrderDemo','Keep TreeSet ordering and equality aligned','''
import java.util.Set;
import java.util.TreeSet;
public class NaturalOrderDemo {
    static final class Ticket implements Comparable<Ticket> {
        private final int number;
        Ticket(int number) { this.number = number; }
        public int compareTo(Ticket other) { return Integer.compare(number, other.number); }
        @Override public boolean equals(Object other) {
            return other instanceof Ticket && number == ((Ticket) other).number;
        }
        @Override public int hashCode() { return Integer.hashCode(number); }
        @Override public String toString() { return "T" + number; }
    }
    public static void main(String[] args) {
        Set<Ticket> tickets = new TreeSet<>();
        tickets.add(new Ticket(3)); tickets.add(new Ticket(1));
        tickets.add(new Ticket(3));
        System.out.println(tickets);
    }
}
''','[T1, T3]',['compareTo returns zero for the same ticket number, matching equals.','TreeSet orders on insertion, so a separate sort call is unnecessary.'])
demo(x,'MapDemo','Insertion order and key order answer different questions','''
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.TreeMap;
public class MapDemo {
    public static void main(String[] args) {
        Map<Integer, String> insertion = new LinkedHashMap<>();
        insertion.put(3, "Grace"); insertion.put(1, "Ada");
        insertion.put(3, "Grace Hopper");
        System.out.println(insertion);
        Map<Integer, String> sorted = new TreeMap<>(insertion);
        for (Map.Entry<Integer, String> entry : sorted.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }
    }
}
''','{3=Grace Hopper, 1=Ada}\n1 -> Ada\n3 -> Grace Hopper',['Replacing key 3 updates its value without adding a second key.','TreeMap gives the same associations a different iteration order by sorting keys.'])

# 12
x=lesson('Sorting, Functional Interfaces & Streams','Express a data transformation as a clear sequence with an explicit result.', ['Compose natural and alternate sorting rules','Use four standard functional interfaces','Build and explain a lazy stream pipeline','Choose terminal operations and avoid shared side effects'])
reuse(x,'maps-ordering-utilities',4)
section(x,'Arrays and Collections are utility classes','Arrays contains static helpers for arrays, including sorting, searching, copying and comparison. Collections contains static algorithms and wrappers for collection objects. Collection is the element-container interface; Collections is a different plural-named utility class.','Arrays.sort changes an array in place. Collections.sort(list) and list.sort(comparator) change a mutable list in place. Binary search requires data sorted under the same ordering used by the search. Arrays.asList returns a fixed-size list backed by its array; new ArrayList<>(...) creates a resizable copy.')
section(x,'Comparator supplies an external ordering strategy','Comparator<T> declares compare(left, right), allowing a caller to choose an order without changing the element class. Comparator.comparingInt and comparing extract a sort key; reversed reverses an order and thenComparing resolves ties. Comparable defines one natural order; Comparator can express many alternatives.','Apply reversed at the intended level. comparingInt(score).reversed().thenComparing(name) sorts by descending score and ascending name. Reversing the entire composed comparator would reverse both rules. A tie-breaker makes output deterministic when primary values match.')
reuse(x,'lambda-stream-api',0)
section(x,'Four interfaces represent four common shapes','Predicate<T> takes T and returns boolean through test. Consumer<T> accepts T and performs an action through accept, returning no value. Function<T,R> transforms T to R through apply. Supplier<T> takes no argument and produces T through get. These shapes describe the contract independently of a lambda’s variable names.','Predicates combine with and, or and negate. Functions compose with andThen or compose, whose execution orders differ. A Supplier can delay an expensive fallback until it is required. Creating a lambda usually does not perform the action; calling its interface method does.')
reuse(x,'lambda-stream-api',2)
section(x,'Intermediate operations describe a new stream','filter keeps elements matching a predicate. map transforms each element. flatMap flattens a stream of streams. distinct removes duplicates according to equality; sorted orders elements; limit bounds the result. These operations return streams rather than immediately producing a final container.','A pipeline usually pulls each element through the necessary operations instead of completing a full separate traversal for every stage. Stateful operations such as sorted may need to buffer data. A terminal operation can short-circuit: anyMatch may stop at the first match, but sorting before it can still require consuming all input.')
section(x,'Choose the terminal result deliberately','count produces a number; anyMatch and allMatch produce booleans; findFirst produces an Optional because no result may exist. collect accumulates results, and reduce combines values with an operation such as addition. For numeric data, mapToInt followed by sum or average avoids repeatedly boxing primitive values.','Stream.toList() produces an unmodifiable list in the Java 21 examples. If later mutation is required, collect with Collectors.toCollection(ArrayList::new). Do not assume Collectors.toList() guarantees a specific mutable implementation. Optional.orElseGet uses a Supplier only when the result is absent.')
reuse(x,'lambda-stream-api',3)
section(x,'Performance follows the work, not the syntax','A sequential stream can be clear without being faster than a loop. Parallel pipelines need enough independent work to outweigh splitting and coordination. Reduction operations must be associative and have suitable identity values. Side effects on an ordinary shared ArrayList are unsafe in a parallel forEach.','Prefer a collector that manages the reduction rather than external mutation. Encounter order and execution order are different: parallel forEach does not promise encounter-order output, while forEachOrdered preserves it where defined. Measure a representative workload before choosing parallel execution.')
section(x,'Build a report from explicit stages','Start with typed records in a list, filter the records that belong in the report, sort with a visible comparator, map each record to the requested representation, and collect the result. Each stage should answer one question that can be stated in a sentence.','Keep storage, validation and presentation separate. A stream reads from the collection; it does not automatically validate domain rules or persist records. The final demonstration uses ordinary classes, a Map index and Stream reporting to connect the concepts from previous lessons without adding a new framework.')
visual(x,'maps-ordering-utilities',2);visual(x,'lambda-stream-api',0,1)
flow(x,'Trace one reporting pipeline',[('Source','85, 42, 90, 68'),('filter ≥ 60','85, 90, 68'),('sorted','68, 85, 90'),('map to label','Pass: 68, Pass: 85, Pass: 90'),('toList','An unmodifiable result list')])
demo(x,'SortingDemo','Compose an order without changing the class','''
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
public class SortingDemo {
    static class Student {
        private final String name;
        private final int score;
        Student(String name, int score) { this.name = name; this.score = score; }
        String name() { return name; }
        int score() { return score; }
        @Override public String toString() { return name + ":" + score; }
    }
    public static void main(String[] args) {
        int[] numbers = {3, 1, 2};
        Arrays.sort(numbers);
        System.out.println(Arrays.toString(numbers));
        List<String> names = new ArrayList<>(Arrays.asList("Grace", "Ada"));
        Collections.sort(names);
        System.out.println(names);
        List<Student> students = new ArrayList<>();
        students.add(new Student("Grace", 90));
        students.add(new Student("Ada", 90));
        students.add(new Student("Linus", 80));
        students.sort(Comparator.comparingInt(Student::score).reversed()
                                .thenComparing(Student::name));
        System.out.println(students);
    }
}
''','[1, 2, 3]\n[Ada, Grace]\n[Ada:90, Grace:90, Linus:80]',['Arrays.sort handles the array; Collections.sort uses String natural ordering for the list.','Student has no Comparable requirement here because the caller provides an explicit Comparator.'])
demo(x,'FunctionsDemo','Test, transform, act and supply','''
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;
public class FunctionsDemo {
    public static void main(String[] args) {
        Predicate<String> nonBlank = text -> !text.isBlank();
        Function<String, String> normalize = text -> text.trim().toUpperCase(java.util.Locale.ROOT);
        Consumer<String> display = System.out::println;
        Supplier<String> fallback = () -> "UNKNOWN";
        String value = " Ada ";
        display.accept(nonBlank.test(value) ? normalize.apply(value) : fallback.get());
        display.accept(fallback.get());
    }
}
''','ADA\nUNKNOWN',['Each variable names behavior with one of the four standard input/output shapes.','The first fallback is not evaluated because the predicate accepts the supplied value.'])
demo(x,'StreamDemo','A lazy pipeline becomes a result','''
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;
public class StreamDemo {
    public static void main(String[] args) {
        List<Integer> scores = List.of(85, 42, 90, 68);
        Stream<Integer> passing = scores.stream().filter(score -> {
            System.out.println("Testing " + score);
            return score >= 60;
        });
        System.out.println("Pipeline created");
        List<Integer> result = passing.sorted().toList();
        System.out.println(result);
        int total = scores.stream().mapToInt(Integer::intValue).sum();
        System.out.println("Total: " + total);
        List<String> labels = scores.stream().filter(score -> score >= 60)
            .sorted().map(score -> "Pass: " + score)
            .collect(Collectors.toCollection(ArrayList::new));
        labels.add("Report complete");
        System.out.println(labels);
    }
}
''','Pipeline created\nTesting 85\nTesting 42\nTesting 90\nTesting 68\n[68, 85, 90]\nTotal: 285\n[Pass: 68, Pass: 85, Pass: 90, Report complete]',['The diagnostic prints occur only after the terminal toList() starts traversal. Logging inside filter is for this trace only, not a reliable production side-effect protocol.','passing is consumed once; each later calculation starts a fresh stream.','The first result is unmodifiable; the labels collector explicitly requests a mutable ArrayList.'])
demo(x,'ReportDemo','Connect a Map index with a Stream report','''
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
public class ReportDemo {
    static class Student {
        private final String name;
        private final int score;
        Student(String name, int score) { this.name = name; this.score = score; }
        String name() { return name; }
        int score() { return score; }
    }
    public static void main(String[] args) {
        Map<Integer, Student> byId = new LinkedHashMap<>();
        byId.put(1, new Student("Ada", 92));
        byId.put(2, new Student("Grace", 85));
        byId.put(3, new Student("Linus", 45));
        List<String> report = byId.values().stream()
            .filter(student -> student.score() >= 60)
            .sorted(Comparator.comparingInt(Student::score).reversed())
            .map(student -> student.name() + " = " + student.score())
            .toList();
        report.forEach(System.out::println);
        String first = report.stream().findFirst().orElseGet(() -> "No passing students");
        System.out.println("Top: " + first);
        int sum = byId.values().stream().map(Student::score).reduce(0, Integer::sum);
        System.out.println("Total: " + sum);
    }
}
''','Ada = 92\nGrace = 85\nTop: Ada = 92\nTotal: 222',['The Map stores the records; the pipeline builds a separate report without changing stored scores.','A comparator sorts the objects before map transforms them into display strings.','findFirst handles an empty report with a Supplier fallback, while reduce combines scores using an associative addition operation.'])

# Keep demonstrations directly after the concepts they use.
LESSONS[0]['sections'][3]['paragraphs'][1]='Import java.util.Scanner, create a Scanner with new Scanner(System.in), then call its reading methods. In the demonstration, the scanner validates an integer age and then reads a full name. The two reads deliberately use different input units: a token for the age and a line for the name.'
LESSONS[6]['demos'][1],LESSONS[6]['demos'][2]=LESSONS[6]['demos'][2],LESSONS[6]['demos'][1]
placements=[[7,9,10],[4,5,7],[2,3,5],[2,6,7],[3,6,8],[3,6,8],[5,7,10],[6,8,9],[3,4,6],[2,4,6,8],[1,3,7],[3,5,10,11]]
for l,positions in zip(LESSONS,placements):
 for d,p in zip(l['demos'],positions):d['after']=p
# Early examples use ordinary top-level helper classes; nesting is introduced in lesson 4.
import re
for l in LESSONS[:3]:
 for d in l['demos']:
  code=d['code'];helpers=[]
  while True:
   match=re.search(r'^    (?:(abstract) )?static class \w+[^\n]*\{',code,re.M)
   if not match:break
   start=match.start();brace=code.index('{',match.start());depth=1;end=brace+1
   while depth:
    if code[end]=='{':depth+=1
    elif code[end]=='}':depth-=1
    end+=1
   block=textwrap.dedent(code[start:end]).replace('static class ','class ',1)
   helpers.append(block)
   code=code[:start]+code[end:].lstrip('\n')
  if helpers:d['code']='\n\n'.join(helpers)+'\n\n'+code

# Restore the complete program-skeleton lesson, including its original visual walkthrough.
skeleton_html=json.loads((Path(__file__).parent/'program-templates.json').read_text())['skeleton']
skeleton=dict(BASE['STUDY_CHAPTERS']['java-platform-ide']['sections'][1])
skeleton['html']=skeleton_html
main_section=LESSONS[0]['sections'][1]
LESSONS[0]['sections'][1]=skeleton
LESSONS[0]['sections'][2]=main_section

# Beginner commands, data representation and input demonstrations.
first=LESSONS[0]
first['sections'][1]['html']=first['sections'][1]['html'].replace('java -cp . First','java First').replace('<code>-cp .</code> searches the current folder; ','').replace('With the default classpath, <code>java First</code> also works. These are terminal commands; they do not go inside the Java file.','Run these commands from the folder containing First.java and First.class. These are terminal commands; they do not go inside the Java file.')
section(first,'Java data types: Primitive and Reference',
'Primitive variables hold simple values. Reference variables hold references to objects, or null. The diagram below shows the two groups.')
section(first,'Java memory: Method Area, Stack and Heap',
'For a local declaration such as Student s = new Student(), s holds a reference in the current method’s stack frame; the new Student object belongs to the heap. The method area holds class information and method code.')
new_sections=first['sections'][-2:];del first['sections'][-2:];first['sections'][9:9]=new_sections
for d in first['demos']:
 if d['after']>=10:d['after']+=2
first['goals'].extend(['Distinguish primitive values from reference values','Trace local variables, stack frames and heap objects'])
first['sections'][3]['paragraphs'][1]='Import java.util.Scanner, create a Scanner with new Scanner(System.in), then call its reading methods. Begin by reading two integers and adding them. A second example reads a full name with nextLine(). Input validation and the newline trap follow after these simple examples.'
demo(first,'KeyboardSum','Read two integers and display their sum','''
import java.util.Scanner;
public class KeyboardSum {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int a, b, c;
        System.out.println("Enter 2 numbers:");
        a = s.nextInt();
        b = s.nextInt();
        c = a + b;
        System.out.println("Sum is " + c);
    }
}
''','Enter 2 numbers:\nSum is 25',['System.in supplies standard input, normally the keyboard. Scanner converts its text into typed values.','Each nextInt() reads one integer token. Entering 10 15 on one line or on separate lines works.','java.lang is imported automatically, so no explicit import java.lang.* is required. This first example assumes valid integers.'],stdin='10 15\n');first['demos'][-1]['after']=4

demo(first,'ReadName','Read a full name with nextLine()','''
import java.util.Scanner;
public class ReadName {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        String name;
        System.out.println("May I know your name?");
        name = s.nextLine();
        System.out.println("Welcome Mr./Miss " + name);
    }
}
''','May I know your name?\nWelcome Mr./Miss Ada Lovelace',['nextLine() reads the whole line, including the space between Ada and Lovelace. next() would read only Ada.','There is no preceding token read in this separate program, so no extra nextLine() is needed to consume a pending newline.'],stdin='Ada Lovelace\n');first['demos'][-1]['after']=5

demo(first,'StringScanner','Scanner can also parse an existing string','''
import java.util.Scanner;
public class StringScanner {
    public static void main(String[] args) {
        Scanner s = new Scanner("10 20 30");
        int a = s.nextInt();
        int b = s.nextInt();
        int c = s.nextInt();
        System.out.println(a + b + c);
        s.close();
    }
}
''','60',['This Scanner reads the supplied String; it does not wait for keyboard input.','The same nextInt() operation works because Scanner separates parsing from the choice of input source. Closing this scanner does not close System.in.']);first['demos'][-1]['after']=5

demo(first,'ValueAndReferenceDemo','Copy a value; share an array object','''
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
''','copy = 9\ncount = 2\nvalues[0] = 99\nsame array = true',['copy receives its own primitive value. Changing it leaves count unchanged.','alias receives a copy of the array reference. Both references reach the same array, so updating alias[0] is visible through values[0].','The memory diagram shows these locals in the main frame and the single array object on the heap.']);first['demos'][-1]['after']=11
first['demos'].sort(key=lambda d:d['after'])

# Combine the program structure and execution explanation into one concept.
first = LESSONS[0]
assert first['sections'][2]['title'] == 'The main method and program boundaries'
del first['sections'][2]
for d in first['demos']:
    if d['after'] >= 3:
        d['after'] -= 1
for v, position in zip(first['visuals'], [2, 4, 5, 11]):
    v['after'] = position
program_flow = first['visuals'][0]
for item in program_flow['items']:
    item['label'] = item['label'].replace('HelloJava', 'First')

# Put data types immediately after the program skeleton, retaining attached material.
previous_sections = list(first['sections'])
types_index = next(i for i, s in enumerate(previous_sections)
                   if s['title'] == 'Java data types: Primitive and Reference')
first['sections'].insert(2, first['sections'].pop(types_index))
LESSON_ONE_SECTION_POSITIONS = {
    old_position: next(i for i, current in enumerate(first['sections'], 1)
                       if current is section)
    for old_position, section in enumerate(previous_sections, 1)
}
for attachment in first['demos'] + first['visuals']:
    attachment['after'] = LESSON_ONE_SECTION_POSITIONS[attachment['after']]
first['demos'].sort(key=lambda d: d['after'])

for diagram in first['visuals']:
    if diagram['title'] == 'A validation loop must always move forward':
        diagram['kind'] = 'scanner-validation'

# Teach Scanner as four connected questions, with examples attached to each.
from scanner_unit import reorganize
reorganize(first, demo)

# Five opening parts; Scanner retains four unnumbered topic headings.
original_first = list(first['sections'])
scanner_topics = original_first[3:7]
for topic in scanner_topics:
    topic['title'] = topic['title'].removeprefix('Scanner: ')
    topic['title'] = topic['title'][0].upper() + topic['title'][1:]
first['sections'] = original_first[:3] + [original_first[8], dict(
    title='Scanner: sources, keyboard input, validation and consumption',
    paragraphs=[], subsections=scanner_topics)]
first['title']='Java Foundations, Data Types & Scanner'
first['subtitle']='Understand how Java runs, where values live, and how to read input clearly.'
first['goals']=['Explain source → bytecode → JVM', 'Read the structure of a Java program',
                'Distinguish primitive values from reference values',
                'Relate local variables and objects to stack and heap',
                'Read, validate and consume input with Scanner']
second=LESSONS[1]
second['sections'].insert(0,original_first[9])
second['sections'].insert(4,original_first[7])
second['title']='Objects, Methods, Encapsulation & Inheritance'
second['goals'][:0]=['Distinguish classes, objects and references', 'Choose an overloaded method by its parameters']
SECOND_SECTION_POSITIONS={i:i+1 if i<4 else i+2 for i in range(1,8)}
for d in second['demos']:d['after']=SECOND_SECTION_POSITIONS[d['after']]
# Preserve the existing every-third-section visual placements after inserting topics.
for v,position in zip(second['visuals'],[3,6]+[7]*len(second['visuals'])):
    v['after']=SECOND_SECTION_POSITIONS[position]
for d in list(first['demos']):
    if d['name'] in ('ObjectDemo','OverloadDemo'):
        first['demos'].remove(d)
        d['after']=1 if d['name']=='ObjectDemo' else 5
        second['demos'].append(d)
    elif d['after']==9:d['after']=4
    else:
        d['subpart']=d['after']-3
        d['after']=5
for v in list(first['visuals']):
    if v['after']==10:
        first['visuals'].remove(v);v['after']=1;second['visuals'].append(v)
    elif v['kind']=='scanner-validation':
        first['visuals'].remove(v);scanner_topics[2]['visuals']=[v]
first['demos'].sort(key=lambda d:(d['after'],d.get('subpart',0)))
second['demos'].sort(key=lambda d:d['after'])

second["sections"][0]["paragraphs"] = [p.replace("the next lesson will protect state with encapsulation", "the following sections protect state with encapsulation") for p in second["sections"][0]["paragraphs"]]

# Clarify the opening explanations without expanding the five-part structure.
first['sections'][0]['paragraphs'].insert(1,
    'The Java Runtime Environment, or JRE, provides what a Java program needs to run: the JVM, standard libraries and supporting runtime components. The JDK includes these runtime components as well as development tools such as javac; a runtime alone does not provide that compiler.')
for v in first['visuals']:
    if v['title']=='From source file to running program':v['after']=1
skeleton=first['sections'][1]
skeleton['lead']='In the Java 21 programs in this course, methods and executable statements belong inside a class; statements such as printing or reading input go inside a method.'
skeleton['paragraphs']=['A .java source file can contain more than one class, as well as package and import declarations outside the classes. For this first program, use one public class named First and save it as First.java. Java also has other type declarations, such as interfaces; not every source file must declare a class.']
skeleton['html']=re.sub(r'<aside class="skeleton-args">[\s\S]*?</aside>', '''<aside class="skeleton-args"><strong>What does String[] args mean?</strong><p><code>args</code> is a list (an array) of text values supplied when you launch the program. In the terminal command below, <code>First</code> is the class to run; the words after it become the arguments.</p><p><code>java First Candice 2026</code></p><p><code>args[0]</code> is <code>"Candice"</code> and <code>args[1]</code> is <code>"2026"</code>. Array positions start at 0, and even <code>2026</code> arrives as text.</p><p>The Hello World program above never uses <code>args</code>, so those extra words do not change its output. A statement such as <code>System.out.println(args[0]);</code> would print <code>Candice</code> for this command.</p></aside>''',skeleton['html'])
skeleton['note']='Names must match exactly: First and first are different names. Because the declaration is public class First, save the file as First.java. String and System are standard Java types in java.lang, which is available automatically; Scanner belongs to java.util, so it needs import java.util.Scanner.'
first['sections'][2]['paragraphs']=[
    'Java variables come in two kinds. A primitive variable holds the value itself: after int x = 10;, x stores 10. A reference variable holds a reference to an object: after String s = new String("hi");, s holds a reference to that String object — or it could hold null, meaning "no object." Think of a reference as a way to locate an object on the heap, rather than an address you can inspect or manipulate in Java.',
    'Assigning a primitive copies the value, while assigning a reference copies the reference. Two references to the same mutable object see changes made to that object through either reference. String objects are immutable, so use the array example in the next part to see shared changes.'
]

first["sections"][2]["emphasis"] = ["A primitive variable holds the value itself", "A reference variable holds a reference to an object"]

first["sections"][2]["emphasis"].append("String objects are immutable, so use the array example in the next part to see shared changes.")

from lesson_two import rewrite as rewrite_lesson_two
rewrite_lesson_two(LESSONS[1], demo)

from lesson_three import rewrite as rewrite_lesson_three
rewrite_lesson_three(LESSONS[2], demo)
