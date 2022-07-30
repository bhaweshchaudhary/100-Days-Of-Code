#include <stdio.h>
#include <string.h>
#include <math.h>
// Linear search algorithm
int main(void) {
    int number[] = {12, 23, 2, 3, 6, 9, 1};

    for (int i = 0; i <= 7; i++) {
        if (number[i] == 1) {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}