class Pen {
    String color;
    String type; // ballpoint, gel

    public void write() {
        System.out.println("Write Something");
    }
}

public class OOPS {
    public static void main(String args[]) {
        Pen pen1 = new Pen();
        pen1.color = "blue";
        pen1.type = "gel";

        pen1.write();
    }
}