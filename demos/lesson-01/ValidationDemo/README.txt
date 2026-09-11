Open a terminal in this demo folder. Use JDK 21 or later.

javac ValidationDemo.java
java ValidationDemo < input.txt

Expected output:
Enter an age (0 or greater):
Not an int: hello
Not an int: 3.5
Age cannot be negative: -2
Accepted age: 20
