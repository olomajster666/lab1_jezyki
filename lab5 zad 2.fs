// Definicja drzewa binarnego
type BinaryTree<'T> =
    | Empty
    | Node of 'T * BinaryTree<'T> * BinaryTree<'T>

// Funkcja rekurencyjna wyszukiwania w drzewie binarnym
let rec searchTree value tree =
    match tree with
    | Empty -> false
    | Node(v, left, right) ->
        if v = value then true
        else searchTree value left || searchTree value right

// Iteracyjne wyszukiwanie w drzewie binarnym
let searchTreeIter value tree =
    let rec loop stack =
        match stack with
        | [] -> false
        | Empty :: rest -> loop rest
        | Node(v, left, right) :: rest ->
            if v = value then true
            else loop (left :: right :: rest)
    loop [tree]

// Funkcja główna programu
[<EntryPoint>]
let main argv =
    // Przykładowe drzewo
    let myTree = Node(10, Node(5, Empty, Empty), Node(20, Empty, Node(25, Empty, Empty)))
    
    printfn "Rekurencyjne wyszukiwanie:"
    printfn "Czy wartość 25 jest w drzewie? %b" (searchTree 25 myTree)
    printfn "Czy wartość 15 jest w drzewie? %b" (searchTree 15 myTree)

    printfn "Iteracyjne wyszukiwanie:"
    printfn "Czy wartość 25 jest w drzewie? %b" (searchTreeIter 25 myTree)
    printfn "Czy wartość 15 jest w drzewie? %b" (searchTreeIter 15 myTree)

    0