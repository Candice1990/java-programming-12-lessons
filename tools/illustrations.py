import re, html, json
from pathlib import Path
EXTRAS={}
E=lambda s:html.escape(s)
def add(l,s,body):EXTRAS.setdefault((l,s),[]).append(body)
def frame(key,title,caption,body,height=330):
 return f'<figure class="visual-card teaching-illustration"><header><span class="visual-type">Visual explanation</span><h3>{E(title)}</h3></header><div class="illustration-scroll"><svg viewBox="0 0 900 {height}" role="img" aria-labelledby="{key}-title {key}-desc"><title id="{key}-title">{E(title)}</title><desc id="{key}-desc">{E(caption)}</desc><defs><marker id="{key}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="#9b4d2b"/></marker></defs>{body}</svg></div><figcaption class="illustration-caption">{E(caption)}</figcaption></figure>'
def box(x,y,w,h,title,lines=(),dark=False):
 fill='#122127' if dark else '#eee6d8';ink='#f4f0e6' if dark else '#182228'
 s=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{fill}" stroke="#b7977e" stroke-width="1.5"/><text x="{x+20}" y="{y+34}" fill="{ink}" font-size="23" font-weight="600">{E(title)}</text>'
 for i,line in enumerate(lines):s+=f'<text x="{x+20}" y="{y+66+i*26}" fill="{ink}" font-size="18">{E(line)}</text>'
 return s
def arrow(key,x1,y1,x2,y2,label='',ly=None):
 return f'<path d="M{x1} {y1} L{x2} {y2}" stroke="#9b4d2b" stroke-width="2.5" fill="none" marker-end="url(#{key}-arrow)"/>'+ (f'<text x="{(x1+x2)/2}" y="{ly if ly is not None else (y1+y2)/2-12}" text-anchor="middle" fill="#9b4d2b" font-size="17">{E(label)}</text>' if label else '')
