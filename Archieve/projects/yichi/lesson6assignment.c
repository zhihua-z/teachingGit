#include <stdio.h>
#include <stdlib.h>

struct Student{
    char name[30];
    int age;
};

int main() {
    int Number = 0;
    struct Student * s = 0;

    printf("Please enter the number of students: \n");
    scanf("%d", &Number);
    printf("\n");

    s = (struct Student *) malloc(sizeof(struct Student) * Number);

    // in C, variable names usually start with lower case letters
    // class name usually start with upper case letters
    for(int Index = 0; Index < Number; Index++){
        printf("Please enter the name of student %d: \n", Index+1);
        // 你可以直接写s[Index].name
        scanf("%s", s[Index].name);
        printf("Please enter the age of student %d: \n", Index+1);
        scanf("%d", &s[Index].age);
        printf("Information saved, (%s, %d)\n", s[Index].name, s[Index].age);
        printf("\n");
    }

    printf("\n");
    printf("All Information acquired: \n");

    for(int Index = 0; Index < Number; Index++){
        printf("%s, %d\n", s[Index].name, s[Index].age);
    }

    free(s); // no free no mark
    return 0;
}