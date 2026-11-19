"""
Algorithms in Five Case Studies (Rosen, Discrete Mathematics 8e, Chapter 3)
Author: Yash

Instrumented implementations of slow vs. fast algorithms across five core
problem domains from Rosen Chapter 3. Each function returns both the
computed solution and the exact elementary operation count.
"""

import math


# ==============================================================================
# 1. ORDERED LIST SEARCHING (Rosen Section 3.1.2 & Section 3.3.2)
# ==============================================================================
def linear_search(x, arr):
    """Sequential search. Returns (1-based index or 0, total comparisons)."""
    n = len(arr)
    i, comps = 1, 0
    while True:
        comps += 1  # while condition: i <= n
        if i > n:
            break
        comps += 1  # while condition: x != a_i
        if x == arr[i - 1]:
            break
        i += 1
    comps += 1  # post-loop check: if i <= n
    return (i if i <= n else 0), comps


def binary_search(x, arr):
    """Divide-and-conquer binary search on sorted list. Returns (1-based index or 0, comparisons)."""
    n = len(arr)
    i, j, comps = 1, n, 0
    while True:
        comps += 1  # while condition: i < j
        if not (i < j):
            break
        m = (i + j) // 2
        comps += 1  # if x > a_m
        if x > arr[m - 1]:
            i = m + 1
        else:
            j = m
    comps += 1  # post-loop check: if x == a_i
    return (i if x == arr[i - 1] else 0), comps


# ==============================================================================
# 2. COMPARISON SORTING (Rosen Section 3.1.3 & Section 3.3.2)
# ==============================================================================
def bubble_sort(arr):
    """Adjacent-exchange bubble sort. Returns (sorted list, element comparisons)."""
    a = list(arr)
    n, comps = len(a), 0
    for i in range(1, n):
        for j in range(0, n - i):
            comps += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a, comps


def insertion_sort(arr):
    """Incremental prefix insertion sort. Returns (sorted list, element comparisons)."""
    a = list(arr)
    n, comps = len(a), 0
    for j in range(1, n):
        key = a[j]
        i = 0
        while i < j:
            comps += 1
            if key > a[i]:
                i += 1
            else:
                break
        a.insert(i, a.pop(j))
    return a, comps


def merge_sort(arr):
    """Divide-and-conquer merge sort. Returns (sorted list, element comparisons)."""
    if len(arr) <= 1:
        return list(arr), 0
    mid = len(arr) // 2
    left, c1 = merge_sort(arr[:mid])
    right, c2 = merge_sort(arr[mid:])
    merged, comps, i, j = [], c1 + c2, 0, 0
    while i < len(left) and j < len(right):
        comps += 1
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, comps


# ==============================================================================
# 3. EXACT STRING PATTERN MATCHING (Rosen Section 3.1.4)
# ==============================================================================
def naive_string_match(T, P):
    """Brute-force sliding window matcher. Returns (valid shifts, char comparisons)."""
    n, m = len(T), len(P)
    shifts, comps = [], 0
    for s in range(n - m + 1):
        j = 0
        while j < m:
            comps += 1
            if T[s + j] == P[j]:
                j += 1
            else:
                break
        if j == m:
            shifts.append(s)
    return shifts, comps


