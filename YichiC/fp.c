#include <stdio.h>

// int (*)(int, int) <- function signature
int add(int a, int b)
{
    return a + b;
}

int div(int a, int b)
{
    return a / b;
}

// int (*)(int, int, int)
int dunno(int b, int e, int f)
{
    return b - e + f;
}


int main()
{
    // F is a pointer to a function that takes in two integer and returns one integer
    int (*F)(int, int) = dunno;

    printf("%d\n", F(1, 2));
    return 0;
}