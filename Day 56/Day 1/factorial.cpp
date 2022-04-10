#include <iostream>
using namespace std;

int main() {
    int n;
    int multiply = 1;
    printf("Enter the value of n\n");
    scanf("%d", &n);
    for(int i=1; i<=n; i++){
        multiply = multiply*i;
    }
    printf("The factorial of %d is %d", n, multiply);
}