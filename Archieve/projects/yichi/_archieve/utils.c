#include "utils.h"

void mystrcpy(char * destination, const char * source) {
    // 从source一个一个的抄，直到看到一个\0

    const char * curr = source;

    while (*curr != '\0') {
        *destination = *curr;
        destination++;
        curr++;
    }
}

