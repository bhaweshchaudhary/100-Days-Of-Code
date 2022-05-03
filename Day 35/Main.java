// Write a program to create a class Student with data ‘name, city and age’ along with method printData to display the data. Create the two objects s1 ,s2 to declare and access the values. 

class Student {
    String name;
    String city;
    int age;

    public Student(String name, String city, int age) {
        this.name = name;
        this.city = city;
        this.age = age;
    }
// copy constructor
    Student(Student s2){
        name = s2.name;
        city = s2.city;
        age = s2.age;
    }

    void printData(){
        System.out.println(this.name);
        System.out.println(this.city);
        System.out.println(this.age);
    }
}

public class Main {
    public static void main(String args[]) {
        Student s2 = new Student("bhawesh", "vizag", 19);
        s2.printData();

    }
}

