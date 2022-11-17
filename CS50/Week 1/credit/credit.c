#include <cs50.h>
#include <stdio.h>
#include <math.h>

int main(void)
{
    long credit = get_long("Type a number: ");
    int sum = 0;
    int i = 0;
    int x, y;
    while (i <=16)



    {
        long num = credit / (pow(10, i));
        if (num == 0)
        {
            break;
        }
        y = x;
        x = num % 10;
        if (i % 2 == 0)
        {
            sum += x;
        }
        else
        {

            if (x * 2 >= 10)
            {
                int x1 = x * 2 % 10;
                int x10 = x * 2 / 10;
                sum += x10 + x1;
            }
            else
            {
                sum += x * 2;
            }
        }
        i++;
    }

    // Calculate first two digits
    int starting = 10 * x + y;

    // printf("i = %i\n", i);
    // printf("sum = %i\n", sum);
    int remainder = sum % 10;

    if (remainder == 0)
    {
        // Check if Visa card
        if ((i == 13 || i == 16) && x == 4)
        {
            printf("VISA\n");
        }
        // Check for AMEX card
        else if (i == 15 && (starting == 34 || starting == 37))
        {
            printf("AMEX\n");
        }
        // Check for Mastercard card
        else if (i == 16 && (starting == 51 || starting == 52 || starting == 53 || starting == 54 || starting == 55))
        {
            printf("MASTERCARD\n");
        }
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }





}