def table(title,columns,rows):
 return '<figure class="visual-card"><header><span class="visual-type">Reference table</span><h3>'+E(title)+'</h3></header><div class="visual-table-wrap"><table class="visual-table"><thead><tr>'+''.join('<th scope="col">'+E(v)+'</th>' for v in columns)+'</tr></thead><tbody>'+''.join('<tr>'+''.join(('<th scope="row">'+E(v)+'</th>') if i==0 else '<td>'+E(v)+'</td>' for i,v in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div></figure>'

platform=json.loads((Path(__file__).parent/'program-templates.json').read_text())['platform']
add(1,1,platform)
add(1,1,table('Know which part does what',['Part','Main responsibility','Typical example'],[['JDK','Develops and runs Java programs','Development tools (javac, javadoc, jdb) + runtime components'],['JRE','Provides the environment to run Java programs','JVM + standard libraries and supporting runtime components'],['JVM','Loads and executes Java bytecode','Class loading, interpreter / JIT, memory management and GC']]))

key='class-objects'
body=box(35,95,245,165,'Class: Circle',['radius: double','area(): double'])
body+=box(545,25,315,110,'Object A',['radius = 2.0'],True)+box(545,205,315,110,'Object B',['radius = 5.0'],True)
body+=arrow(key,280,130,535,80,'new Circle()')+arrow(key,280,230,535,255,'new Circle()')
add(1,10,frame(key,'One class defines many independent objects','The class defines the structure and behavior. Each new expression creates a separate object with its own instance state.',body,350))
key='reference-alias'
body=box(30,30,205,95,'first',['reference'])+box(30,190,205,95,'alias',['reference'])+box(580,100,270,130,'One Circle object',['radius = 3.0'],True)
body+=arrow(key,235,80,570,145)+arrow(key,235,235,570,185)
body+='<text x="310" y="300" fill="#59656a" font-size="19">Circle alias = first; copies the reference.</text>'
add(1,10,frame(key,'Two variables can identify the same object','Changing alias.radius changes the object also accessed through first. Assigning a reference does not clone its object.',body))

key='encapsulation-controls'
# A concrete television analogy, drawn as vector shapes rather than a screenshot.
body='<rect x="35" y="65" width="320" height="200" rx="18" fill="#122127"/><rect x="53" y="84" width="284" height="141" rx="8" fill="#dce5db"/><path d="M162 265 L147 286 L245 286 L230 265" fill="none" stroke="#182228" stroke-width="5"/><circle cx="292" cy="245" r="5" fill="#be9072"/><text x="195" y="146" text-anchor="middle" fill="#182228" font-size="25">TV controls</text><text x="195" y="180" text-anchor="middle" fill="#59656a" font-size="20">power · channel · volume</text>'
body+=box(540,45,315,245,'TV object',['Public operations','setVolume(0..100)','changeChannel(number)','','Private state','volume, tuner, circuitry'])
body+=arrow(key,355,165,530,165,'controlled access',145)
add(2,1,frame(key,'Use the controls; protect the implementation','Abstraction presents the useful operations. Encapsulation groups state and behavior and controls access to the internal state. A public setter still needs to enforce valid values.',body))
add(2,1,table('Four OOP ideas, four different questions',['Concept','Question it answers','Java example'],[['Abstraction','What useful operation is exposed?','area() hides the calculation details'],['Encapsulation','Who may read or change the state?','private radius and validated setters'],['Inheritance','Which type specializes another type?','Student extends Person'],['Polymorphism','Which implementation answers this call?','Shape reference calls Circle.area()']]))
key='inheritance-tree'
body=box(310,20,280,105,'Person',['name · describe()'],True)+box(55,215,320,100,'Student',['studentId · study()'])+box(525,215,320,100,'Teacher',['subject · teach()'])
body+=arrow(key,215,215,365,135,'extends',167)+arrow(key,685,215,535,135,'extends',167)
add(2,7,frame(key,'Specializations share a parent contract','Student and Teacher are kinds of Person. Arrows point from the specialized class to its superclass; constructors initialize one complete object, not a separate linked parent object.',body,350))
add(3,1,table('Overloading versus overriding',['Question','Overloading','Overriding'],[['Where is the variation?','Different parameter lists','A subclass supplies a compatible inherited method'],['When is the choice made?','Compile time','Runtime for overridden instance methods'],['What determines the choice?','Declared argument types and applicable signatures','The actual object type'],['Does return type alone suffice?','No','A compatible, possibly covariant return type is required'],['Useful annotation','None required','@Override']]))
key='monitor-gate'
body=box(20,35,230,100,'Worker A',['requests the monitor'])+box(20,215,230,100,'Worker B',['waits while A owns it'])+box(350,110,200,120,'Same lock',['counter monitor'],True)+box(650,100,225,145,'Shared state',['read value','increment','write value'])
body+=arrow(key,250,85,340,145)+arrow(key,250,260,340,195)+arrow(key,550,170,640,170)
add(7,5,frame(key,'One monitor guards the whole update','Only one thread owns this monitor at a time. Synchronizing on different objects would not protect this shared counter. Acquiring and releasing the monitor also establishes visibility.',body,350))
key='collection-contracts'
body=box(315,15,270,75,'Iterable<E>',[],True)+box(315,130,270,75,'Collection<E>',[],True)
body+=arrow(key,450,130,450,100,'extends',113)
for xx,title,lines in [(20,'List<E>',['ArrayList','LinkedList']),(315,'Set<E>',['HashSet · LinkedHashSet','TreeSet']),(610,'Queue<E>',['PriorityQueue','Deque → ArrayDeque'])]:
 body+=box(xx,280,270,130,title,lines)+arrow(key,xx+135,280,450,215)
body+='<text x="450" y="248" text-anchor="middle" fill="#9b4d2b" font-size="17">interfaces extend Collection&lt;E&gt;</text>'
add(10,1,frame(key,'Separate interfaces from their implementations','Iterable enables traversal. Collection groups element-container operations. List, Set and Queue specialize that contract. Map is a separate interface and is not part of this inheritance chain.',body,440))
add(11,7,table('Choose a collection by its contract',['Requirement','Starting point','Ordering or identity rule'],[['Indexed sequence; duplicates allowed','ArrayList','Position and insertion sequence'],['Unique elements; order unimportant','HashSet','equals and hashCode'],['Unique elements in insertion order','LinkedHashSet','equals and hashCode'],['Unique elements in sorted order','TreeSet','Comparison result determines equivalence'],['Key lookup; order unimportant','HashMap','Key equals and hashCode'],['Key lookup in sorted key order','TreeMap','Key comparison'],['FIFO task processing','ArrayDeque via Queue','Add at tail, remove from head']]))

# Data types and memory precede class/object/reference in the opening lesson.
EXTRAS[(1,12)]=EXTRAS.pop((1,10))
add(1,10,table('The eight primitive data types',['Type','Value width','Range / values','Field or array default','Literal example'],[
 ['byte','8 bits','−128 to 127','0','byte b = 12;'],
 ['short','16 bits','−32,768 to 32,767','0','short s = 300;'],
 ['int','32 bits','−2,147,483,648 to 2,147,483,647','0','int age = 20;'],
 ['long','64 bits','−9,223,372,036,854,775,808 to 9,223,372,036,854,775,807','0L','long n = 3_000_000_000L;'],
 ['float','32 bits','Finite values ≈ −3.4028235 × 10^38 to +3.4028235 × 10^38; smallest positive nonzero ≈ 1.4 × 10^-45','0.0F','float f = 3.5F;'],
 ['double','64 bits','Finite values ≈ −1.7976931348623157 × 10^308 to +1.7976931348623157 × 10^308; smallest positive nonzero ≈ 4.9 × 10^-324','0.0D','double d = 3.5;'],
 ['char','16 bits','0 to 65,535; one unsigned UTF-16 code unit',r"'\u0000'","char grade = 'A';"],
 ['boolean','No language-specified storage size','true or false','false','boolean ready = true;']]))
add(1,10,'<aside class="teaching-note"><strong>Read the table correctly</strong>Widths describe primitive value representations, not the complete memory cost of a variable or object. Floating-point values also include positive and negative zero, infinities and NaN; not every value between the bounds is representable. Reference fields and reference-array elements default to null. Local variables must be assigned before use.</aside>')
key='type-families'
body=box(315,15,270,80,'Java data types',[],True)+box(30,180,400,150,'Primitive types',['Integer: byte, short, int, long, char','Floating point: float, double','Logical: boolean'])+box(470,180,400,150,'Reference types',['Class: String, Scanner, Student','Interface: Runnable, List','Array: int[], String[]'])
body+=arrow(key,420,95,230,170)+arrow(key,480,95,670,170)
add(1,10,frame(key,'Two groups of Java data types','String and arrays are reference types.',body,355))

key='three-memory-areas'
body=box(20,30,265,385,'METHOD AREA',[],False)
body+='<text x="40" y="98" font-size="17" fill="#59656a">Shared class information</text><line x1="40" y1="116" x2="265" y2="116" stroke="#c5b298"/>'
for y,label in [(153,'Student class metadata'),(191,'Constructor code'),(229,'main() method code'),(267,'Other method code')]:
 body+=f'<text x="40" y="{y}" font-size="17" fill="#182228">{label}</text>'
body+='<text x="40" y="348" font-size="16" fill="#59656a">Stores definitions and code,</text><text x="40" y="375" font-size="16" fill="#59656a">not each call’s local values.</text>'
body+=box(310,30,255,385,'STACK',[],False)
body+='<text x="330" y="98" font-size="17" fill="#59656a">One stack per thread</text><rect x="330" y="128" width="215" height="235" rx="9" fill="#fbf8f1" stroke="#b7977e"/><text x="350" y="162" font-size="20" font-weight="600" fill="#182228">main() frame</text><text x="350" y="201" font-size="17" fill="#59656a">Parameters / local values</text><rect x="348" y="222" width="177" height="44" rx="5" fill="#eee6d8"/><text x="362" y="251" font-size="19" fill="#182228">age = 20</text><rect x="348" y="283" width="177" height="44" rx="5" fill="#eee6d8"/><text x="362" y="312" font-size="19" fill="#182228">s = reference</text>'
body+=box(645,30,235,385,'HEAP',[],True)
body+='<text x="665" y="98" font-size="17" fill="#bccbc7">Shared objects and arrays</text><rect x="665" y="227" width="195" height="118" rx="9" fill="#e4ebe3"/><text x="683" y="261" font-size="20" font-weight="600" fill="#182228">Student object</text><text x="683" y="298" font-size="18" fill="#182228">score = 0</text><text x="683" y="324" font-size="16" fill="#59656a">instance field</text>'
body+=arrow(key,526,305,655,286)
body+='<text x="592" y="266" text-anchor="middle" fill="#9b4d2b" font-size="15">points to</text>'
add(1,11,frame(key,'Code, local variables and objects','Conceptual JVM model. The reference s is local, so it is shown in the stack frame. References stored in object fields or array elements belong to those heap objects.',body,440))
add(1,11,'<div class="memory-example"><code>int age = 20;<br>Student s = new Student();</code><p><strong>Method call:</strong> creates a stack frame. <strong>new:</strong> creates an object and returns its reference. <strong>Method return:</strong> removes the frame; an object may remain alive if still reachable.</p></div>')

add(1,4,table('Scanner reads different input sources',['Input source','Constructor expression','Meaning'],[
 ['Keyboard / standard input','new Scanner(System.in)','Reads the process standard input; normally the keyboard'],['File','new Scanner(new File("data.txt"))','Reads a file; requires java.io.File and checked-exception handling'],['String','new Scanner("10 20 30")','Parses characters already stored in a String'],['Network input stream','new Scanner(socket.getInputStream())','Assumes an existing connected socket; obtaining the stream can throw IOException']]))
add(1,4,'<aside class="teaching-note"><strong>Same parser, different source</strong>These constructor expressions show alternatives, not four statements from one complete program. File handling is developed in lesson 6. The socket expression is only a source illustration, not a network connection example. Closing a Scanner closes its underlying source when that source is closeable; ownership must be deliberate.</aside>')

# Present the classification immediately after the short introduction, before details.
type_panels=EXTRAS[(1,10)]
classification=next(panel for panel in type_panels if 'id="type-families-title"' in panel)
EXTRAS[(1,10)]=[classification]+[panel for panel in type_panels if panel is not classification]

# Lesson 1 merges the former third concept into the program skeleton.
EXTRAS = {(lesson, section - 1 if lesson == 1 and section > 3 else section): panels
          for (lesson, section), panels in EXTRAS.items()}

from course import LESSON_ONE_SECTION_POSITIONS
EXTRAS = {(lesson, LESSON_ONE_SECTION_POSITIONS[section] if lesson == 1 else section): panels
          for (lesson, section), panels in EXTRAS.items()}

# Alternative branches, not consecutive steps; both consume exactly one token.
key='scanner-validation'
body=box(190,15,520,95,'While input.hasNext() is true',
         ['A token is available. Otherwise, finish the loop.'],True)
body+=arrow(key,450,110,450,150)
body+='<path d="M450 150 L665 230 L450 310 L235 230 Z" fill="#eee6d8" stroke="#9b4d2b" stroke-width="2"/>'
body+='<text x="450" y="222" text-anchor="middle" fill="#182228" font-size="23" font-weight="600">input.hasNextInt()?</text><text x="450" y="250" text-anchor="middle" fill="#59656a" font-size="18">Check only — do not consume</text>'
body+='<path d="M235 230 H215 V350 M665 230 H685 V350" fill="none" stroke="#9b4d2b" stroke-width="2.5" marker-end="url(#scanner-validation-arrow)"/>'
body+='<text x="195" y="324" text-anchor="middle" fill="#315e48" font-size="19" font-weight="600">YES · fits int</text><text x="705" y="324" text-anchor="middle" fill="#9b4d2b" font-size="19" font-weight="600">NO · does not fit int</text>'
body+=box(20,350,390,150,'int number = input.nextInt();',
          ['Read and convert one token to int.', 'Example: "20" → integer 20', 'Use the integer value.'])
body+=box(490,350,390,150,'String skipped = input.next();',
          ['Read one token as text, then skip it.', 'Examples: "hello" or "3.5"', 'No numeric conversion is required.'])
body=body.replace('font-size="23" font-weight="600">int number', 'font-size="19" font-weight="600">int number').replace('font-size="23" font-weight="600">String skipped', 'font-size="19" font-weight="600">String skipped')
body+='<path d="M215 500 V540 H450 M685 500 V540 H450 V575" fill="none" stroke="#9b4d2b" stroke-width="2.5" marker-end="url(#scanner-validation-arrow)"/>'
body+=box(190,575,520,95,'Both paths advance past one token',
          ['Repeat: check hasNext() before the next iteration.'],True)
SCANNER_VALIDATION=frame(key,'Check, then choose ONE reading path',
    'Invalid means “not readable as an int”, not unreadable text. next() reads any available token as a String; nextDouble() would still fail on text such as hello. Checking alone never advances the input.',body,690)
SCANNER_VALIDATION+='<div class="trace-grid"><div class="expected"><b>Example input</b><pre>hello 3.5 20</pre></div><div class="walkthrough"><b>Three loop iterations</b><ol><li><code>hello</code> → NO → <code>next()</code> reads and skips it.</li><li><code>3.5</code> → NO → <code>next()</code> reads and skips it.</li><li><code>20</code> → YES → <code>nextInt()</code> returns the integer 20.</li></ol><p>Consume means read and move past a token. If you only display an error, the next check sees the same token again.</p></div></div>'

# Scanner source and method tables now belong to the four-part written unit.
from scanner_unit import SECTION_POSITIONS
EXTRAS = {(lesson, SECTION_POSITIONS[section] if lesson == 1 else section): panels
          for (lesson, section), panels in EXTRAS.items()
          if not (lesson == 1 and section in (4, 5, 6, 7, 8))}

# Match the five-part opening lesson and the moved OOP introduction.
from course import SECOND_SECTION_POSITIONS
EXTRAS = {(lesson, SECOND_SECTION_POSITIONS[section] if lesson == 2 else section): panels
          for (lesson, section), panels in EXTRAS.items()}
EXTRAS[(1,4)]=EXTRAS.pop((1,9))
EXTRAS[(2,1)]=EXTRAS.pop((1,10))
