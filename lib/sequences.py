#!/usr/bin/env python3

def print_fibonacci(n):  
    if n <= 0:  
        print([])  # If n is 0 or negative, print an empty list  
        return  
    
    fibonacci_sequence = [0, 1]  # Start the sequence with the first two Fibonacci numbers  
    
    while len(fibonacci_sequence) < n:  
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Sum of the last two numbers  
        fibonacci_sequence.append(next_number)  # Append the next Fibonacci number to the list  
    
    # Print only the first n numbers of the Fibonacci sequence  
    print(fibonacci_sequence[:n])