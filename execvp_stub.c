#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
 
char *script[] = {"python", "-c", "print \"Hello World\""};
char *test[] = {"python", "-m", "SimpleHTTPServer"};
 
void main(int argc, char *argv[])
{
    int i;
 
    printf("Attempt to Execv.\n");
    //i = execvp(test[0], test);
    i = execvp(script[0], script);
    if (i == -1)
    {
        printf("Execv failed.\n");
    }
}
