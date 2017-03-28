import math

def get_primes(sieveSize):
    ''' Returns a list of prime numbers calculated using
    the Sieve of Eratosthenes algorithm'''	

    sieve = [True] * sieveSize
    sieve[0] = False 
    sieve[1] = False

    # create the sieve
    for i in range(2, int(math.sqrt(sieveSize)) + 1):
        pointer = i * 2
        while pointer < sieveSize:
            sieve[pointer] = False
            pointer += i
            
    # extract the list of primes
    primes = [index for index,val in enumerate(sieve) if val == True]

    return primes
          
if __name__ == "__main__":
    sieveSize = int(input("Enter a number upto which you want all prime numbers (not-inclusive of the number): "))
    if sieveSize < 0 or sieveSize > 1e6:
        raise ValueError( "Only enter an integer between 0 and 1e6 (inclusive)" )
    print(get_primes(sieveSize))f