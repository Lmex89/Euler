#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sympy as smp


def get_consecutives_primes(a, b):
    i = 0
    while True:
        num = i**2 + a*i + b
        if smp.isprime(num):
            i += 1
        else:
            return i


def compute(max_a, max_b):
    best_primes = 0
    best_a = 0
    best_b = 0
    for a in range(-max_a, max_a+1):
        for b in range(-max_b, max_b+1):
            primes = get_consecutives_primes(a, b)
            if primes > best_primes:
                best_primes = primes
                best_a = a
                best_b = b
    return best_primes, best_a, best_b


best_primes, best_a, best_b = compute(1000, 1000)

print(best_a, best_b, best_a*best_b, best_primes)
