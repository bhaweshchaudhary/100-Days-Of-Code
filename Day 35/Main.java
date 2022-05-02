// Write a program to create a class Student with data ‘name, city and age’ along with method printData to display the data. Create the two objects s1 ,s2 to declare and access the values. 

class Student{
    String name;
    String city;
    int age;

    void printData(){
        System.out.println("Name is "+ this.name);
        System.out.println("City is "+ this.city);
        System.out.println("Age is "+ this.age + "\n");
    }
}

public class Main{
    public static void main(String args[]){
        Student s1 = new Student();
        s1.name = "Bhawesh";
        s1.city = "Vizag";
        s1.age = 21;
        Student s2 = new Student();
        s2.name = "Einstein";
        s2.city = "Zurich";
        s2.age = 199;
        s1.printData();
        s2.printData();
    }
}