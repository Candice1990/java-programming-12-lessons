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
