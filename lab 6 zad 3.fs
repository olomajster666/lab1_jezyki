open System

let removeDuplicates (words: string list) : string list =
    words |> List.distinct

[<EntryPoint>]
let main argv =
    printfn "Podaj słowa oddzielone spacjami:"
    let input = Console.ReadLine()
    let words = input.Split(' ') |> Array.toList
    let uniqueWords = removeDuplicates words
    printfn "Lista unikalnych słów: %A" uniqueWords
    0
