"""Lesson 2: overloads, OOP concepts, then the class-design sequence."""
from html import escape


def rewrite(lesson, demo):
    lesson.update(title='Method Overloading & Object-Oriented Programming',
        subtitle='Choose a method by its parameters, then design objects with state and useful operations.',
        goals=['Write overloaded methods with different parameter lists',
               'Explain abstraction, encapsulation, inheritance and polymorphism',
               'Turn properties and operations into fields and methods',
               'Control access with getters and setters',
               'Initialize objects with overloaded constructors',
               'Create and use an array of object references'],
        sections=[], visuals=[], demos=[])

    def topic(parent, title, *paragraphs, note=None):
        t=dict(title=title,paragraphs=list(paragraphs))
        if note:t['note']=note
        parent['subsections'].append(t)
        return t

    def grid(t,title,columns,rows):
        t.setdefault('visuals',[]).append(dict(kind='table',title=title,columns=columns,rows=rows))

    def example(part,sub,name,title,code,output,*explain):
        demo(lesson,name,title,code,output,list(explain))
        lesson['demos'][-1].update(after=part,subpart=sub,output_in_comments=True)

    overload=dict(title='Method Overloading',paragraphs=[
        'Overloading lets several methods share one name when their parameter lists are different. Start with what a method receives and what it returns, then compare the calls.'],subsections=[])
    oop=dict(title='Object-Oriented Programming',paragraphs=[
        'Object-oriented programming organizes a program around objects. An object combines state (fields) with behavior (methods). The four principles guide how we expose, protect and reuse that behavior.'],subsections=[])
    lesson['sections']=[overload,oop]
    t=topic(overload,'One name, different parameter lists',
        'In int max(int x, int y), int before max is the return type; x and y are parameters. In max(10, 15), 10 and 15 are arguments. return sends the result back to the caller.',
        'Overloaded methods have the same name but different parameter types, numbers of parameters, or orders of types. Changing only a parameter name or the return type does not create a new overload.',
        'For these ordinary calls, the compiler chooses an overload from the declared argument types. The helpers below are static so main can call them without first creating an object.')
    grid(t,'Which max method is selected?', ['Call','Parameter list','Result'],[
        ['max(10, 15)','int, int','15'],['max(5.5f, 7.5f)','float, float','7.5'],['max(8, 10, 3)','int, int, int','10']])
    example(1,1,'OverloadDemo','Same operation, three parameter lists','''
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
''','15\n7.5\n10','The f suffix makes 5.5f and 7.5f float literals. Without f they are double, and these overloads do not accept double arguments.',
        'Java can widen some argument types when needed, such as byte to int. It does not automatically narrow an int argument to byte.',
        'Try adding float max(int x, int y): it fails because max(int, int) already exists. Return type alone cannot distinguish the calls.')
    topic(overload,'Practice: area, reverse and validate',
        'Use one method name for one idea. area can take a radius or a length and breadth. reverse can receive one integer or an int array. validate can receive a name or an age.',
        'The parameter list must tell the methods apart. area(double length, double breadth) and area(double base, double height) would have the same signature; changing the words does not distinguish them.')
    example(1,2,'AreaOverloadDemo','Change the number of parameters','''
public class AreaOverloadDemo {
    static double area(double radius) {
        return Math.PI * radius * radius;
    }
    static double area(double length, double breadth) {
        return length * breadth;
    }
    static double area(double a, double b, double height) {
        return (a + b) * height / 2;
    }
    public static void main(String[] args) {
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", area(2)); // 12.57
        System.out.println(area(4, 3));       // 12.0: rectangle
        System.out.println(area(4, 6, 3));    // 15.0: trapezium
    }
}
''','12.57\n12.0\n15.0','One, two and three arguments select different area methods. These int literals can widen to the double parameters.')
    example(1,2,'ReverseOverloadDemo','An integer and an array are different parameter types','''
import java.util.Arrays;
public class ReverseOverloadDemo {
    static int reverse(int number) {
        int result = 0;
        while (number > 0) {
            result = result * 10 + number % 10;
            number = number / 10;
        }
        return result;
    }
    static int[] reverse(int[] values) {
        int[] result = new int[values.length];
        for (int i = 0; i < values.length; i++) {
            result[i] = values[values.length - 1 - i];
        }
        return result;
    }
    public static void main(String[] args) {
        System.out.println(reverse(237)); // 732
        int[] values = {2, 3, 7};
        System.out.println(Arrays.toString(reverse(values))); // [7, 3, 2]
        System.out.println(Arrays.toString(values));          // [2, 3, 7]
    }
}
''','732\n[7, 3, 2]\n[2, 3, 7]',
        'reverse(int) builds a reversed number; this small exercise assumes a non-negative integer whose reverse fits in int.',
        'reverse(int[]) creates a new array, so the original array stays unchanged. Arrays.toString displays its elements.')
    example(1,2,'ValidateOverloadDemo','The argument type chooses the validation rule','''
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
''','true\nfalse\ntrue\nfalse',
        'The name rule only checks that name is not null and is not the empty string "". isEmpty() checks for an empty string; ! means not. If name is null, && skips the second check.',
        'The age rule is the exercise’s chosen range, 3–15 inclusive. Both methods return boolean; String versus int makes the overloads different.')

    t=topic(oop,'The four OOP principles',
        'Abstraction exposes the useful operations without making the caller manage the internal steps. A television offers turnOn(); its user does not need to operate the circuitry.',
        'Encapsulation keeps related data and methods together and controls access to the data. A private volume field can be changed through a method that checks the allowed range.',
        'Inheritance lets a more specific class build on a more general class. Television extends Device means a television is a kind of device.',
        'Polymorphism lets the same operation use different implementations. A Device reference can call turnOn(), and a Television object can supply the television-specific behavior.',
        'Overloading is often called compile-time polymorphism. Overriding uses the actual object at runtime. Keep these two selection rules separate; later lessons develop overriding and inheritance in detail.')
    grid(t,'Four principles, four questions',['Principle','Question','In the example'],[
        ['Abstraction','What can the caller do?','Call turnOn() without knowing how the device works.'],
        ['Encapsulation','How is state protected?','private volume; setVolume checks 0–100.'],
        ['Inheritance','What is a more specific kind?','Television extends Device.'],
        ['Polymorphism','Which implementation runs?','device.turnOn() calls Television.turnOn().']])
    example(2,1,'OopPrinciplesDemo','One small example of the four principles','''
class Device {
    public void turnOn() { System.out.println("Device on"); }
}
class Television extends Device {
    private int volume;
    public void setVolume(int value) {
        if (value >= 0 && value <= 100) volume = value;
    }
    public int getVolume() { return volume; }
    @Override
    public void turnOn() { System.out.println("TV on"); }
}
public class OopPrinciplesDemo {
    public static void main(String[] args) {
        Television tv = new Television();
        tv.setVolume(20);
        tv.setVolume(150); // rejected; volume stays 20
        System.out.println(tv.getVolume()); // 20
        Device device = tv;
        device.turnOn(); // TV on
    }
}
''','20\nTV on',
        'private prevents the separate application class from directly changing volume. Public methods form the object’s interface to callers.',
        'extends declares the parent class; @Override marks a replacement for an inherited method. device and tv refer to the same Television object.',
        'Abstraction is a design idea, not merely the abstract keyword. This example uses no abstract class.')
    t=topic(oop,'Class, object and reference: write a Circle',
        'A class defines a type. An object is an instance of that class. A reference variable identifies an object: in Circle first = new Circle(), Circle is the type, first is the variable, and new Circle() creates an object.',
        'To design a class, ask: what does it store, and what can it do? A Circle stores radius and calculates area and perimeter. Fields describe state; methods describe behavior.',
        'Each object has its own instance fields. An instance method such as first.area() uses the radius of first’s object. The first examples use public fields so you can see this relationship; data hiding follows.')
    example(2,2,'CircleDemo','One class, two objects, and an alias','''
class Circle {
    public double radius;
    public double area() { return Math.PI * radius * radius; }
    public double perimeter() { return 2 * Math.PI * radius; }
    public double circumference() { return perimeter(); }
}
public class CircleDemo {
    public static void main(String[] args) {
        Circle first = new Circle();
        Circle second = new Circle();
        first.radius = 2;
        second.radius = 5;
        Circle alias = first;
        alias.radius = 3;
        System.out.println(first.radius);  // 3.0: same object as alias
        System.out.println(second.radius); // 5.0: separate object
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", first.area()); // 28.27
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", first.circumference()); // 18.85
    }
}
''','3.0\n5.0\n28.27\n18.85',
        'There are two new expressions and two Circle objects. Assigning first to alias does not create a third object.',
        'Save this complete example as CircleDemo.java. Circle is a separate non-public helper class in the same file.')
    t=topic(oop,'Practice designing Rectangle, Cylinder and Student',
        'Choose fields first, then methods that use those fields. A method calculating a result should normally return it; main can decide how to display it.',
        'Use double for dimensions and int for whole-number marks. Use boolean for a yes/no question such as isSquare(). A Student grade can return a char such as A or B.')
    grid(t,'From properties to operations',['Class','Fields','Methods'],[
        ['Rectangle','length, breadth','area(), perimeter(), isSquare()'],
        ['Cylinder','radius, height','lidArea(), circumference(), surfaceArea(), volume()'],
        ['Student','rollNo, name, course, three marks','total(), average(), grade()']])
    example(2,3,'RectangleDemo','Fields supply the rectangle’s measurements','''
class Rectangle {
    public double length, breadth;
    public double area() { return length * breadth; }
    public double perimeter() { return 2 * (length + breadth); }
    public boolean isSquare() { return length == breadth; }
}
public class RectangleDemo {
    public static void main(String[] args) {
        Rectangle r = new Rectangle();
        r.length = 4;
        r.breadth = 3;
        System.out.println(r.area());      // 12.0
        System.out.println(r.perimeter()); // 14.0
        System.out.println(r.isSquare());  // false
    }
}
''','12.0\n14.0\nfalse','No dimensions are passed to area(): it reads the fields of the object used in r.area().')
    example(2,3,'CylinderDemo','Reuse calculations inside a class','''
class Cylinder {
    public double radius, height;
    public double lidArea() { return Math.PI * radius * radius; }
    public double circumference() { return 2 * Math.PI * radius; }
    public double surfaceArea() { return 2 * lidArea() + circumference() * height; }
    public double volume() { return lidArea() * height; }
}
public class CylinderDemo {
    public static void main(String[] args) {
        Cylinder c = new Cylinder();
        c.radius = 2;
        c.height = 3;
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", c.lidArea());     // 12.57
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", c.surfaceArea()); // 62.83
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", c.volume());      // 37.70
    }
}
''','12.57\n62.83\n37.70','Total surface area includes two circular ends plus the curved side. This Cylinder is an independent class; no inheritance is needed for this exercise.')
    example(2,3,'StudentDemo','A data object can calculate results','''
class Student {
    public String rollNo, name, course;
    public int m1, m2, m3;
    public int total() { return m1 + m2 + m3; }
    public double average() { return total() / 3.0; }
    public char grade() {
        if (average() >= 60) return 'A';
        return 'B';
    }
}
public class StudentDemo {
    public static void main(String[] args) {
        Student student = new Student();
        student.rollNo = "S01";
        student.name = "Ada";
        student.course = "Java";
        student.m1 = 70; student.m2 = 80; student.m3 = 90;
        System.out.println(student.total());   // 240
        System.out.println(student.average()); // 80.0
        System.out.println(student.grade());   // A
    }
}
''','240\n80.0\nA','Dividing by 3.0 preserves a fractional average. The A/B rule is just this exercise’s grading policy.')
    topic(oop,'Data hiding: private fields, public methods',
        'With public fields, a caller could assign a negative length. Make the fields private, then provide methods that decide which values may be stored. This is data hiding as part of encapsulation.',
        'A getter returns a value. A setter receives a value and updates the field. In this example, a negative dimension becomes zero, so callers cannot leave a negative value inside the rectangle.')
    example(2,4,'DataHidingDemo','Change a dimension through a setter','''
class Rectangle {
    private double length, breadth;
    public double getLength() { return length; }
    public double getBreadth() { return breadth; }
    public void setLength(double value) {
        if (value >= 0) length = value;
        else length = 0;
    }
    public void setBreadth(double value) {
        if (value >= 0) breadth = value;
        else breadth = 0;
    }
    public double area() { return length * breadth; }
}
public class DataHidingDemo {
    public static void main(String[] args) {
        Rectangle r = new Rectangle();
        r.setLength(4); r.setBreadth(3);
        System.out.println(r.area());      // 12.0
        r.setLength(-5);
        System.out.println(r.getLength()); // 0.0
        // r.length = -5; // not allowed: length is private
    }
}
''','12.0\n0.0','The setter implements the chosen rule. Another class design could reject invalid input instead; private alone does not perform validation.')
    t=topic(oop,'Properties: read-write, read-only and write-only',
        'A property describes the access a class offers to a value. A private field does not automatically need both a getter and a setter. Provide only the operations callers should have.',
        'Read-write means getter plus setter. Read-only means a getter without a public setter. Write-only means a setter without a public getter; internal methods may still use the value.')
    grid(t,'Choose access deliberately',['Property kind','Example','Public methods'],[
        ['Read-write','Rectangle length','getLength(), setLength(value)'],
        ['Read-only','Student roll number','getRollNo()'],
        ['Write-only','Input supplied to a producer','setData(value)']])
    example(2,5,'PropertyDemo','A getter or setter is a design choice','''
class Student {
    private String rollNo = "S01";
    private int mark;
    public String getRollNo() { return rollNo; } // no public setter
    public int getMark() { return mark; }
    public void setMark(int value) {
        if (value >= 0 && value <= 100) mark = value;
    }
}
class Producer {
    private int data;
    public void setData(int value) { data = value; } // no public getter
}
public class PropertyDemo {
    public static void main(String[] args) {
        Student s = new Student();
        s.setMark(85);
        System.out.println(s.getRollNo()); // S01
        System.out.println(s.getMark());   // 85
        Producer p = new Producer();
        p.setData(7); // supplies a value; the public API cannot read it back
    }
}
''','S01\n85','The fixed roll number keeps this example short. A constructor can accept a different roll number for each object, as the next examples demonstrate.')
    topic(oop,'Constructors: give an object its starting values',
        'A constructor runs when an object is created. It has the class name and no return type, not even void. new Rectangle(4, 3) creates an object and invokes the matching constructor.',
        'A no-argument constructor receives no values; a parameterized constructor receives values. Constructors can be overloaded using different parameter lists, just like methods.',
        'Java supplies a default no-argument constructor only when a class declares no constructor. If you write Rectangle(double length, double breadth), new Rectangle() needs an explicitly declared no-argument constructor.',
        'In this.length = length, this.length is the current object’s field and length is the parameter. this(...) calls another constructor in the same class; in Java 21 it must be the first constructor statement.')
    example(2,6,'ConstructorDemo','Create a default rectangle, a square or a rectangle','''
class Rectangle {
    private double length, breadth;
    public Rectangle() { this(1, 1); }
    public Rectangle(double side) { this(side, side); }
    public Rectangle(double length, double breadth) {
        this.length = Math.max(0, length);
        this.breadth = Math.max(0, breadth);
    }
    public double area() { return length * breadth; }
}
public class ConstructorDemo {
    public static void main(String[] args) {
        System.out.println(new Rectangle().area());     // 1.0
        System.out.println(new Rectangle(4).area());    // 16.0
        System.out.println(new Rectangle(4, 3).area());  // 12.0
        System.out.println(new Rectangle(-4, 3).area()); // 0.0
    }
}
''','1.0\n16.0\n12.0\n0.0','Math.max(0, value) changes a negative dimension to zero. All three constructors reach that initialization rule.')
    topic(oop,'Practice: complete a Cylinder, Product and Customer',
        'A complete small class needs suitable field types, deliberate public access, and constructors supplying the required starting values. Revisit Cylinder with private fields, getters, setters and overloaded constructors.',
        'For Product, keep item number and name read-only in this model; allow price and quantity to change. For Customer, require an ID and name at construction and allow address and phone to change.',
        'Use String for identifiers and phone numbers: they are labels, not quantities for arithmetic, and a phone may contain + or leading zeros. These access choices belong to this exercise’s model, not a rule that names can never change.')
    example(2,7,'CylinderConstructorDemo','Three ways to initialize a Cylinder','''
class Cylinder {
    private double radius, height;
    public Cylinder() { this(0, 0); }
    public Cylinder(double radius) { this(radius, 1); }
    public Cylinder(double radius, double height) {
        setRadius(radius); setHeight(height);
    }
    public double getRadius() { return radius; }
    public double getHeight() { return height; }
    public void setRadius(double value) { radius = Math.max(0, value); }
    public void setHeight(double value) { height = Math.max(0, value); }
    public double volume() { return Math.PI * radius * radius * height; }
}
public class CylinderConstructorDemo {
    public static void main(String[] args) {
        Cylinder c = new Cylinder(2, 3);
        System.out.println(new Cylinder().getHeight());  // 0.0
        System.out.println(new Cylinder(2).getHeight()); // 1.0
        System.out.println(c.getRadius());               // 2.0
        System.out.printf(java.util.Locale.ROOT, "%.2f%n", c.volume()); // 37.70
    }
}
''','0.0\n1.0\n2.0\n37.70','No arguments chooses radius 0 and height 0. One radius chooses height 1. Two arguments supply both dimensions.')
    example(2,7,'ProductCustomerDemo','Required identity, editable details','''
class Product {
    private final String itemNo, name;
    private double price;
    private int quantity;
    public Product(String itemNo, String name) { this(itemNo, name, 0, 0); }
    public Product(String itemNo, String name, double price, int quantity) {
        this.itemNo = itemNo; this.name = name;
        setPrice(price); setQuantity(quantity);
    }
    public String getItemNo() { return itemNo; }
    public String getName() { return name; }
    public double getPrice() { return price; }
    public int getQuantity() { return quantity; }
    public void setPrice(double value) { price = Math.max(0, value); }
    public void setQuantity(int value) { quantity = Math.max(0, value); }
}
class Customer {
    private final String customerId, name;
    private String address, phone;
    public Customer(String customerId, String name) {
        this(customerId, name, "", "");
    }
    public Customer(String customerId, String name, String address, String phone) {
        this.customerId = customerId; this.name = name;
        this.address = address; this.phone = phone;
    }
    public String getCustomerId() { return customerId; }
    public String getName() { return name; }
    public String getAddress() { return address; }
    public String getPhone() { return phone; }
    public void setAddress(String value) { address = value; }
    public void setPhone(String value) { phone = value; }
}
public class ProductCustomerDemo {
    public static void main(String[] args) {
        Product p = new Product("P01", "Notebook", 5, 10);
        p.setPrice(6);
        System.out.println(p.getItemNo() + ": " + p.getPrice()); // P01: 6.0
        Customer c = new Customer("C01", "Ada");
        c.setPhone("+1 0123");
        System.out.println(c.getName() + ": " + c.getPhone()); // Ada: +1 0123
    }
}
''','P01: 6.0\nAda: +1 0123','final means the identity fields are assigned once. No public setters are supplied for those fields.',
        'Neither class has a no-argument constructor: the caller must supply identity arguments. The short constructors delegate to the full ones.')
    topic(oop,'Arrays of objects: create the array, then each object',
        'new Subject[2] creates one array with two null reference slots. It does not create two Subject objects. Create each Subject separately and assign its reference into a slot before calling its methods.',
        'A Student can hold that Subject array as a field. This is a has-a relationship: a student has subjects; it does not extend Subject.',
        'The example finishes the design with a constructor, getters and setters. setSubjects(Subject... subjects) uses varargs: the caller can supply several Subject references, which the method receives as an array.')
    example(2,8,'ObjectArrayDemo','Give a student two separately created subjects','''
class Subject {
    private final String id, name;
    private int maxMarks, marks;
    public Subject(String id, String name, int maxMarks) {
        this.id = id; this.name = name;
        setMaxMarks(maxMarks);
    }
    public String getId() { return id; }
    public String getName() { return name; }
    public int getMaxMarks() { return maxMarks; }
    public int getMarks() { return marks; }
    public void setMaxMarks(int value) {
        maxMarks = Math.max(1, value);
        marks = Math.min(marks, maxMarks);
    }
    public void setMarks(int value) { marks = Math.max(0, Math.min(value, maxMarks)); }
    public boolean isQualified() { return marks >= maxMarks * 0.4; }
    @Override
    public String toString() { return id + " " + name + ": " + marks; }
}
class Student {
    private final String rollNo, name;
    private String department;
    private Subject[] subjects = new Subject[0];
    public Student(String rollNo, String name, String department) {
        this.rollNo = rollNo; this.name = name; this.department = department;
    }
    public String getRollNo() { return rollNo; }
    public String getName() { return name; }
    public String getDepartment() { return department; }
    public void setDepartment(String value) { department = value; }
    public Subject[] getSubjects() { return subjects; }
    public void setSubjects(Subject... subjects) { this.subjects = subjects; }
}
public class ObjectArrayDemo {
    public static void main(String[] args) {
        Subject[] subjects = new Subject[2];
        System.out.println(subjects[0] == null); // true
        subjects[0] = new Subject("S01", "Java", 100);
        subjects[1] = new Subject("S02", "Databases", 100);
        subjects[0].setMarks(80);
        subjects[1].setMarks(35);
        Student student = new Student("ST01", "Ada", "Computing");
        student.setSubjects(subjects[0], subjects[1]);
        for (Subject subject : student.getSubjects()) {
            System.out.println(subject); // S01 Java: 80, then S02 Databases: 35
        }
        System.out.println(subjects[0].isQualified()); // true
        System.out.println(subjects[1].isQualified()); // false
    }
}
''','true\nS01 Java: 80\nS02 Databases: 35\ntrue\nfalse',
        'The first print proves the difference between allocating an array and constructing its elements.',
        'println calls the subject’s toString() method. The qualification rule here is at least 40% of maxMarks.',
        'The getter exposes the array in this introductory example. Its elements still refer to the original Subject objects.')

    # Organize navigation by concepts; examples remain under their concepts.
    old = oop['subsections']
    old[1]['title'] = 'Class, object and reference'
    old[1]['paragraphs'].extend(old[2]['paragraphs'])
    old[1].setdefault('visuals', []).extend(old[2].get('visuals', []))
    old[3]['title'] = 'Data hiding and encapsulation'
    old[5]['title'] = 'Constructors and constructor overloading'
    old[7]['title'] = 'Arrays of objects'
    oop['subsections'] = [old[i] for i in [0, 1, 5, 3, 4, 7]]
    oop['paragraphs'] = ['Object-oriented programming organizes a program around objects, combining state (fields) with behavior (methods). Start with the four principles—abstraction, encapsulation, inheritance and polymorphism—then explore classes, constructors and objects through code.']
    mapping = {1:1, 2:2, 3:2, 4:4, 5:5, 6:3, 7:5, 8:6}
    for d in lesson['demos']:
        d['concept_example'] = True
        if d['after'] == 2:
            d['subpart'] = mapping[d['subpart']]
    lesson['demos'].sort(key=lambda d: (d['after'], d['subpart']))
    overload['subsections'][1]['title'] = 'Overloading with different parameter types and counts'
    lesson['expanded_toc'] = True

    from oop_diagram import diagram
    old[0]['html'] = diagram()
    old[0]['visuals'] = []
