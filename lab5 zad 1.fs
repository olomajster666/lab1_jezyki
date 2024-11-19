// Definicja funkcji rekurencyjnej dla ciągu Fibonacciego
let rec fib n =
    if n <= 1 then n
    else fib (n - 1) + fib (n - 2)

// Definicja funkcji zoptymalizowanej z ogonową rekurencją
let fibTailRec n =
    let rec aux a b n =
        if n = 0 then a
        else aux b (a + b) (n - 1)
    aux 0 1 n

// Funkcja główna programu
[<EntryPoint>]
let main argv =
    printfn "Rekurencyjne obliczanie ciągu Fibonacciego:"
    printfn "fib(10) = %d" (fib 10)
    printfn "fibTailRec(10) = %d" (fibTailRec 10)
    
    printfn "fib(15) = %d" (fib 15)
    printfn "fibTailRec(15) = %d" (fibTailRec 15)
    
    0
