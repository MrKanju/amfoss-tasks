#include <iostream>
#include <fstream>

int main() {
    std::ifstream inputFile("input.txt");
    std::ofstream outputFile("output.txt");

    if (!inputFile || !outputFile) {
        return 1;
    }

    int rows;
    inputFile >> rows;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < rows - i - 1; j++) {
            outputFile << " ";
        }
        for (int j = 0; j < i + 1; j++) {
            outputFile << "* ";
        }
        outputFile << std::endl;
    }

    for (int i = 0; i < rows - 1; i++) {
        for (int j = 0; j < i + 1; j++) {
            outputFile << " ";
        }
        for (int j = 0; j < rows - i - 1; j++) {
            outputFile << "* ";
        }
        outputFile << std::endl;
    }

    return 0;
}
