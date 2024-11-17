#!/usr/bin/python3

def fibonacci_sequence(n):
    """
    Generate the Fibonacci sequence up to the nth number.

    Parameters:
    n (int): The number of terms in the Fibonacci sequence to generate.

    Returns:
    list: A list containing the Fibonacci sequence.
    """
    if n <= 0:
        return []

    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence

def display_sequence(seq):
    """
    Print the Fibonacci sequence.

    Parameters:
    seq (list): A list of integers representing the Fibonacci sequence.
    """
    print("Fibonacci Sequence:")
    for num in seq:
        print(num, end=' ')
    print()

def main():
    """
    Main function to execute the Fibonacci sequence generator.
    """
    try:
        terms = int(input("Enter the number of Fibonacci sequence: "))
        if terms <= 0:
            print("Please enter a positive integer.")
        else:
            sequence = fibonacci_sequence(terms)
            display_sequence(sequence)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
