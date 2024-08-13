import System.IO

main :: IO ()
main = do
    let content="jhbuhebfurgfyugrwfryfgyurgfyrgf"
    writeFile "input.txt" content
    inputFile <- readFile "input.txt"
    writeFile "output.txt" inputFile
    outputFile <- readFile "input.txt"
    putStrLn "Content of output.txt:"          
    putStrLn outputFile  
