// Funkcja rekurencyjna do rozwiązania problemu wież Hanoi
let rec hanoi n source target auxiliary =
    if n = 1 then
        printfn "Przenieś krążek z %s do %s" source target
    else
        hanoi (n - 1) source auxiliary target
        printfn "Przenieś krążek z %s do %s" source target
        hanoi (n - 1) auxiliary target source

// Funkcja iteracyjna do rozwiązania problemu wież Hanoi
let hanoiIter n source target auxiliary =
    let moves = pown 2 n - 1
    for i in 1 .. moves do
        let fromPeg = 
            match (i &&& i - 1) % 3 with
            | 0 -> source
            | 1 -> auxiliary
            | _ -> target
        let toPeg = 
            match ((i ||| i - 1) + 1) % 3 with
            | 0 -> source
            | 1 -> auxiliary
            | _ -> target
        printfn "Przenieś krążek z %s do %s" fromPeg toPeg

// Funkcja główna programu
[<EntryPoint>]
let main argv =
    let n = 3 // Liczba krążków
    printfn "Rekurencyjne rozwiązanie problemu wież Hanoi:"
    hanoi n "A" "C" "B"

    printfn "\nIteracyjne rozwiązanie problemu wież Hanoi:"
    hanoiIter n "A" "C" "B"

    0
