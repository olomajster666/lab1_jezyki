def analyze_mixed_data(data):
    numbers = list(filter(lambda x: isinstance(x, (int, float)), data))
    max_number = max(numbers) if numbers else None

    strings = list(filter(lambda x: isinstance(x, str), data))
    longest_string = max(strings, key=len) if strings else None

    tuples = list(filter(lambda x: isinstance(x, tuple), data))
    longest_tuple = max(tuples, key=len) if tuples else None

    return max_number, longest_string, longest_tuple

data = [123, "Hello", (1, 2, 3), [1, 2, 3, 4], {"key": "value"}, 3.14, "Python", (1, 2)]
result = analyze_mixed_data(data)
print("Największa liczba:", result[0])
print("Najdłuższy napis:", result[1])
print("Krotka o największej liczbie elementów:", result[2])
