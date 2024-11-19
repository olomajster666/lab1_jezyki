// Funkcja rekurencyjna do generowania permutacji listy
let rec permutations list =
    match list with
    | [] -> [[]]
    | _ -> 
        list 
        |> List.collect (fun x -> 
            let rest = List.filter ((<>) x) list
            permutations rest |> List.map (fun perm -> x :: perm))

// Funkcja główna programu
[<EntryPoint>]
let main argv =
    // Przykładowa lista
    let numbers = [1; 2; 3]
    let perms = permutations numbers

    printfn "Permutacje listy %A:" numbers
    perms |> List.iter (fun perm -> printfn "%A" perm)

    0
