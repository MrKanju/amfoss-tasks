#include <stdio.h>

int main() {
    FILE *inputFile = fopen("input.txt", "r");
    FILE *outputFile = fopen("output.txt", "w");

    if (inputFile == NULL || outputFile == NULL) {
        return 1;
    }

    char c;
    while ((c = fgetc(inputFile)) != EOF) {
        fputc(c, outputFile); 
    }

    fclose(inputFile);
    fclose(outputFile);

    return 0;
}
