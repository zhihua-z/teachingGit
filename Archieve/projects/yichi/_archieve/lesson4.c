#include <stdio.h>

int main() {

    /* memory alignment of variables */
    int some = 1;
    int * psome = &some;
    int num = 10; // 0x358
    int fillpadding = 5;
    char c = 5;
    int* pnum = &num; // 0x354 ??   0x350 ????????????
    int ** ppnum = &pnum;

    printf("%p : some\n", psome); // address of some
    printf("%p : psome\n", &psome); // address of psome
    printf("%p : num\n", pnum);  // address of num
    printf("%p : fillpadding\n", &fillpadding);  // address of fillpadding
    printf("%p : c\n", &c);
    printf("%p : pnum\n", ppnum); // address of pnum
    printf("%p : ppnum\n", &ppnum);  // address of ppnum

    /*  
        0x16dbf7358
        0x16dbf7350
        0x16dbf7348

        it goes down because stack is growing downwards
    */

    /*
        Memory Alignment 内存对齐

        每一个变量的起始位置必须放在自己的大小的倍数上
        所以pnum就不能被放在0x354上，只能0x350上
        那0x354, 0x353, 0x352, 0x351 就浪费了

        0x330  <- address of ppnum
        0x331
        0x332
        0x333
        0x334  
        0x335
        0x336
        0x337  <- last byte of ppnum
        0x338  <- address of pnum
        0x339
        0x33a
        0x33b
        0x33c
        0x33d
        0x33e
        0x33f  <- last byte of pnum
        0x340  ||
        0x341  ||
        0x342  ||
        0x343  ||
        0x344  ||
        0x345  ||
        0x346  ||
        0x347  <- char c
        0x348  <------ first byte of fillpadding
        0x349  
        0x34a  
        0x34b  <------ last byte
        0x34c  <- first byte of num
        0x34d
        0x34e
        0x34f  <- last byte of num
        0x350  <- first byte of psome
        0x351
        0x352
        0x353
        0x354
        0x355
        0x356
        0x357  <- last byte of psome
        0x358  <- first byte of some
        0x359  <- second byte of some
        0x35a  <- third byte of some
        0x35b  <- fourth byte of some
        0x35c

    address of stack goes down...
    memory address of bytes of variables goes up

    this confusion only happens in BIG ENDIAN machines

    ENDIAN....big endian, little endian...

    0x12345678  : num : int  0x100

    0x100 | 0x12         | 0x78
    0x101 | 0x34         | 0x56
    0x102 | 0x56         | 0x34
    0x103 | 0x78         | 0x12
            big endian     little endian

    Big Endian: 
        most significant byte stored in smallest address
        least significant byte stored in largest address

    Little Endian:
        most significant byte stored in largest address
        least significant byte stored in smallest address

    0x0     0x1     0x2     0x3
   |        ssssssssssssssss
   |000011110000111100001111000011110000111100001111|
   |^       ^           ^                           | 1 bit fetching
   |__  __  __  __                                  | 2 bit
   |''''    ''''    ''''                            | 4 bit 
   |~~~~~~~~        ~~~~~~~~                        | 1 byte
   |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                | 2 byte


    if memory is not aligned, my short can be placed on 0x1
    so it occupies 0x1, 0x2 bytes

    to read this short, I have two plans
      1. use a 2 byte fetcher to read 0x0, 0x2, get upperhalf of 0x0, lowerhalf 0x2
      2. use a 1 byte fetcher fetch 0x1, 1 byte fetcher fetch 0x2

    without memory alignment, we might use mutiple times to read one number
    with memory alignment, we just need one fetch
    */

   



    return 0;
}