#include <iostream>
using namespace std;

int main() {
    int n;
    int multiply = 1;
    cout << "Enter the value of n" << endl;
    scanf("%d", &n);
    for(int i=1; i<=n; i++){
        multiply = multiply*i;
    }
    cout << "The factorial of " << n << " is " << multiply << endl;
}