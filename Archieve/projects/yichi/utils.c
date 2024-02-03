#include "utils.h"

void mystrcpy(char * destination, const char * source) {
    // 从source一个一个的抄，直到看到一个\0

    const char * curr = source;

    while (*curr != '\0') {
        *destination++ = *curr++;
    }

    
}

int mystrlen(const char * target){
    int index = 0;
    const char* start = target;
    if (*target == 0) return 0;

    while (*(++target) != '\0'){
    }

    return target - start;
}


void myswap(char* a, char* b) {
    char temp = *a;
    *a = *b;
    *b = temp;
}

void myreverse(char * input) {
    int length = mystrlen(input);
    int i = 0;

    for (i = 0; i < length / 2; ++i) {
        myswap(input + i, input + length - 1 - i);
    }
}
