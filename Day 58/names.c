#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void) {
    string name[] = {"shiwani", "anu", "bhawesh", "suraj", "tunu", "naresh", "pinku"};
    for (int i = 0; i < 7; i++) {
        if (strcmp(name[i], "chandani") == 0) {
            printf("Name Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}