#include <errno.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

FILE* open_file(const char* filepath)
{
    errno = 0;
    
    FILE *fp = fopen(filepath, "r");



    if (errno != 0) printf("%s\n", strerror(errno));
    exit(errno);
    return fp;
}

int main()
{
    errno = 0;
    FILE * fp = open_file("does not exist");
    printf("here I am\n");
    
    return 0;
}