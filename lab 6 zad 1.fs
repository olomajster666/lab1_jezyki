open System

let countWords (text: string) : int =
    text.Split([|' '; '\t'; '\n'|], StringSplitOptions.RemoveEmptyEntries).Length

let countCharsWithoutSpaces (text: string) : int =
    text.Replace(" ", "").Length

[<EntryPoint>]
let main argv =
    printfn "Podaj tekst:"
    let input = Console.ReadLine()
    let wordCount = countWords input
    let charCount = countCharsWithoutSpaces input
    printfn "Liczba słów: %d" wordCount
    printfn "Liczba znaków (bez spacji): %d" charCount
    0
