#include <stdio.h>
#include <stdlib.h>
#include <math.h>
/*

multidimensional array and double pointers


*/

/* complex c declaration */
/* int * arr [4] this is an array of 4 integer pointers */
/* int (*arr) [4] this is a pointer to an array of 4 integers */
void init(int (*arr) [4], unsigned row, unsigned col) {
    for (unsigned i = 0; i < row; ++i)
        for (unsigned j = 0; j < col; ++j)
            arr[i][j] = i + j;
}

void print(int (*arr) [4], unsigned row, unsigned col) {
    for (unsigned i = 0; i < row; ++i) {
        for (unsigned j = 0; j < col; ++j)
            printf("%d ", arr[i][j]);
        printf("\n");
    }
}   

void receive_arr(int arr[5]) {
    printf("%d\n", arr[0]);
}

void init2(int* s, unsigned row, unsigned col) {
    for (unsigned i = 0; i < row * col; ++i)
        s[i] = i / col + i % col;
}

void print2(int * s, unsigned row, unsigned col) {
    for (unsigned i = 0; i < row * col; ++i) {
        printf("%d ", s[i]);
        if (i % col == col - 1) // at the end of this column
            printf("\n");
    }
}

void init3(int ** s, unsigned row, unsigned col) {
    for (unsigned i = 0; i < row; ++i)
        for (unsigned j = 0; j < col; ++j)
            s[i][j] = i + j;
}

void print3(int ** s, unsigned row, unsigned col) {
    for (unsigned i = 0; i < row; ++i) {
        for (unsigned j = 0; j < col; ++j)
            printf("%d ", s[i][j]);
        printf("\n");
    }
}

int add(int, int);
int mul(int, int);
int pow2(int, int);
void dothis(int (fn)(int, int), int, int);

int main() {
    /*
    
            METHOD 1 (native array)
    
    */
    int arr[5][4];
    // arr is an array of 5 (array of 4 integers)

    // int arr2[5] = {5, 4, 3 ,2 ,1};
    // receive_arr(arr2);

    // this is a pointer to array of 4 integer
    init(&arr[0], 5, 4);
    print(&arr[0], 5, 4);
    /*
    0 1 2 3
    1 2 3 4
    2 3 4 5
    3 4 5 6
    4 5 6 7
    */

    /* C multidimensional array 
    
            METHOD 2 FAKE MULTIDIMENSIONAL ARRAY

    if I want an 5 x 4 array
    */
    int * array = (int*) malloc(sizeof(int) * 5 * 4);
    init2(array, 5, 4);
    print2(array, 5, 4);
    free(array);




    /*
    
            METHOD 3, REAL 2 DIMENSIONAL ARRAY
    
    */
    int ** marray = (int **) malloc(sizeof(int *) * 5);
    for (unsigned i = 0; i < 5; ++i) {
        marray[i] = (int *) malloc(sizeof(int) * 4);
    }

    init3(marray, 5, 4);
    print3(marray, 5, 4);

    for (unsigned i = 0; i < 5; ++i) {
        free(marray[i]);
    }
    free(marray);



    /*
    
            EXTENSINO: 3x3x3 array
    
    */
    int *** carray = (int***) malloc(sizeof(int**) * 3);
    for (unsigned i = 0; i < 3; ++i) {
        carray[i] = (int**) malloc(sizeof(int*) * 3);
        for (unsigned j = 0; j < 3; ++j) {
            carray[i][j] = (int*) malloc(sizeof(int) * 3);
        }
    }

    // use it....

    for (unsigned i = 0; i < 3; ++i) {
        for (unsigned j = 0; j < 3; ++j) {
            free(carray[i][j]);
        }
        free(carray[i]);
    }
    free(carray);


    /*  
    
            HIGH ORDER FUNCTIONS

    */
    
    // fn is a pointer to a function that takes in two integers and return an int
    // int (*fn)(int, int) = &add;

    // fn is an array of two pointers to function that takes in two integers and return an int
    int (* fn[3])(int, int) = {&add, &mul, &pow2};


    int option = 0;
    int param1 = 1;
    int param2 = 2;

    switch (option) {
        case 0:
            printf("%d\n", add(param1, param2));
            break;
        case 1:
            printf("%d\n", mul(param1, param2));
            break;
        case 2:
            printf("%d\n", pow2(param1, param2));
            break;
    }

    /*
    Human john = Human('John', 12, 'M');
    john.walk()
    john.run()
    john.grow(2)

    how does C++ achieve this? if you write .walk it knows that it needs to run the walk function

    C++ have a virtual table structure, 
        string -> function

    
    
    */
    
    
    


    return 0;
}

/* the function signature of add, mul and pow2 are the same, so they are of the same type */
int add(int a, int b) {
    return a + b;
}

int mul(int a, int b) {
    return a * b;
}

int pow2(int a, int b) {
    return pow(a, b);
}

// fn is a function that takes in two functions and return an integer
void dothis(int (fn)(int, int), int a, int b) {
    int result = fn(a, b);
    printf("%d\n", result);
}


/* HOME WORK

now you are hosting a school system
> so you need to have a multi dimensional array of :
1. year 
     2. class
          3. student

> this code will get input from user

> this code will also print out the entire school students in this order:

year 1
    class 1E1
        John, 15, "M", .....
        Marry, 14, "F", .....

    class 1E2
        ...
        ...

year 2
    ...
    ..


> free
...
 */