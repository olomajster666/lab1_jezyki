import numpy as np


def add_matrices(A, B):
    if A.shape != B.shape:
        raise ValueError("Macierze muszą mieć te same wymiary do dodawania.")
    return A + B


def multiply_matrices(A, B):
    if A.shape[1] != B.shape[0]:
        raise ValueError("Liczba kolumn pierwszej macierzy musi być równa liczbie wierszy drugiej.")
    return A @ B


def transpose_matrix(A):
    return A.T


def execute_matrix_operation(operation_str, matrices):
    operations = {
        '+': add_matrices,
        '@': multiply_matrices,
        'T': transpose_matrix
    }

    try:
        if 'T' in operation_str:
            matrix_name = operation_str.replace('T', '').strip()
            matrix = matrices[matrix_name]
            return transpose_matrix(matrix)

        for op in operations.keys():
            if op in operation_str and op != 'T':
                left, right = operation_str.split(op)
                left, right = left.strip(), right.strip()

                A, B = matrices[left], matrices[right]

                return operations[op](A, B)

        raise ValueError("Niepoprawne wyrażenie operacji.")

    except KeyError:
        raise ValueError("Macierz nie istnieje.")
    except ValueError as e:
        raise ValueError(f"Błąd wykonania operacji: {str(e)}")


# Przykład użycia systemu
if __name__ == "__main__":
    # Przykładowe macierze
    matrices = {
        'A': np.array([[1, 2], [3, 4]]),
        'B': np.array([[5, 6], [7, 8]]),
        'C': np.array([[1, 2, 3], [4, 5, 6]])
    }

    # Przykładowe operacje
    try:
        result1 = execute_matrix_operation("A + B", matrices)
        print("Wynik A + B:\n", result1)

        result2 = execute_matrix_operation("A @ B", matrices)
        print("Wynik A @ B:\n", result2)

        result3 = execute_matrix_operation("C T", matrices)
        print("Wynik transpozycji C:\n", result3)

    except ValueError as e:
        print(e)
