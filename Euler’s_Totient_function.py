import random
from math import gcd
def is_prime(n):
    "Check if a number is prime."
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_prime_numbers(start, end):
    "Generate a list of prime numbers within a given range."
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

def pick_two_primes(prime_list):
    "Randomly pick two distinct prime numbers from a list."
    p = random.choice(prime_list)
    q = random.choice(prime_list)
    while q == p:
        q = random.choice(prime_list)
    return p, q

def euler_totient(n):
    "Calculate Euler's Totient function φ(n)."
    count = 0
    for i in range(1, n):
        if gcd(n, i) == 1:
            count += 1
    return count

def main():
    # Define the range to generate prime numbers
    start_range = 10
    end_range = 100

    # Generate prime numbers within the range
    prime_list = generate_prime_numbers(start_range, end_range)

    # Ensure we have enough prime numbers in the list
    if len(prime_list) < 2:
        print("Not enough prime numbers in the specified range.")
        return

    # Randomly pick two prime numbers
    p, q = pick_two_primes(prime_list)

    # Calculate Euler's Totient function values for p and q
    phi_p = euler_totient(p)
    phi_q = euler_totient(q)

    # Print the selected prime numbers and their Totient values
    print(f"Randomly selected prime numbers are: p = {p}, q = {q}")
    print(f"Euler's Totient function value φ({p}) = {phi_p}")
    print(f"Euler's Totient function value φ({q}) = {phi_q}")

if __name__ == "__main__":
    main()
