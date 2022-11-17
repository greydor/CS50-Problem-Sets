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

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{

    int index = hash(word);

    node *pointer = malloc(sizeof(node));
    pointer = table[index];
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
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
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
    node *temp = malloc(sizeof(node));
    node *pointer = malloc(sizeof(node));
    while (i <= N)
    {

        if (table[i] != NULL)
        {
            pointer->next = table[i]->next;
        }


        while (pointer->next != NULL)
        {
            temp->next = pointer->next;
            pointer->next = pointer->next->next;
            free(temp->next);
        }

        i++;
    }
    free(temp);
    free(pointer);
    return true;
}
