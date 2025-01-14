open System

let transformEntry (entry: string) : string =
    let parts = entry.Split(';') |> Array.map (fun x -> x.Trim())
    if parts.Length = 3 then
        let firstName = parts.[0]
        let lastName = parts.[1]
        let age = parts.[2]
        sprintf "%s, %s (%s lat)" lastName firstName age
    else
        "Nieprawidłowy format danych"

[<EntryPoint>]
let main argv =
    printfn "Wprowadź wpisy w formacie 'imię; nazwisko; wiek', oddzielając je nowymi liniami. Aby zakończyć, naciśnij Enter na pustej linii."
    let rec readEntries acc =
        let input = Console.ReadLine()
        if String.IsNullOrWhiteSpace(input) then acc
        else readEntries (input :: acc)
    let entries = readEntries [] |> List.rev
    let transformedEntries = entries |> List.map transformEntry
    printfn "Przetworzone dane:"
    transformedEntries |> List.iter (printfn "%s")
    0
