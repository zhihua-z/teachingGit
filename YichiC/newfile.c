
// 让你的编译器在查找printf的时候，不仅仅查找当前文件，也查找include的文件
// it instruct your compiler where to look up to this function: printf
// C look up order: local scope -> global scope -> include scope
#include <stdio.h>

// 定义一个宏，在preprocessing的时候扫一遍你的代码，把WAAKAKKA全部替换成它的值
// 这个宏不存在于内存中，不是变量，没有地址，甚至都不是C代码。就是一个替换指令
#define WAAKAKKA "hello world!\n"

#define MAX 10
#define EXTRA 5

#define TOTAL (MAX + EXTRA)

#define min(a,b) ((a) < (b) ? (a):(b))


void print_debug_info()
{
    printf("\n\ndebug\n\n");
}

int main()
{
    for (int i = 0; i < MAX; ++i)
    {
        printf(WAAKAKKA);
#if a > 5
        print_debug_info();
#endif
    }


    printf("%d\n", min(1, 2));
}

