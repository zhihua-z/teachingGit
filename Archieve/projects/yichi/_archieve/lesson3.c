#include <stdio.h>

int main() {
    /* Array size is determined at compile time, 在编译时就确定array的大小 */
    /* myNumbers is an array of int */
    /*   start -> array | */
    /* int            <-  */
    int myNumbers[] = {25, 50, 75, 10}; /* implicitly convert 100.0 into int */
    unsigned i = 0;

    for (; i < 5; ++i) {
        printf("%d ", myNumbers[i]);
    }

    /* 
        "c" : we call this a string literal, in the execution of a program
        strings are not stored as those local variables....

        Program RAM Allocations:
            .CODE : stores all the codes of your program
            .DATA : global variables and your strings...
            stack : functions and local variables
            heap : dynamically allocated memories

        this is why when we do this...
            int myNumbers[] = {25, 50, 75, 10, "c"};
        it says we can't implicitly convert a pointer into int, "c" is actually 
          a pointer pointing to the string "c" in the .DATA section
    */

    /* matrix is an array of two (array of 3 integers) */
    /* int matrix[2][3] = { {1, 4, 2}, {3, 6, 8} }; */

    /*  */
    char greetings[] = "Hello World!";
    printf("%lu\n", sizeof(greetings)); /* 13 byte because this is an array, with \0 behind */

    char * greetings2 = "Hello World!";
    printf("%lu\n", sizeof(greetings2)); /* 8 byte because this is a pointer */

    printf("--------------\n");
    printf("%s\n", greetings);
    printf("%s\n", greetings2);
    printf("%d\n", greetings);
    printf("%d\n", greetings2);

    /* gcc is very kind to initialize all the memory to 0 in the beginning */
    /* msvc microsoft compiler will not do this nice thing for you
       all the memory are rubbish value
     */
    char gree[] = {'H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', '!'};
    printf("%s", gree);



    // Create an integer variable that will store the number we get from the user
    int myNum;

    // Ask the user to type a number
    printf("Type a number: \n");


    /* reference operator / address of */
    /* scanf did not change anything to myNum variable, but changed what is stored inside */
    // scanf("%d", &myNum);

    // // Output the number the user typed
    // printf("Your number is: %d", myNum);

    char firstName[10];

    // Ask the user to input some text (name)
    printf("Enter 9 characters: \n");

    // Get and save the text
    scanf("%f", firstName);

    // Output the text
    printf("|%s|", firstName);

    /* When we assign a value to the variable, it is stored in this memory address. */
    /* this is totally different from python, probably different from java as well 
    
    int a = 5; // 0x100c
    a = 10; // 0x100c

    a本身时不变的，它原本在哪儿，现在就在哪儿，变化的只是这个地址储存的值

    对于python来说，a = 10的时候，可能a就是另一个东西了。。地址可能就不是原来那个了
    在python当你说a=5的时候，你是做了一个盒子，储存5在里面，然后把这个盒子的reference放在a里。
    当你再做一次a=10的时候，根据当前的内存策略，你有可能做了一个新盒子，储存10在里面，然后把这个黑子的reference放在a里。

    */


    return 0;
}
