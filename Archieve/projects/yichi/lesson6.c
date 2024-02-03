#include <stdio.h>
#include <stdlib.h>
#include "utils.h"

/*
    Alignment of a structure is only determined by the primitive types
*/
struct AA {
    double a; // size of a is 8 
    char name[30]; // size of name is 30 (will not be the alignment of this struct)
};

struct Student {
    char name[30];
    int age;
};

int main() {
    const char * sss = "Happy birthday!";
    char arr[20] = "";

    mystrcpy(arr, sss);
    printf("%d\n", mystrlen(sss));
    printf("%s\n", arr);


    /* constness of pointers 
    
        adding qualifier is ok
        removing qualifier is not ok

        char * pp;

        const char * cpp = pp; // ok

        char * mpp = cpp;      // not ok
    
    */

    char name[] = "Yichi";
    int length = mystrlen(name);

    myreverse(name);

    printf("%s\n", name);

    struct AA a1;
    printf("%d\n", sizeof(struct Student));
    struct AA a2;

    printf("%p\n%p\n", &a1, &a2);


    // C arrays are static, so we need a more dynamic solution
    struct Student smallerStudent[20] = {};
    struct Student students[100] = {};

    /*       DYNAMIC ALLOCATION        */

    /* malloc is handy for this
    malloc : memory allocation, means you want a chunk of memory from heap
    
    if you do malloc, the memory will be reserved, however, it doesn't auto clear

    if you do not want to use that memory anymore, you have to do free on that memory

    否则这块内存就永远被锁着了，直到你重启app
    */

    // malloc(10) means I want to reserve 10 bytes for me: malloc(10)
    // and use it as a char *:   (char *)
    char * myname = (char *)malloc(10);

    // now you can treat myname as an array of 10 elements
    myname[0] = 'h';
    myname[1] = 'a';
    myname[10] = 'a';

    printf("%s\n", myname);

    // 我觉得不够，需要30个byte
    free(myname);
    myname = (char *) malloc(30);



    // this will release the memory allocated to myname
    free(myname);

    /*
    
    用dynamic allocation非常的危险，因为一个不小心你就会写到你申请到的内存的外面去。
    如果那个地方没有数据，那么暂时没问题
    1. 但是这个地方随时可能会被别的malloc分配走，别的地方往这里写数据的话，你的数据就没了


    比如你申请了0x100，10个byte，所以0x100 - 0x109 这10个byte都是你的
    然后你写了一串子，"hello world"，这个会占用0x100 - 0x 10b，一共12个byte（null terminator）

    然后另一段代码申请了malloc，分到了0x10a到0x11a这17个byte
    然后那个代码写了一些别的东西，你的这个“hello world”里的d和null terminator就没了。

    所以可能你的程序运行了一会儿以后，之前都是打印hello world，然后忽然开始打印 hello worl%&@&*@*^!@^*!&^!^!

    那你就应该知道是内存被覆盖掉了。

    2. 如果你不小心写到了你申请到的内存的外面，然后那个地方刚好是你的操作系统重要的数据，你就直接蓝屏。

    3. 如果你不小心覆盖到别的内存，那个地方是某一个值，本来是1，被你变成了2，你的程序将不会出现任何问题，直到你使用那个值。这时候，你就要查你的程序里所有的malloc和被分配了内存的object的使用方式。（除非，你使用visual studio code的breakpoint debugger，这个breakpoint可以监控一段内存，然后在这个内存被修改的瞬间暂停你的程序，然后把你的cpu里当前正在运行的function，和它全部的上层function都找出来。）

    这种事情我们都叫他undefined behavior
    
    */

    /*
    Assignment: 
    问用户输入一个数字，
    根据用户输入的数字，做出一个array of Students

    然后对于每一个学生，都问用户要他的名字和年龄

    sample output:
    please enter number of students: 3

    please enter name of student 1: Zhihua
    please enter his/her age: 15
    information saved, (Zhihua, 15)

    please enter name of student 2: Yichi
    please enter his/her age: 12
    information saved, (Yichi, 12)

    please enter name of student 3: James
    please enter his/her age: 1
    information saved, (James, 1)
    
    All information acquired:
    Zhihua, 15
    Yichi, 12
    James, 1
    */


    return 0;
}
