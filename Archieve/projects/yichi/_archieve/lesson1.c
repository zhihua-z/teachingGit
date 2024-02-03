/*
  multiple line
*/
#include <stdio.h> 
#include <stdlib.h>
#include <assert.h>
/* 
    # stands for pre-processor command
    https://www.tutorialspoint.com/cprogramming/c_preprocessors.htm

    #include means copy the content of that file here

    <> stands for system file / library files

    #include "myfile.h"  < "" double quotation

    stdio.h   .h stands for header file (store your declarations)
              .c stands for c implementation file

    .h is like interface in java, a file full of interfaces...

    stdio.h < standard input output library file from c language standard
*/

struct MyChessboard{
  int board[14][14];
};

void foo(int a) {
  printf("%d\n", a);
}

void myassert(int expression, const char* msg) {
  if (!expression) {
    printf("[ASSERTION ERROR] %s\n", msg);
    /* exit(1); this is not recommended */
  }
}

/* complex C declaration : TODO */

int main(void) {
    int a = 110;
    int i;
    unsigned mystate = 0;
    struct MyChessboard haha;
    /* int in_a; */

    printf("hello world!\n");
    printf("hello world!\n");
    printf("value of a is %-10d%-10d\n", a, a * 2);
    printf("%e\n", (float)a);
    /* c format specifier */

    for (i = 0; i < 10; ++i) {
      printf("%d\n", i);
    }

    /*
    scanf("%d", &in_a); 
    printf("%d\n", in_a);
    myassert(in_a == 5, "did not type 5");
    */
    /* & reference operator, address of operator */
    /* if you want to read a %d into your value in_a, c will not check
      if it is an integer or not, it will just read whatever is there, 4 byte

      %d is just telling c compiler to read 4 byte and read it as an integer
     */


    /* 
      we are using bitwise operator here
      >> << is called shift operator, it means bit shiftfing
      11 >> 1 => 1
      11 << 1 => 1100
      11 << 3 => 11000

      8: 1000
      5: 0101

      8 & 5 : 1000 AND 0101 => 0000
     */
    printf("-----------\n");
    printf("%d\n", ~10);
    printf("-----------\n");

    /*
    0000...0001010 10
    1111...1110110 -10
    1111...1110101 -11
    0000...0001011 11*/

    /*
    int : signed integer, half negative, half non-negative, implemented with 
          2's complement 
    unsigned : unsigned integer, all positive, plain old binary implementation
    */

    /* front, right, back, left 8 (1000) 4(100) 2(10) 1(1) */
    /* if I'm walking front */
    mystate |= 8;

    /* if I'm walking left at the same time */
    mystate |= 1;

    printf("state: %d\n", mystate); /* 1001 means I'm walking front and left */

    foo(a);
    return 0; /* return 0 means exist without error */
}
