#include "helpers.h"
#include "math.h"
#include <stdio.h>

void swap(BYTE *a, BYTE *b);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;
            int red = image[i][j].rgbtRed;
            int average = round((blue + green + red) / 3.0);
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blue = image[i][j].rgbtBlue;
            int green = image[i][j].rgbtGreen;
            int red = image[i][j].rgbtRed;

            int blue_new = round(.272 * red + .534 * green + .131 * blue);
            int green_new = round(.349 * red + .686 * green + .168 * blue);
            int red_new = round(.393 * red + .769 * green + .189 * blue);

            if (blue_new > 255)
            {
                blue_new = 255;
            }
            if (green_new > 255)
            {
                green_new = 255;
            }
            if (red_new > 255)
            {
                red_new = 255;
            }

            image[i][j].rgbtBlue = blue_new;
            image[i][j].rgbtGreen = green_new;
            image[i][j].rgbtRed = red_new;

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            swap(&image[i][j].rgbtBlue, &image[i][width - j - 1].rgbtBlue);
            swap(&image[i][j].rgbtGreen, &image[i][width - j - 1].rgbtGreen);
            swap(&image[i][j].rgbtRed, &image[i][width - j - 1].rgbtRed);
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j].rgbtBlue = image[i][j].rgbtBlue;
            copy[i][j].rgbtGreen = image[i][j].rgbtGreen;
            copy[i][j].rgbtRed = image[i][j].rgbtRed;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int count = 0;
            float red_sum = 0;
            float blue_sum = 0;
            float green_sum = 0;
            for (int k = -1; k < 2; k++)
            {
                for (int m = -1; m < 2; m++)
                {
                    if (m + j >= 0 && m + j < width && k + i >= 0 && k + i < height)
                    {
                        red_sum += copy[i + k][j + m].rgbtRed;
                        blue_sum += copy[i + k][j + m].rgbtBlue;
                        green_sum += copy[i + k][j + m].rgbtGreen;
                        count++;
                    }
                }
            }
            int red_average = round(red_sum / count);
            int blue_average = round(blue_sum / count);
            int green_average = round(green_sum / count);

            image[i][j].rgbtBlue = blue_average;
            image[i][j].rgbtGreen = green_average;
            image[i][j].rgbtRed = red_average;
        }
    }
    return;
}


void swap(BYTE *a, BYTE *b)
{
    BYTE tmp = *a;
    *a = *b;
    *b = tmp;
}

