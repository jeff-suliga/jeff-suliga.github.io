#include <stdio.h>
#include <unistd.h>
#include <termios.h>
#include <sys/time.h>

#define BITLIMIT 10000

// For Windows, GetSystemTime() is what you want. For POSIX, gettimeofday()

static char letters[36] = {'a', 'b', 'c', 'd', 'e', 'f',
                            'g', 'h', 'i', 'j', 'k',
                            'l', 'm', 'n', 'o', 'p',
                            'q', 'r', 's', 't', 'u',
                            'v', 'w', 'x', 'y', 'z',
                            '1', '2', '3', '4', '5',
                            '6', '7', '8', '9', '0'
}; 

// 0 for dit, 1 for dah
static char* codes[36] = {"01", "1000", "1010", "100", "0", "0010",
                "110",      "0000",     "00",       "0111",     "101",
                "0100",     "11",       "10",       "111",      "0110",
                "1101",     "010",      "000",      "1",        "001",
                "0001",     "011",      "1001",     "1011",     "1100",
                "01111",    "00111",    "00011",    "00001",    "00000",
                "10000",    "11000",    "11100",    "11110",    "11111"
};

int main()
{
    printf("This will accept up to %d morse inputs, including spaces between words.\n", BITLIMIT);
    printf("Clicks of the spacebar cannot be under 0.3s of one another.\n");
    printf("Clicks from 0.3 to 0.6 seconds apart will register as \'*\'\n");
    printf("Clicks from 0.6 to 1 seconds apart will register as \'-\'\n");
    printf("Remember to add a \'*\' at the very end!\n");
    printf("Type \'x\' to end.\n\n");
    printf("Listening...\n");
    
    char inputs[BITLIMIT + 1];
    
    struct timeval current_time;
    gettimeofday(&current_time, NULL);
    long last_sec = current_time.tv_sec;
    long last_usec = current_time.tv_usec;

    char c;
    static struct termios oldt, newt;
    double elapsed;
    int idx = 0;

    /*tcgetattr gets the parameters of the current terminal
    STDIN_FILENO will tell tcgetattr that it should write the settings
    of stdin to oldt*/
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;

    /*ICANON normally takes care that one line at a time will be processed
    that means it will return if it sees a "\n" or an EOF or an EOL*/
    newt.c_lflag &= ~(ICANON | ECHO);

    /*Those new settings will be set to STDIN
    TCSANOW tells tcsetattr to change attributes immediately. */
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);


    int spaces = 0;
    /*I choose 'e' to end input. Notice that EOF is also turned off
    in the non-canonical mode*/
    while((c=getchar()) != 'x') {
        if (c == ' ') {
            gettimeofday(&current_time, NULL);
            elapsed = (current_time.tv_sec - last_sec) + ((double)current_time.tv_usec - last_usec) / 1000000;
            if (elapsed < 0.3) { // Too fast
                // printf("HOLDING");
                continue;
            }
            else if (elapsed < 0.6) {
                inputs[idx++] = '*';
            }
            else if (elapsed <= 1.0) {
                inputs[idx++] = '-';
            }
            else {
                inputs[idx++] = '/';
            }
            last_sec = current_time.tv_sec;
            last_usec = current_time.tv_usec;
            // printf("Elapsed time since start: %lf\n", elapsed);
            // printf("Elapsed time since last space: %lf\n", elapsed);
            spaces++;
        }
    }
    
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);
    
    printf("You clicked the spacebar %d times.\n", spaces);
    
    printf("idx: %d\n", idx);
    inputs[idx++] = '\0';
    printf("Entered string: %s\n\n", inputs);
    
    return 0;
}