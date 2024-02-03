#include <stdio.h>
#include <stdlib.h>

struct Student{
    char Name[30];
    char Gender[6];
    int Age;
};

int main() {
    int Grades = 0;
    int Classes = 0;
    int Students = 0;

    // Input Part, User input three integers that related to the multi dimensional array.
    printf("Please enter the number of grades: \n");
    scanf("%d", &Grades);
    printf("\n");

    printf("Please enter the number of classes of each grade: \n");
    scanf("%d", &Classes);
    printf("\n");

    printf("Please enter the number of students of each class: \n");
    scanf("%d", &Students);
    printf("\n");

    // Creating a multi dimensional array and allocate memory for this array, it's size is Grades x Classes x Students.
    struct Student *** School_List = (struct Student***) malloc(sizeof(struct Student**) * Grades);
    for (unsigned i = 0; i < Grades; ++i) {
        School_List[i] = (struct Student**) malloc(sizeof(struct Student*) * Classes);
        for (unsigned j = 0; j < Classes; ++j) {
            School_List[i][j] = (struct Student*) malloc(sizeof(struct Student) * Students);
        }
    }

    // User enter the information of Students of each class of each grade.
    for(int i = 0; i < Grades; i++){
        for(int j = 0; j < Classes; j++){
            for(int k = 0; k < Students; k++){
                printf("Please enter the Name of Grade %d, Class %d, Student %d\n:",i+1,j+1,k+1);
                scanf("%s", (School_List[i][j][k]).Name);
                printf("\n");
                printf("Please enter the Gender of Grade %d, Class %d, Student %d\n:",i+1,j+1,k+1);
                scanf("%s", (School_List[i][j][k]).Gender);
                printf("\n");
                printf("Please enter the Age of Grade %d, Class %d, Student %d\n:",i+1,j+1,k+1);
                scanf("%d", (School_List[i][j][k]).Age);
                printf("\n");
            }
        }
    }

    // After Entering all informations of students of this school. Show it.
    printf("\n");
    for(int i = 0; i < Grades; i++){
        printf("Grade %d: \n",i+1);
        for(int j = 0; j < Classes; j++){
            printf("    Class %d: \n",j+1);
            for(int k = 0; k < Students; k++){
                printf("        %s, %s, %d\n", School_List[i][j][k].Name, School_List[i][j][k].Gender, School_List[i][j][k].Age);
            }
        }
    }


    // free the memory of the multi dimensional array.
    for (unsigned i = 0; i < Grades; ++i) {
        for (unsigned j = 0; j < Classes; ++j) {
            free(School_List[i][j]);
        }
        free(School_List[i]);
    }
    free(School_List);

    return 0;
}