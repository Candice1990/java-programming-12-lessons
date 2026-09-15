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
