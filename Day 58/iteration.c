#include <cs50.h>
#include <stdio.h>

void draw(int n);

int main(void) {
    int height;
    printf("Height:\n");
    scanf("%d", &height);
    draw(height);
    return 0;
}

void draw(int n) {
    for (int i=0; i<n; i++) {
        for (int j = 0; j < i+1; j++) {
            printf("* ");
        }
        printf("\n");
    }
}