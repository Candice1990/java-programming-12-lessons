class Product {
    private final String itemNo, name;
    private double price;
    private int quantity;
    public Product(String itemNo, String name) { this(itemNo, name, 0, 0); }
    public Product(String itemNo, String name, double price, int quantity) {
        this.itemNo = itemNo; this.name = name;
        setPrice(price); setQuantity(quantity);
    }
    public String getItemNo() { return itemNo; }
    public String getName() { return name; }
    public double getPrice() { return price; }
    public int getQuantity() { return quantity; }
    public void setPrice(double value) { price = Math.max(0, value); }
    public void setQuantity(int value) { quantity = Math.max(0, value); }
}
class Customer {
    private final String customerId, name;
    private String address, phone;
    public Customer(String customerId, String name) {
        this(customerId, name, "", "");
    }
    public Customer(String customerId, String name, String address, String phone) {
        this.customerId = customerId; this.name = name;
        this.address = address; this.phone = phone;
    }
    public String getCustomerId() { return customerId; }
    public String getName() { return name; }
    public String getAddress() { return address; }
    public String getPhone() { return phone; }
    public void setAddress(String value) { address = value; }
    public void setPhone(String value) { phone = value; }
}
public class ProductCustomerDemo {
    public static void main(String[] args) {
        Product p = new Product("P01", "Notebook", 5, 10);
        p.setPrice(6);
        System.out.println(p.getItemNo() + ": " + p.getPrice()); // P01: 6.0
        Customer c = new Customer("C01", "Ada");
        c.setPhone("+1 0123");
        System.out.println(c.getName() + ": " + c.getPhone()); // Ada: +1 0123
    }
}
