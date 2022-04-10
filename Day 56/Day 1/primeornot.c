// prime means the number that only comes in the table of either 1 or itself. means if i divide all the numbers from 2 to n-1 then remainder shouldn't be zero.

#include <stdio.h>

int main(){
    int number;
    printf("Enter the number to check prime or not\n");
    scanf("%d", &number);
    for(int i=2; i<number; i++){
        if(number%i!=0){
            printf("It is prime number.");
        }
        else{
            printf("It is not prime number.");
        }
    }
}