#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <ctype.h>

int only_digits(string text);
string rotate_message(string message, int key);

int main(int argc, string argv[])
{

    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    if (only_digits(argv[1]) != 1)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    string message = get_string("plaintext: ");
    int key = atoi(argv[1]);
    message = rotate_message(message, key);
    printf("ciphertext: %s\n", message);

    return 0;
}




int only_digits(string text)
{
    int i = 0;
    while (text[i] != '\0')
    {
        if (isdigit(text[i]) == 0)
        {
            return 0;
        }
        i++;
    }
    return 1;


}

string rotate_message(string message, int key)
{
    int i = 0;
    while (message[i] != '\0')
    {
        if (!isalpha(message[i]))
        {
            ;
        }
        else if (islower(message[i]))
        {
            message[i] = 97 + (message[i] + key - 97) % 26;

        }
        else
        {
            message[i] = 65 + (message[i] + key - 65) % 26;
        }
        i++;
    }
    return message;
}
