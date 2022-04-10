#include <stdio.h>

int main() {
    int n;
    int result = 1;
    printf("Enter the value of n\n");
    scanf("%d", &n);
    for(int i=1; i<=n; i++){
        result = result*i;
    }
    printf("%d", result);
}