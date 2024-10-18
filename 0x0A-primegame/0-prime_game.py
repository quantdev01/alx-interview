#!/usr/bin/python3
"""
Module, this will be checking a game
"""


def sieve_of_eratosthenes(limit):
    """
    Implements the Sieve of Eratosthenes to find all prime numbers up to n.

    Args:
    n (int): The upper limit of the range to check for primes.

    Returns:
    list: A list of boolean values where True indicates a prime number.
    """
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if is_prime[p]:
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game for multiple rounds.

    Args:
    x (int): The number of rounds.
    nums (list): An array of n values for each round.

    Returns:
        str: The name of the player that won the most rounds,
        or None if it's a tie.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    prime_count = [0] * (max_n + 1)

    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1]
        if i in primes:
            prime_count[i] += 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
