import sys
from base_algos.sieve import get_primes

def main():
    if len(sys.argv) != 2:
        print("Usage: python run_example.py <sieve_size>")
        sys.exit(1)

    try:
        sieve_size = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid integer for sieve size.")
        sys.exit(1)

    primes = get_primes(sieve_size)
    print(f"Prime numbers up to {sieve_size}: {primes}")

if __name__ == "__main__":
    main()