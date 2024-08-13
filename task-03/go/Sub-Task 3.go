package main

import (
    "fmt"
    "strconv"
)

func main() {
    var input string
    fmt.Print("Enter the number of rows: ")
    fmt.Scanln(&input)
    rows, err := strconv.Atoi(input)
    if err != nil || rows <= 0 {
        fmt.Println("Please enter a valid positive number.")
        return
    }
    for i := 0; i < rows; i++ {
        for j := 0; j < rows-i-1; j++ {
            fmt.Print(" ")
        }
        for j := 0; j <= i; j++ {
            fmt.Print("* ")
        }
        fmt.Println()
    }
    for i := 0; i < rows-1; i++ {
        for j := 0; j <= i; j++ {
            fmt.Print(" ")
        }
        for j := 0; j < rows-i-1; j++ {
            fmt.Print("* ")
        }
        fmt.Println()
    }
}

