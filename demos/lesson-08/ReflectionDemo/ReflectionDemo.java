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
