#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;
    while (true)
    {
        height = get_int("Type a number: ");
        if (height >= 1 && height <= 8)
        {
            break;
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j <= height - i - 2; j++)
        {
            printf(" ");
        }
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("  ");
        for (int j = 0; j <= i; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}