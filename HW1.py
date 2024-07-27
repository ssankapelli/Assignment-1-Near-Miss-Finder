"""
Title: Fermat's Last Theorem Near Miss Finder
File: test.py
External Files Needed: None
External Files Created: 
    results.txt - Contains the best x, y, z values and the smallest relative miss.
Programmers:
         Parth Yashvantkumar Barot(Parthyashvantkumar@lewisu.edu)
         Sai Prasanna Sankapelli(SaiPrasannaSankape@lewisu.edu)
Course: CS101 Section 2
Date Submitted: 2024-07-26
Program Description: 
    This program finds the near misses for Fermat's Last Theorem for given values of n and k.
    It iterates through possible values of x and y, calculates z, and finds the smallest relative miss.
"""

import math

def find_near_misses(n, k):
    smallest_relative_miss = float('inf')
    best_x = best_y = best_z = 0

    for x in range(10, k + 1):
        for y in range(10, k + 1):
            lhs = x**n + y**n

            z = int(lhs**(1/n))
            z1 = z + 1

            z_n = z**n
            z1_n = z1**n

            diff1 = abs(lhs - z_n)
            diff2 = abs(lhs - z1_n)

            if diff1 < diff2:
                miss = diff1
                z_best = z
            else:
                miss = diff2
                z_best = z1

            relative_miss = miss / lhs

            if relative_miss < smallest_relative_miss:
                smallest_relative_miss = relative_miss
                best_x, best_y, best_z = x, y, z_best
                print(f"New best x: {best_x}, y: {best_y}, z: {best_z}")
                print(f"Actual miss: {miss}, Relative miss: {relative_miss}")

    return best_x, best_y, best_z, smallest_relative_miss

def main():
    print("Fermat's Last Theorem Near Miss Finder")
    try:
        n = int(input("Enter the value for n (2 < n < 12): "))
        if not (2 < n < 12):
            raise ValueError("n must be between 2 and 12.")
        
        k = int(input("Enter the value for k (k > 10): "))
        if k <= 10:
            raise ValueError("k must be greater than 10.")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
        return

    x, y, z, relative_miss = find_near_misses(n, k)
    print(f"Smallest relative miss: {relative_miss}")
    print(f"Best x: {x}, y: {y}, z: {z}")
    input("press enter to exit")
if __name__ == "__main__":
    main()
