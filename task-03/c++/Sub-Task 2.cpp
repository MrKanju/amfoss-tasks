#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream inputFile("input.txt");
    std::ofstream outputFile("output.txt");

    if (!inputFile || !outputFile) {
        return 1;
    }

    std::string line;
    while (std::getline(inputFile, line)) {
        outputFile << line << std::endl;
    }

    return 0;
}
