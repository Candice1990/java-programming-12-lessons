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
