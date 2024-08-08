#!/usr/bin/python3

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    if x == 0 or not nums:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [i for i in range(1, n+1) if is_prime(i)]
        while primes:
            if len(primes) == 1:
                ben_wins += 1
                break
            maria_picks = primes[0]
            primes = [p for p in primes if p % maria_picks != 0]
            if not primes:
                maria_wins += 1
                break
            ben_picks = primes[0]
            primes = [p for p in primes if p % ben_picks != 0]
            if not primes:
                ben_wins += 1
                break

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
