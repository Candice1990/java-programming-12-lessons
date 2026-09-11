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
            'Calling nextInt() directly on hello throws InputMismatchException and leaves that token unread; checking first lets the program handle it deliberately.',
            'Validation asks whether input meets a requirement. First check whether a token can be read as the desired type: hasNextInt() before nextInt(), hasNextDouble() before nextDouble(), or hasNextBoolean() before nextBoolean(). hasNext() checks for any token; hasNextLine() checks for another line. These checks do not read past the input.',
            'After reading a correctly typed value, check the rule for your program. For example, -2 is a valid int but an invalid age under an age >= 0 rule. Type validation and value validation answer different questions.',
            'In the loop below, hasNext() guards against the end of input. If a token is not an int, next() reads and skips it as text. This advances the input so the next iteration can inspect a different token. The next part explains this movement in detail.'
        ]),
        dict(title='Scanner: consume input and understand the nextLine() trap', paragraphs=[
            'Consume means read input and advance the Scanner’s position past it. It does not necessarily mean discard: int age = input.nextInt() consumes a token and keeps its converted value. input.next() without storing the result consumes a token and discards its text.',
            'hasNextInt() only looks ahead. nextInt() consumes a token if it can convert it to int. next() consumes any available token as a String, which makes it useful for skipping invalid numeric input. nextDouble() also consumes, but cannot skip arbitrary text such as hello because it requires a floating-point token.',
            'Token reads and line reads stop in different places. After nextInt() reads 20 from a line containing only 20, the following line separator remains. nextLine() then reads the remainder of that current line: an empty String, and moves past the separator. It has not read the name on the next line.',
            'When your input format puts the name on the next line, call nextLine() once to finish the number’s line, then again to read the name. That first call discards the entire line remainder, not just a newline; if the name is on the same line as the number, it would be discarded too.'
        ],html=table('Trace the read position: 20 followed by a name on the next line',[
            ['Input','20\\nAda Lovelace\\n','Here \\n represents a line break.'],
            ['Read the integer','nextInt() → 20','The position is just after 20, before its line break.'],
            ['Finish the current line','nextLine() → ""','Reads the empty remainder and passes the line break.'],
            ['Read the name','nextLine() → "Ada Lovelace"','Reads the next line and passes its line break.']
        ]),note='Calling nextLine() twice is not a general rule. It is needed here because we switch from a token read to a separate next-line field. A program that only reads lines does not need this extra call.')
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
    add('ValidationDemo','Validate the type, then the value','''
import java.util.Scanner;
public class ValidationDemo {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter an age (0 or greater):");
        while (input.hasNext()) {
            if (!input.hasNextInt()) {
                String skipped = input.next();
                System.out.println("Not an int: " + skipped);
                continue;
            }
            int age = input.nextInt();
            if (age < 0) {
                System.out.println("Age cannot be negative: " + age);
                continue;
            }
            System.out.println("Accepted age: " + age);
            return;
        }
        System.out.println("No valid age supplied");
    }
}
''','Enter an age (0 or greater):\nNot an int: hello\nNot an int: 3.5\nAge cannot be negative: -2\nAccepted age: 20',[
        'hasNextInt() does not advance. next() skips hello and 3.5 as text so the loop can move forward.',
        '-2 passes the type check and is consumed by nextInt(), but fails the non-negative age rule.',
        'continue starts another loop iteration; return ends main after the first acceptable age. A keyboard check may wait for more input.'
    ],6,stdin='hello 3.5 -2 20\n')
    add('InputDemo','Consume a token, then finish its line','''
import java.util.Scanner;
public class InputDemo {
    public static void main(String[] args) {
        try (Scanner input = new Scanner("20\\nAda Lovelace\\n")) {
            System.out.println("Check 1: " + input.hasNextInt());
            System.out.println("Check 2: " + input.hasNextInt());
            int age = input.nextInt();
            String remainder = input.nextLine();
            String name = input.nextLine();
            System.out.println("Age: " + age);
            System.out.println("Line remainder: [" + remainder + "]");
            System.out.println("Name: " + name);
        }
    }
}
''','Check 1: true\nCheck 2: true\nAge: 20\nLine remainder: []\nName: Ada Lovelace',[
        'Both checks see the same 20 because look-ahead does not consume input.',
        'nextInt() reads 20; the first nextLine() returns an empty String shown as []. The second reads Ada Lovelace.',
        'Using a fixed String makes the position changes repeatable. With new Scanner(System.in), the same reading sequence works when the user enters the age and name on separate lines.'
    ],7)
    first['demos'].sort(key=lambda d:d['after'])
