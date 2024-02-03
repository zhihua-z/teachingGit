#include <stdio.h>

int main() {
    /* integral type 整数类型 */
    
    /* only for versions before C99
    bool b = true; 
    bool f = false;
    */

    char c = 'a';  /* ''表示一个字符*/ /* ASCII */ /* 1 byte */
    printf("char size:%lu\n", sizeof(c));  /* operator, not a function, return the size of a variable */

    signed short s = -275; /* 2 byte, 65535 values*/
    printf("%d\n", s);
    printf("short size: %lu\n", sizeof(s));  /* operator, not a function, return the size of a variable */


    int i = 10; /* 4 byte, -21亿 - 21亿, signed */
    unsigned int ui = 10; /* 4 byte unsigned int, 0 - 43亿 */
    printf("int size: %lu\n", sizeof(i));  /* operator, not a function, return the size of a variable */

    long l = 5; /* 4/8 byte,  */
    printf("long size: %lu\n", sizeof(l));  /* operator, not a function, return the size of a variable */

    long long ll = 10; /* size >= long, 4/8/16 */
    unsigned long long ull = 100000000000000000; 
    printf("long long size: %lu\n", sizeof(ll));  /* operator, not a function, return the size of a variable */

    /* 
    
    c 1 byte <= short <= int <= long <= long long

    */

    /* float values */
    float f = 2.0f; /* 4 byte, end with f */
    double d = 100.10; /* 8 byte, does not end with f */


    /* string values */
    const char * st = "Heshdiaisdhiahsdllo";
    printf("%s\n", st);
    printf("st size: %lu\n", sizeof(st));

    /* int a = 20;  no redefinition of variable */

    /* -ansi C forbid redefinition of a in a loop
    for (int a = 0; a < 10; ++a) {
        printf("s");
    }
    */

    /* Always use a new variable name */
    printf("-------------- CONVERSION ----------------\n");

    float a = (float)5 / 2;
    printf("%.2f\n", a);

    /* / 如果左右都是整数，结果只能是整数
        但是如果左右两边精度不同，保留高精度的那个
     */

    /* 1000000000 is an integer literal, */

    long ci = (long)1000000000 * 5;
    printf("%ld\n", ci);
    /* VERY IMPORTANT: size of variable is very important... */

    printf("--------------- CONST --------------------\n");
    /* 
    防止别人或者自己修改你的变量
    */
    const int myNum = 15;  // myNum will always be 15
    /* myNum = 10; */ // error: assignment of read-only variable 'myNum'

    const int anotherint; /* IF YOU DO NOT ASSIGN, THIS WILL BE USELESS */

    /* anotherint = 5; */ 

    int inca = 10;
    printf("%d\n", ++inca);
    /* ++inca : 立刻在inca里面+1 */ /* inca = inca + 1; return inca */
    /* inca++ : 下一个操作再增加inca的值*/
    /* inca++ : T tempval = inca; inca = inca + 1; return tempval */

    /* ++ and -- have size effect, means they will change the value of the
       operand 
       
       c = a % 1 has no side effect on a, it has side effect on c
       a++ has side effect on a, value of a will change
    */

    /* 
     一个程序的生命分为两个时间：
     一个是compile time，就是编译时间, syntax error 语法错误
     一个是run time， 就是执行时间,    semantics error 语义错误， 需要assert帮你抓error
     */

    /* 
     int c = 1000000000 * 5;
     assert(c == (long long)5000000000) 如果你做了这个，就会立刻发现错误
    */

    /* 
        NULL / 0 / 0.0f / false: false
        others none zero number/ all strings / true: true

        in c, we only care about result, all results will be implicitly converted
        into a bool before we use it for if-else
        ""
     */

    /* 
        const char * st = "Hello"; 默认都是有一个额外的\0作为终止符
     */
    if (NULL) {
        printf("have panda\n");
    } else {
        printf("no panda");
    }

    /*
    
    ternary operator由一个输入和两个输出组成。它先对输入进行一个判定，如果输入判定成true
    就返回第一个值，否则返回第二个值
    
    */
    int da = 10;
    int db = 20;
    double dd = da > 5 ? 1.0 : db < 30 ? 10.0 : 20.0;

    // dd = 0.0;
    // if (da > 5) { // 1.0 
    //     dd = 1.0; 
    // } else { // db < 30 ? 10.0 : 20.0
    //     if (db < 30) { 
    //         dd = 10.0;
    //     } else {
    //         dd = 20.0;
    //     }
    // }


    int swa = 10;

    switch (swa) {
        case 1:
            printf("value of swa is 1\n"); // 如果你不写break，就会运行到下一个case
        case 10:
            printf("value of swa is 10\n");
            break; // 帮你从switch跳出来
        default:
            print("i don't know the value of swa\n");
    }

    /*

    www.bing.com
    
    1. use short to perform an overflow operation

    1.1 use char to achieve an underflow operation

    2. use int to achieve an underflow operation

    3. reading assignment
    read up on IEEE 754 floating point values, how does it work, 把3.5转换成一个32位浮点数
    0000 0000 0000 0000 0000 0000 0000 0000

    13.75

    13.9 只要精确到5位小数就好
    */
}