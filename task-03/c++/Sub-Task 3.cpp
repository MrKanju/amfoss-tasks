#include <iostream>

int main() {
    int rows;
    std::cout << "Enter the number of rows: ";
    std::cin >> rows;

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < rows - i - 1; j++) {
            std::cout << " ";
        }
        for (int j = 0; j < i + 1; j++) {
            std::cout << "* ";
        }
        std::cout << std::endl;
    }

    for (int i = 0; i < rows - 1; i++) {
        for (int j = 0; j < i + 1; j++) {
            std::cout << " ";
        }
        for (int j = 0; j < rows - i - 1; j++) {
            std::cout << "* ";
        }
        std::cout << std::endl;
    }

    return 0;
}
