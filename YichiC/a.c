
#include <stdio.h>


struct BigItem {
    struct AAAA {
        int integer;        // 4
        char character;     // 1 + 3
        float fp;           // 4
    } b1; // 12 + 4

    struct BBBB {
        int integer;        // 4
        char character;     // 1 + 3
        double fp;          // 8
    } b2; // 16
};


union Item
{
    struct DDDD {
        int integer;
        char character;
        float fp;
    } b1;

    struct CCCC {
        int integer;
        char character;
        double fp;
    } b2;

    char k;

    // 1 sign bit
    // 11 exponent big
    // 52 mantissa
};

int main()
{
    union Item item;
    struct BigItem bigItem;
    
    printf("addr of bigitem b1: %p\n", &bigItem.b1);
    printf("addr of bigitem b2: %p\n", &bigItem.b2);

    printf("addr of item b1: %p\n", &item.b1);
    printf("addr of item b1: %p\n", &item.b2);

    item.b1.integer = 817293719;

    // printf("%p\n", (&item.b2.character) + 1);
    // printf("b2 integer: %d\n", *(&item.b2.character + 1));

    printf("%c\n", item.k);

    /* static allocation :  */
    union Item arr[10];

    /* dynamic allocation */
    // int * arr = (int*) malloc(10 * sizeof(int));

    arr[0].b1.integer = 10;
    arr[1].b2.character = 'c';
    arr[2].b1.fp = 1.12f;
    arr[100].b1.character = 'c'; // arr's position + 100 * sizeof(union Item) + 5


    return 0;
}
