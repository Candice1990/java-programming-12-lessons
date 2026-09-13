"""Four connected Scanner topics for lesson 1."""
from html import escape

SECTION_POSITIONS = {1:1, 2:2, 3:3, 4:4, 5:4, 6:6, 7:7, 8:6, 9:8, 10:9, 11:10}

def table(title, rows):
    return '<figure class="visual-card"><header><h3>'+title+'</h3></header><div class="visual-table-wrap"><table class="visual-table"><thead><tr><th>Input / result</th><th>Java expression</th><th>Meaning</th></tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+escape(c)+'</td>' for c in row)+'</tr>' for row in rows)+'</tbody></table></div></figure>'

def reorganize(first, demo):
    topics = [
        dict(title='Scanner: a reference type and its input sources', paragraphs=[
            'Scanner is a class, so Scanner is a reference type. In Scanner input = new Scanner(System.in), input holds a reference to a Scanner object; it does not hold the text or an integer. The object reads text from a source and its methods return values such as int, double, boolean or String.',
            'Choose the source when constructing the Scanner. Choose what to read when calling a method. A token is one piece of text separated by a delimiter; Scanner uses whitespace by default. For example, "10 20" contains two tokens. The same nextInt() method can read an integer from keyboard input, a file or an existing string.'
        ], html=table('One reader, different sources',[
            ['Keyboard / standard input','new Scanner(System.in)','Usually receives text typed in the terminal; standard input can also be redirected.'],
            ['Text file','new Scanner(new File("numbers.txt"))','Reads text stored in a file.'],
            ['Existing text','new Scanner("10 20")','Reads a String already in the program.'],
            ['Other text sources','new Scanner(inputStream)','Can read a supplied stream, such as one obtained from a network connection.']
        ]), note='The source provides text. nextInt() converts a token to int; next() returns token text; nextLine() returns line text. The Scanner itself remains an object.'),
        dict(title='Scanner: read keyboard input', paragraphs=[
            'Import java.util.Scanner, create one Scanner connected to System.in, and call a reading method for each value you expect. A keyboard read can wait until input is available. These first examples assume that the user enters the requested types.',
            'Spaces separate tokens and Enter ends a line; neither signals the end of input, so a keyboard loop using hasNext() may wait for more input.',
            'Token methods skip leading whitespace, so numbers may be separated by spaces or line breaks. next() reads one token; nextLine() reads the rest of a line, including spaces within it. Decimal examples below use Locale.ROOT so a decimal point is interpreted consistently.'
        ],html=table('Choose the result you need',[
            ['byte / short / int / long','nextByte() / nextShort() / nextInt() / nextLong()','An integer within the chosen type’s range.'],
            ['float / double','nextFloat() / nextDouble()','A floating-point number, such as 3.5.'],
            ['boolean','nextBoolean()','true or false, ignoring case; not yes/no or 1/0.'],
            ['String: one token','next()','Ada Lovelace → Ada; the next token is Lovelace.'],
            ['String: line remainder','nextLine()','Reads through the end of the current line; the returned String excludes the line separator.'],
            ['char','next().charAt(0)','No nextChar() method: read a token, then take its first character.'],
            ['BigInteger / BigDecimal','nextBigInteger() / nextBigDecimal()','Additional numeric reference types; not needed for these introductory examples.']
        ]),note='Use one shared keyboard Scanner. Closing it also closes System.in. A file Scanner owns a separate resource and should be closed.'),
        dict(title='Scanner: validate before reading', paragraphs=[
            'Validation means checking before you read. hasNextInt() asks: “Can the next token be read as an int?” It returns true or false, but leaves the token where it is.',
            'If the answer is true, use nextInt() to read the integer. If it is false, show a message instead. For example, 20 is an int; hello and 3.5 are not. Calling nextInt() on hello without checking would cause InputMismatchException.'
        ]),
        dict(title='Scanner: consume input and understand the nextLine() trap', emphasis=['Consume simply means read and move past input.'], paragraphs=[
            'Consume simply means read and move past input. hasNextInt() only checks; nextInt() reads an integer; next() reads one token as text.',
            'For hello 20, next() can read past hello so nextInt() can reach 20. The word hello is invalid as an int, but next() can still read it as a String. Repeating a check without reading would keep checking the same hello.'
        ],html=table('Check or read?',[
            ['hasNextInt()','Check the next token','Does not move past it.'],
            ['nextInt()','Read one integer token','Moves past the integer.'],
            ['next()','Read one token as text','Moves past that token, whether it is hello or 20.'],
            ['nextLine()','Read the rest of the current line','Moves past the line break; the returned text excludes that break.']
        ]))
    ]
    first['sections'][3:8] = topics
    scanner_names={'KeyboardSum','ReadName','StringScanner','InputDemo'}
    for d in first['demos']:
        d['after']=SECTION_POSITIONS[d['after']]
    first['demos']=[d for d in first['demos'] if d['name'] not in scanner_names]
    first['visuals']=[v for v in first['visuals'] if v['title']!='Choose a Scanner method by the shape of the input']
    for v in first['visuals']:v['after']=SECTION_POSITIONS[v['after']]
    def add(name,title,code,output,explain,after,**kwargs):
        demo(first,name,title,code,output,explain,**kwargs)
        first['demos'][-1]['after']=after
    add('StringScanner','Read the same values from a String and a file','''
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class StringScanner {
    public static void main(String[] args) throws FileNotFoundException {
        try (Scanner text = new Scanner("10 20")) {
            System.out.println("String sum: " + (text.nextInt() + text.nextInt()));
        }
        try (Scanner file = new Scanner(new File("numbers.txt"))) {
            System.out.println("File sum: " + (file.nextInt() + file.nextInt()));
        }
    }
}
''','String sum: 30\nFile sum: 30',[
        'text and file are reference variables pointing to separate Scanner objects. Both objects return int values through nextInt().',
        'Place numbers.txt beside the program and run from that folder. The only change to the reading operation is the source.',
        'try (...) closes each owned Scanner; throws declares the possible missing-file error. These resource and exception details are developed in lesson 6.'
    ],4,files={'numbers.txt':'10 20\n'})
    add('KeyboardSum','Keyboard input: read two integers','''
import java.util.Scanner;
public class KeyboardSum {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter two integers:");
        int first = input.nextInt();
        int second = input.nextInt();
        System.out.println("Sum: " + (first + second));
    }
}
''','Enter two integers:\nSum: 25',['Scanner input declares a reference; new Scanner(System.in) constructs the reader.','Each nextInt() returns one int. Enter 10 and 15 separated by a space or a line break.'],5,stdin='10 15\n')
    add('ReadName','Keyboard input: choose a method for each value','''
import java.util.Locale;
import java.util.Scanner;
public class ReadName {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in).useLocale(Locale.ROOT);
        System.out.println("Enter a full name:");
        String name = input.nextLine();
        System.out.println("Enter age, height, and enrolled (true/false):");
        int age = input.nextInt();
        double height = input.nextDouble();
        boolean enrolled = input.nextBoolean();
        System.out.println(name + " | " + age + " | " + height + " | " + enrolled);
    }
}
''','Enter a full name:\nEnter age, height, and enrolled (true/false):\nAda Lovelace | 20 | 1.65 | true',[
        'nextLine() reads the name including its space. It is the first read, so there is no leftover number line to finish.',
        'The following token methods return int, double and boolean. This example assumes valid input; validation comes next.'
    ],5,stdin='Ada Lovelace\n20 1.65 true\n')
    add('ValidationDemo','Check first, then read','''
import java.util.Scanner;
public class ValidationDemo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter an integer:");
        if (input.hasNextInt()) {
            int number = input.nextInt();
            System.out.println("Number: " + number);
        } else {
            System.out.println("That is not an integer.");
        }
    }
}
''','Enter an integer:\nNumber: 20',[
        'Enter 20: the check returns true, so nextInt() reads 20.',
        'Try hello instead: the check returns false, so the message is printed. This program checks once and then ends; it does not ask again.'
    ],6,stdin='20\n')
    add('ConsumeDemo','Check stays still; read moves forward','''
import java.util.Scanner;
public class ConsumeDemo {
    public static void main(String[] args) {
        Scanner input = new Scanner("hello 20");
        System.out.println(input.hasNextInt()); // false: sees hello
        System.out.println(input.hasNextInt()); // false: still sees hello
        System.out.println(input.next());       // hello: read past it
        System.out.println(input.nextInt());    // 20: now read the integer
        input.close();
    }
}
''','false\nfalse\nhello\n20',[
        'Both checks see hello. Checking does not consume anything.',
        'next() reads hello as text and moves past it; nextInt() can then read 20.',
        'Here we print the text returned by next(). Calling input.next(); alone would read and discard it.'
    ],7)
    add('InputDemo','Why nextLine() can return an empty String','''
import java.util.Scanner;
public class InputDemo {
    public static void main(String[] args) {
        Scanner input = new Scanner("20\\nAda\\n");
        int age = input.nextInt();
        String rest = input.nextLine();
        String name = input.nextLine();
        System.out.println("Age: " + age); // Age: 20
        System.out.println("Rest: [" + rest + "]"); // Rest: []
        System.out.println("Name: " + name); // Name: Ada
        input.close();
    }
}
''','Age: 20\nRest: []\nName: Ada',[
        'nextInt() reads 20 but leaves the line break after it.',
        'The first nextLine() finishes that line. There is no text left on it, so rest is empty: [].',
        'The second nextLine() reads Ada from the next line.'
    ],7)
    first['demos'][-1]['output_in_comments'] = True
    first['demos'][-1]['before_html'] = '<div class="lesson-copy"><h3>The nextLine() trap: finish the current line first</h3><p>Suppose the age and name are on separate lines. After reading the age with nextInt(), the nextLine() call still finishes the age line; it does not jump straight to the name.</p><pre>20\nAda</pre><p>In the code below, a line break is written as <code>\\n</code> inside the Java string to represent a line break.</p><p>If you do not need the remaining text, write <code>input.nextLine();</code> before reading the name. This skips the whole line remainder, so use it only when the name belongs on the next line.</p></div>'
    first['demos'].sort(key=lambda d:d['after'])
