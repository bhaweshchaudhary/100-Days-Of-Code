class Pen{
    String color;
    String type;

    void printSomething(){
        System.out.println(this.color);
    }
}

public class Main{
    public static void main(String args[]){
        Pen pen1 = new Pen();
        Pen pen2 = new Pen();
        pen1.color = "Blue";
        pen2.color = "Black";
        pen1.printSomething();
        pen2.printSomething();
    }
}