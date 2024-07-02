import random
def is_prime(n):
    """Check if a number is prime."""
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
    """Generate a list of prime numbers within a given range."""
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

def pick_two_primes(prime_list):
    """Randomly pick two distinct prime numbers from a list."""
    p = random.choice(prime_list)
    q = random.choice(prime_list)
    while q == p:
        q = random.choice(prime_list)
    return p, q

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

    # Print the selected prime numbers
    print(f"Randomly selected prime numbers are: p = {p}, q = {q}")

if __name__ == "__main__":
    main()
