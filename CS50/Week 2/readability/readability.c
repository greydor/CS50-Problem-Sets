#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);
int readability_index(int sentences, int words, int letters);


int main(void)
{

    string text = get_string("Enter text: ");

    int sentences = count_sentences(text);
    // printf("Sentences: %i\n", sentences);

    int letters = count_letters(text);
    // printf("Letters: %i\n", letters);

    int words = count_words(text);
    // printf("Words: %i\n", words);

    int index = readability_index(sentences, words, letters);
    // printf("Index: %i\n", index);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 1 && index <= 15)
    {
        printf("Grade %i\n", index);
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }


}


int count_sentences(string text)
{

    int i = 0;
    int sentences = 0;
    while (text[i] != '\0')
    {
        if (text[i] == '.' || text[i] == '?' || text[i] == '!')
        {
            sentences++;
        }
        i++;
    }
    return sentences;
}

int count_letters(string text)
{

    int i = 0;
    int letters = 0;
    while (text[i] != '\0')
    {
        if (isalpha(text[i]))
        {
            letters++;
        }
        i++;
    }
    return letters;
}

int count_words(string text)
{

    int i = 0;
    int words = 1;
    while (text[i] != '\0')
    {
        if (text[i] == ' ')
        {
            words++;
        }
        i++;
    }
    return words;
}

int readability_index(int sentences, int words, int letters)
{
    float S = (float)sentences / ((float)words / 100);
    float L = (float)letters / ((float)words / 100);
    int index =  round(0.0588 * L - 0.296 * S - 15.8);
    return index;
}