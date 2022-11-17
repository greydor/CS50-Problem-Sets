#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 4;
    }

    BYTE buffer[512];
    int count = 0;
    char out_file_name[8];
    while (fread(buffer, 1, 512, file) == 512)
    {
        if ((buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff) &&
        (buffer[3] >= 0xe0 && buffer[3] <= 0xef))
        {
            int x = count % 10;
            int y = (count / 10) % 10;
            sprintf(out_file_name, "0%i%i.jpg", y, x);

            count++;
        }
        FILE *out_file = fopen(out_file_name, "w");
        if (file == NULL)
        {
            printf("Could not open %s.\n", out_file_name);
            return 4;
        }
        fwrite(buffer, 1, 512, out_file);
        fclose(out_file);


    }





    fclose(file);
}