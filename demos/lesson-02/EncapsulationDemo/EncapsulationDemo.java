class Student {
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

public class EncapsulationDemo {
    public static void main(String[] args) {
        Student student = new Student(7, 80);
        student.setScore(92);
        System.out.println(student.getId() + ": " + student.getScore());
    }
}
