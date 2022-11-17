// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "dictionary.h"
#include <strings.h>

int word_count = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 10000;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int index = hash(word);


    node *pointer = table[index];
    while (pointer != NULL)
    {
        if (strcasecmp(pointer->word, word) == 0)
        {

            return true;
        }
        pointer = pointer->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{

    int i = 0;
    int sum = 0;
    while (word[i] != '\0')
    {
        if (i < 4)
        {
            sum += (toupper(word[0]) - 'A') * 26 * (i + 1);
        }
        else
        {
            sum += (toupper(word[0]) - 'A');
        }
        i++;
    }
    return sum;

}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *file = fopen(dictionary, "r");
    if (file == NULL)
    {
        return false;
    }
    char word[45];
    while (fscanf(file, "%s", word) != EOF)
    {
        word_count++;
        node *n = malloc(sizeof(node));
            if (n == NULL)
            {
                return false;
            }
        strcpy(n->word, word);
        int index = hash(word);
        n->next = table[index];
        if (table[index] != NULL)
        {
            n->next = table[index]->next;
            table[index]->next = n;
        }
        else
        {
            table[index] = n;
        }
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    int i = 0;
    node *pointer = NULL;
    node *temp = pointer;
    while (i <= N)
    {
        if (table[i] != NULL)
        {
            pointer = table[i];
        }
        while (pointer != NULL)
        {
            temp = pointer;
            pointer = pointer->next;
            free(temp);
        }
        i++;
    }
    return true;
}
