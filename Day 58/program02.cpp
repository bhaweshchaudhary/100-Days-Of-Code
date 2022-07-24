#include <iostream>
using namespace std;

// right angle triangle function
void rightAngleTriangle() {
    // declaring variable to store rows number
    int n;
    // asking user to enter the following
    cout << "Enter the number of rows" << endl;
    // storing the value of rows in variable n
    cin >> n;
    // rows
    for (int i = 1; i <= n; i++) {
        // columns
        for (int j = 1 ; j <= i; j++) {
            cout << "* ";
        }
        cout << endl;
    }
}

// square function
void square() {
    // declare variable -> rows
    int n;
    // initialize row
    int i = 1;
    // user input -> rows
    cout << "Enter the total number of rows" << endl;
    cin >> n;
    // while loop
    while (i <= n) {
        int j = 1;
        while (j <= n) {
            cout << "* ";
            j = j + 1;
        }
        cout << endl;
        i = i + 1;
    }
}

// main function
int main() {
    // function called
    square();
    return 0;
}