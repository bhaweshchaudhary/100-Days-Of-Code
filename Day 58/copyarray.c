#include <stdio.h>

int main(void) {
    int firstArray[] = {1, 2, 4, 5, 6, 7, 8, 9};
    int length = sizeof(firstArray)/sizeof(firstArray[0]);
    printf("%d\n", length);
}