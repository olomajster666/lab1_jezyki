open System

let findLongestWord (text: string) : string * int =
    text.Split([|' '; '\t'; '\n'|], StringSplitOptions.RemoveEmptyEntries)
    |> Array.fold (fun (longestWord, maxLength) word ->
        if word.Length > maxLength then (word, word.Length)
        else (longestWord, maxLength)
    ) ("", 0)

[<EntryPoint>]
let main argv =
    printfn "Podaj tekst:"
    let input = Console.ReadLine()
    let longestWord, length = findLongestWord input
    printfn "Najdłuższe słowo: %s" longestWord
    printfn "Długość najdłuższego słowa: %d" length
    0