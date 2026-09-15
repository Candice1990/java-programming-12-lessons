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
