open System

let isPalindrome (text: string) : bool =
    let cleanedText = text.ToLower().Replace(" ", "").Replace("\t", "")
    cleanedText = String(cleanedText.ToCharArray() |> Array.rev)

[<EntryPoint>]
let main argv =
    printfn "Podaj tekst:"
    let input = Console.ReadLine()
    if isPalindrome input then
        printfn "Podany ciąg jest palindromem"
    else
        printfn "Podany ciąg nie jest palindromem"
    0
