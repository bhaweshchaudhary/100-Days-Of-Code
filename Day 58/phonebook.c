#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct {
        string names;
        string numbers;
    }
    person;

int main(void) {
    // string names[] = {"shiwani", "bhawesh"};
    // string phone[] = {"+977-9828374890", "+91-8293827739"};

    person people[2];

    people[0].names = "Shiwani";
    people[0].numbers = "+977 98349303922";

    people[1].names = "Bhawesh";
    people[1].numbers = "+91 827382728192"; 

    for (int i = 0; i < 2; i++) {
        if (strcmp(people[i].names, "Bhawesh") == 0) {
            printf("Found %s\n", people[i].numbers);
            return 0;
        }
    }
    printf("Not found, try again.\n");
}