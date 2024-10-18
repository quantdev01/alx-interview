#!/usr/bin/python3
"""
Module, this will be checking a game
"""


def isWinner(x, nums):
    def sieve_of_eratosthenes(max_n):
        is_prime = [True] * (max_n + 1)
        p = 2
        while (p * p <= max_n):
            if (is_prime[p]):
                for i in range(p * p, max_n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, max_n + 1) if is_prime[p]]

    max_n = max(nums)  # Find the maximum value of n from nums
    primes = sieve_of_eratosthenes(max_n)  # Get all primes up to max_n

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_set = set(primes)  # Create a set of primes for the current n
        current_player = 0  # 0 for Maria, 1 for Ben

        while prime_set:
            # Choose the smallest prime
            chosen_prime = min(prime_set)
            # Remove the chosen prime and its multiples from the set
            for multiple in range(chosen_prime, n + 1, chosen_prime):
                prime_set.discard(multiple)
            # Switch players
            current_player = 1 - current_player

        if current_player == 0:  # If current_player is 0, then Ben won
            ben_wins += 1
        else:  # If current_player is 1, then Maria won
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
