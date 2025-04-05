# base-algos/base-algos/README.md

# Base Algos

Base Algos is a Python package that implements various algorithms, including the Sieve of Eratosthenes for finding prime numbers. This package is designed to be simple and efficient, making it easy to integrate into your projects.

## Installation

To install the Base Algos package, you can use pip. First, ensure you have Python and pip installed on your system. Then, run the following command:

```
pip install .
```

Alternatively, you can clone the repository and install the dependencies listed in `requirements.txt`:

```
git clone https://github.com/yourusername/base-algos.git
cd base-algos
pip install -r requirements.txt
```

## Usage

To use the Sieve of Eratosthenes implementation, you can import the `get_primes` function from the `base_algos.sieve` module:

```python
from base_algos.sieve import get_primes

sieve_size = 100
primes = get_primes(sieve_size)
print(primes)
```

This will output a list of all prime numbers less than the specified `sieve_size`.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.