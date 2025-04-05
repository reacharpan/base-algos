from setuptools import setup, find_packages

setup(
    name='base-algos',
    version='0.1.0',
    author='Arpan Shah',
    author_email='your_email@example.com',
    description='A collection of basic algorithms, including the Sieve of Eratosthenes for finding prime numbers.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/base-algos',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)