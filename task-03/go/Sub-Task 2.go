package main

import (
    "fmt"
    "io/ioutil"
    "os"
)

func main() {
    inputData, err := ioutil.ReadFile("input.txt")
    if err != nil {
        fmt.Println("Error reading input file:", err)
        os.Exit(1)
    }

    err = ioutil.WriteFile("output.txt", inputData, 0644)
    if err != nil {
        fmt.Println("Error writing to output file:", err)
        os.Exit(1)
    }

    fmt.Println("String has been written to output.txt")
}
