#!/usr/bin/python3
"""
Module, this will be checking a game
"""


def sieve_of_eratosthenes(n):
    """Generates a list of prime numbers up to n using the Sieve of Eratosthenes."""
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return [i for i in range(2, n + 1) if primes[i]]

def isWinner(x, nums):
    """Determines the winner of the most rounds in the Prime Game."""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_in_game = [p for p in primes if p <= n]
        moves = 0
        while primes_in_game:
            prime = primes_in_game.pop(0)
            moves += 1
            primes_in_game = [p for p in primes_in_game if p % prime != 0]

        if moves % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