def kmp_string_match(T, P):
    """Knuth-Morris-Pratt prefix-jump matcher. Returns (valid shifts, char comparisons)."""
    n, m = len(T), len(P)
    lps, length, i, comps = [0] * m, 0, 1, 0
    while i < m:
        comps += 1
        if P[i] == P[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    shifts, i, j = [], 0, 0
    while i < n:
        comps += 1
        if P[j] == T[i]:
            i += 1
            j += 1
        if j == m:
            shifts.append(i - j)
            j = lps[j - 1]
        elif i < n and P[j] != T[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return shifts, comps


# ==============================================================================
# 4. POLYNOMIAL EVALUATION (Rosen Section 3.3, Exercises 13-14)
# ==============================================================================
def poly_conventional(c, coeffs):
    """Evaluates sum(coeffs[i] * c^i). Returns (value, arithmetic ops)."""
    power, y, ops = 1.0, float(coeffs[0]), 0
    for i in range(1, len(coeffs)):
        power *= c
        ops += 1
        y += coeffs[i] * power
        ops += 2
    return y, ops


def poly_horner(c, coeffs):
    """Horner's nested evaluation. Returns (value, arithmetic ops)."""
    y, ops = float(coeffs[-1]), 0
    for i in range(len(coeffs) - 2, -1, -1):
        y = y * c + coeffs[i]
        ops += 2
    return y, ops


# ==============================================================================
# 5. TALK SCHEDULING OPTIMIZATION (Rosen Section 3.1.5, Algorithm 8)
# ==============================================================================
def schedule_bruteforce(talks):
    """Exhaustive 2^n subset search for compatible talks. Returns (schedule, ops)."""
    n = len(talks)
    best, ops = [], 0
    for mask in range(1 << n):
        subset = [talks[i] for i in range(n) if (mask >> i) & 1]
        subset.sort(key=lambda t: t[0])
        ok = True
        for k in range(len(subset) - 1):
            ops += 1
            if subset[k][1] > subset[k + 1][0]:
                ok = False
                break
        if ok and len(subset) > len(best):
            best = subset
    return best, max(ops, 1)


def schedule_greedy(talks):
    """Earliest-finish-time greedy algorithm. Returns (schedule, ops)."""
    sorted_talks = sorted(talks, key=lambda t: t[1])
    ops = max(1, int(len(talks) * math.log2(max(2, len(talks)))))
    selected, last_end = [], -float("inf")
    for s, e in sorted_talks:
        ops += 1
        if s >= last_end:
            selected.append((s, e))
            last_end = e
    return selected, ops


# ==============================================================================
# BENCHMARK DRIVER
# ==============================================================================
def run_all_experiments():
    print("=" * 72)
    print("1. ORDERED SEARCHING: Linear Search vs. Binary Search (Worst Case)")
    print("=" * 72)
    print(f"{'n':>8} {'Linear (Worst)':>16} {'Linear (Avg)':>14} {'Binary (Worst)':>16}")
    for n in (10, 100, 1_000, 10_000, 100_000):
        arr = list(range(1, n + 1))
        _, lin_w = linear_search(-1, arr)
        avg = sum(linear_search(v, arr)[1] for v in arr) / n if n <= 1000 else n + 2
        _, bin_w = binary_search(-1, arr)
        print(f"{n:>8,} {lin_w:>16,} {avg:>14.1f} {bin_w:>16,}")

    print("\n" + "=" * 72)
    print("2. COMPARISON SORTING: Bubble vs. Insertion vs. Merge Sort (Reverse Input)")
    print("=" * 72)
    print(f"{'n':>8} {'Bubble':>14} {'Insertion':>14} {'Merge Sort':>14}")
    for n in (20, 50, 100, 250, 500, 1_000):
        arr = list(range(n, 0, -1))
        s1, c_bub = bubble_sort(arr)
        s2, c_ins = insertion_sort(arr)
        s3, c_mrg = merge_sort(arr)
        assert s1 == s2 == s3 == list(range(1, n + 1))
        print(f"{n:>8,} {c_bub:>14,} {c_ins:>14,} {c_mrg:>14,}")

    print("\n" + "=" * 72)
    print("3. EXACT STRING MATCHING: Naive vs. KMP (Adversarial T='a'^(n-1)+'b')")
    print("=" * 72)
    print(f"{'n':>8} {'m':>6} {'Naive Comps':>15} {'KMP Comps':>13}")
    m = 50
    P = "a" * (m - 1) + "b"
    for n in (100, 250, 500, 1_000, 2_500, 5_000):
        T = "a" * (n - 1) + "b"
        sh1, c_naive = naive_string_match(T, P)
        sh2, c_kmp = kmp_string_match(T, P)
        assert sh1 == sh2 == [n - m]
        print(f"{n:>8,} {m:>6} {c_naive:>15,} {c_kmp:>13,}")

    print("\n" + "=" * 72)
    print("4. POLYNOMIAL EVALUATION: Conventional vs. Horner's Rule")
    print("=" * 72)
    for deg in (10, 100, 1_000):
        coeffs = [i + 1 for i in range(deg + 1)]
        v1, op1 = poly_conventional(1.05, coeffs)
        v2, op2 = poly_horner(1.05, coeffs)
        assert math.isclose(v1, v2, rel_tol=1e-9)
        print(f"Degree {deg:>4}: Conventional = {op1:>5,} ops | Horner = {op2:>5,} ops")

    print("\n" + "=" * 72)
    print("5. TALK SCHEDULING: Brute-Force Subsets vs. Greedy Earliest-Finish-Time")
    print("=" * 72)
    print(f"{'n talks':>8} {'Brute-Force Ops':>18} {'Greedy EFT Ops':>16}")
    for n in (6, 10, 14, 18, 22):
        talks = [(i, i + 2) for i in range(n)]
        b_sch, c_bf = schedule_bruteforce(talks)
        g_sch, c_gr = schedule_greedy(talks)
        assert len(b_sch) == len(g_sch)
        print(f"{n:>8} {c_bf:>18,} {c_gr:>16,}")

    print("\n" + "=" * 72)
    print("6. BIG-THETA WITNESS VERIFICATION: f(n) = 4n^2 + 6n log2(n) + 10")
    print("=" * 72)
    f = lambda n: 4 * n**2 + 6 * n * math.log2(n) + 10
    holds = all(4 * n**2 <= f(n) <= 20 * n**2 for n in range(1, 100_001))
    print(f"4*n^2 <= f(n) <= 20*n^2 for all 1 <= n <= 100,000: {holds}")
    print(f"f(10^6) / 10^12 = {f(10**6) / 10**12:.4f}")


if __name__ == "__main__":
    run_all_experiments()