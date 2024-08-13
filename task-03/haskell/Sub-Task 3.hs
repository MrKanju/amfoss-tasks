main :: IO ()
main = do
    putStrLn "Enter the number of rows:"
    input <- getLine
    let rows = read input :: Int
    
    mapM_ (\i -> do
        putStr (replicate (rows-i-1) ' ')
        putStrLn (concat (replicate (i+1) "* "))
        ) [0..rows-1]

    mapM_ (\i -> do
        putStr (replicate (i+1) ' ') 
        putStrLn (concat (replicate (rows-i-1) "* ")) 
        ) [0..rows-2]
