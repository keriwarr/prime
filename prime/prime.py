import math
import random

"""
This document will provide a number of tools and functions for working with
prime numbers, including a number of deterministic and probabilistic primality
tests, and a function for generating large prime numbers
"""

def naive_probabilistic (num):
    """
    This is a probabilistic, fast, poor primality test for quickly weeding out
    candidates with low primes as factors
    :param num: int (>= 2)
    :return: boolean
    """
    low_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                       53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
                       109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
                       173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                       233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
                       293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                       367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
                       433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
                       499]
    if num in low_primes_list: return True
    if num < 500: return False
    for prime in low_primes_list:
        if num % prime == 0:
            return False
    return True


def naive_deterministic (num):
    """
    This is a deterministic, slow, primality test, included just 'cuz
    :param num: int (>= 2)
    :return: boolean
    """
    if num == 2: return True
    for val in range(2, math.ceil(math.sqrt(num)) + 1):
        if num % val == 0: return False
    return True


def fermat_test (num):
    """
    an implementation of the fermat primality test
    :param num:
    :return:
    """
    a = random.randint(0, num)
    if pow(a, num - 1, num) != 1: return False
    return True


def miller_rabin_test (num, iter):
    """

    :param num:
    :return:
    """
    assert num >= 2
    if num == 2 or num == 3:
        return True


    s = 0
    d = num - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    assert(2**s * d == num - 1)

    for _ in range(iter):
        a = random.randint(2, num - 1)
        x = pow(a, d, num)
        if x == 1 or x == num - 1: continue
        for r in range(1, s):
            x = pow(x, 2, num)
            if x == 1: return False
            elif x == num - 1: continue
        return False
    return True


def large_prime (bits):
    """
    If implemented correctly, this function should return a value in the range
    [2, 2^(bits)] which is prime with a certainty of 1-2^(-100)
    It makes use of a number of probabilistic primality tests of increasing
    power
    :param bits: int
    :return: int U boolean
    """
    while True:
        num = random.getrandbits(bits)
        if naive_probabilistic(num):
            fermat = fermat_test(num)
            if fermat:
                miller_rabin = miller_rabin_test(num, 7)
                if miller_rabin: return num
                #else: print ("miller: ", num)
            #else: print ("fermat: ", num)
    return False



# some testing stuff:

#for iters in range(10):
#    naive_passed = 0
#    fermat_failed = 0
#    while naive_passed < 100:
#        num = random.getrandbits(256)
#        if naive_probabilistic(num):
#            naive_passed += 1
#            if not miller_rabin_test(num, iters):
#                fermat_failed += 1
#    print (iters, fermat_failed)

#for _ in range (10):
#    print (large_prime(512))

#for val in range (2, 270000):
#    if naive_probabilistic(val) != naive_deterministic(val): print ("error at", val, "; probabilistic reports: ", naive_probabilistic(val))

