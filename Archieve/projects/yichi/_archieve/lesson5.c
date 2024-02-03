#include <stdio.h>
#include <string.h>
#include "utils.h"

struct Person {
    int age;
    char name[30];
    float weight;
    float height;
};

int main() {
    int arr[5] = {10, 1, 2, 3, 4}; // 20 byte
    int * pi = arr; 
    unsigned i = 0;

    // // you are actually printing the address of the first element in the arr
    // printf("%p\n", arr);

    // // you can use an array like a pointer ot the first elmenet
    // printf("%d\n", *pi);

    // // although you can use array like a pointer, but they are not the same
    // printf("size of arr %lu, size of pi %lu\n", sizeof(arr), sizeof(pi));

    for (i = 0; i < 5; ++i) {
        // printf("%d\n", arr[i]);
        printf("%d\n", *pi);
        // printf("%p | %p\n", pi, pi + 1);
        pi += 1;
    }

    /* Pointer arithmetic 
    
    看起来是    pi + 10
    其实是      pi + sizeof(int) * 10


    另一个藏起来的语法： syntatic sugar
    看起来是    arr[3]
    其实是      *(arr + sizeof(int) * 3)
    
    */
    pi = arr;
    printf("%d\n", pi[4]); // *(pi + sizeof(int) * 4) 


    int testnum = 1102053376;
    printf("%f\n", *(float*)&testnum);

    /*
    在C里面，一个内存格子储存的数据没有类型，取决于我们怎样使用它
    0x41
    0xB0
    0x00
    0x00
    */

    struct Person yichi;
    yichi.age = 20;
    yichi.height = 180;
    yichi.weight = 70;

    // string copy
    mystrcpy(yichi.name, "Zhang Yichi");
    // yichi.name[0] = 'T';
    
    strcpy(yichi.name, "Liang");
    yichi.name[5] = ' ';

    printf("%s is %d years old\n", yichi.name, yichi.age);
    printf("my name has %lu characters\n", strlen(yichi.name));

    // strlen will not count the null terminator
    // strcpy will copy the null terminator (\0)
}