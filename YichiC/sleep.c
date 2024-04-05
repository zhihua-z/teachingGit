#include <stdio.h>
#include <unistd.h> // Header file for sleep function
#include <signal.h>

void printkk(int sigval)
{
    printf("kk\n");
}

int main() {
    printf("sleeping...\n");
    signal(SIGUSR1, printkk);

    while (1)
    {
        sleep(5); // Pause execution for 5 seconds
        printf("I woke up a bit\n");
    }
    printf("Finished waiting!\n");
    return 0;
}
