#include <stdio.h>

int main(void) {
    // int list[3]; this automatically create a stack memory
    // below program create a heap memory
    int *list = malloc(3 * sizeof(int));
    // error check
    if (list == NULL) {
        return 1;
    }
    //
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // time passes

    int *tmp = malloc(4 * sizeof(int));
    if (tmp == NULL) {
        free(list);
        return 1;
    }
    
}