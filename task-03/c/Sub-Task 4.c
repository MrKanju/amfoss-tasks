#include <stdio.h>

int main() {
    FILE *inputFile, *outputFile;
    int rows, i, j;

    inputFile = fopen("input.txt", "r");
    outputFile = fopen("output.txt", "w");

    if (inputFile == NULL || outputFile == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    fscanf(inputFile, "%d", &rows);

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < rows - i - 1; j++) {
            printf(" ");
        }
        for (int j = 0; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }

    for (int i = 0; i < rows - 1; i++) {
        for (int j = 0; j <= i; j++) {
            printf(" ");
        }
        for (int j = 0; j < rows - i - 1; j++) {
            printf("* ");
        }
        printf("\n");
    }

    fclose(inputFile);
    fclose(outputFile);

    return 0;
}
