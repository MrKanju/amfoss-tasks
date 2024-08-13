package main

import (
    "fmt"
    "io/ioutil"
    "strconv"
    "strings"
)

func main() {
    inputData, err := ioutil.ReadFile("input.txt")
    if err != nil {
        fmt.Println("Error reading input file:", err)
        return
    }

    inputString := strings.TrimSpace(string(inputData))
    rows, err := strconv.Atoi(inputString)
    if err != nil || rows <= 0 {
        fmt.Println("Please ensure the input is positive number.")
    }

    var diamond strings.Builder

    for i := 0; i < rows; i++ {
        for j := 0; j < rows-i-1; j++ {
            diamond.WriteString(" ")
        }
        for j := 0; j <= i; j++ {
            diamond.WriteString("* ")
        }
        diamond.WriteString("\n")
    }
    for i := 0; i < rows-1; i++ {
        for j := 0; j <= i; j++ {
            diamond.WriteString(" ")
        }
        for j := 0; j < rows-i-1; j++ {
            diamond.WriteString("* ")
        }
        diamond.WriteString("\n")
    }

    err = ioutil.WriteFile("output.txt", []byte(diamond.String()), 0644)
    if err != nil {
        fmt.Println("Error writing to output file:", err)
        return
    }

    fmt.Println("Diamond pattern has been written to output.txt")
}
