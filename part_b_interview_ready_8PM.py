# ============================================================
# PART B: Interview Ready
# Day 8 PM Assignment | codewithnavaid
# ============================================================


# ─────────────────────────────────────────────────────────────
# Q1: break vs continue, and loop-else
# ─────────────────────────────────────────────────────────────
"""
BREAK vs CONTINUE
─────────────────

break:
  Exits the ENTIRE loop immediately. Code after the loop runs next.
  Use when you've found what you're looking for and further iteration
  is unnecessary.

continue:
  Skips the REST of the current iteration and jumps to the NEXT one.
  The loop itself keeps running.
  Use when you want to skip certain items but keep looping.

Example:
"""

print("=" * 55)
print("Q1: break vs continue")
print("─" * 55)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# continue — skip even numbers
print("continue (skip evens): ", end="")
for n in numbers:
    if n % 2 == 0:
        continue        # skip this iteration, go to next n
    print(n, end=" ")
print()

# break — stop at first even number
print("break   (stop at 4) : ", end="")
for n in numbers:
    if n == 4:
        break           # exit loop entirely
    print(n, end=" ")
print()

"""
LOOP-ELSE CLAUSE
────────────────
The `else` block of a for/while loop runs ONLY if the loop
completed normally — i.e., was NOT terminated by a `break`.

If a `break` fires, the `else` is SKIPPED.

Practical use case: Search pattern.
  → "Search through a list; if found, break. If not found,
     the else handles the 'not found' case cleanly."

This avoids needing a found_flag variable.
"""

print("\nloop-else — search pattern:")

def search_demo(items, target):
    for item in items:
        if item == target:
            print(f"  Found '{target}' in list — else skipped.")
            break
    else:
        # Runs only if loop finished without break (item never found)
        print(f"  '{target}' not found — else executed.")

search_demo([10, 20, 30, 40], 20)   # Found  → else skipped
search_demo([10, 20, 30, 40], 99)   # Not found → else runs


# ─────────────────────────────────────────────────────────────
# Q2: find_pairs — O(n²) then O(n)
# ─────────────────────────────────────────────────────────────
"""
O(n²) APPROACH — Nested loops
  For every element i, check every element j after it.
  Total comparisons ≈ n*(n-1)/2 → O(n²).

O(n) APPROACH — Set (hash lookup)
  For each number x, check if (target - x) is already in a set.
  Hash set lookup is O(1), so the whole pass is O(n).
  Use a seen set: add x after checking, so we never pair x with itself
  and never produce duplicate pairs.
"""

def find_pairs_n2(numbers, target):
    """O(n²) — nested loops."""
    pairs = []
    for i in range(len(numbers)):                   # outer loop
        for j in range(i + 1, len(numbers)):        # inner loop
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))
    return pairs


def find_pairs_n1(numbers, target):
    """O(n) — set-based single pass."""
    seen   = set()
    pairs  = []
    for x in numbers:
        complement = target - x
        if complement in seen:          # O(1) hash lookup
            pair = (min(x, complement), max(x, complement))
            if pair not in pairs:       # avoid duplicate pairs
                pairs.append(pair)
        seen.add(x)
    return pairs


print("\n" + "=" * 55)
print("Q2: find_pairs")
print("─" * 55)

nums   = [1, 2, 3, 4, 5]
target = 6

print(f"  Input : {nums}, target = {target}")
print(f"  O(n²) : {find_pairs_n2(nums, target)}")
print(f"  O(n)  : {find_pairs_n1(nums, target)}")

# Extra test with duplicates
nums2   = [1, 5, 3, 3, 2, 4, 5]
target2 = 6
print(f"\n  Input : {nums2}, target = {target2}")
print(f"  O(n²) : {find_pairs_n2(nums2, target2)}")
print(f"  O(n)  : {find_pairs_n1(nums2, target2)}")


# ─────────────────────────────────────────────────────────────
# Q3: Debug & Fix is_prime
# ─────────────────────────────────────────────────────────────
"""
BUGGY CODE:
    for i in range(2, n):   # iterates all the way up to n-1

BUGS IDENTIFIED:
  1. PERFORMANCE BUG (O(n) → fixable to O(√n)):
     The loop runs from 2 to n-1. A factor pair (a, b) where a×b = n
     always has one factor ≤ √n. So we only need to check up to √n.
     Checking beyond √n is redundant — all those factors were already
     covered by their smaller partners earlier.
     Fix: range(2, int(n**0.5) + 1)

  2. EDGE CASE — n = 2:
     range(2, 2) is empty → loop doesn't run → returns True. ✅ Correct.

  3. EDGE CASE — n = 1, n = 0, negative:
     The `if n < 2: return False` guard handles these correctly. ✅

  Fix summary:
     Change range(2, n) → range(2, int(n**0.5) + 1)
     This reduces time complexity from O(n) to O(√n).
"""

def is_prime_buggy(n):
    """Original buggy version — O(n)."""
    if n < 2:
        return False
    for i in range(2, n):          # ← BUG: should stop at √n
        if n % i == 0:
            return False
    return True


def is_prime(n):
    """Fixed version — O(√n)."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:                 # quick even check (optional optimisation)
        return False
    for i in range(3, int(n**0.5) + 1, 2):   # only odd divisors up to √n
        if n % i == 0:
            return False
    return True


print("\n" + "=" * 55)
print("Q3: is_prime — Bug Fix")
print("─" * 55)

test_values = [0, 1, 2, 3, 4, 13, 17, 25, 97, 100]
print(f"  {'n':>5}  {'buggy':>8}  {'fixed':>8}")
print(f"  {'─'*5}  {'─'*8}  {'─'*8}")
for n in test_values:
    print(f"  {n:>5}  {str(is_prime_buggy(n)):>8}  {str(is_prime(n)):>8}")

print()
