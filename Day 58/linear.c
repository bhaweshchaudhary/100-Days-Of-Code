#include <stdio.h>

int main(void) {
    // given array
    int arr[] =  {10, 20, 80, 30, 60, 50,110, 100, 130, 170};
    // to find
    int number = 80;
    // length of given array
    int length = sizeof(arr)/sizeof(arr[0]);
    // iterate through the given array
    for (int i = 0; i < length; i++) {
        if (arr[i] == number) {
            // if number found
            printf("At index %d in given array the number %d is present.\n", i, number);
            return 0;
        }
    }
    // if number not found
    printf("Not present in array\n");
    return 1;
}