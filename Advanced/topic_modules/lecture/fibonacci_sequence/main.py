def create_fibonacci_sequence(n):
    sequence = [0, 1]
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        for _ in range(n-2):
            sequence.append(sequence[-1] + sequence[-2])
        return sequence

def find_n(number, seq):
    try:
        number_index = seq.index(number)
        return f"The number - {number} is at index {number_index}"
    except ValueError:
        return f"The number {number} is not in the sequence"




