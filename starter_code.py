"""
Recursion Assignment Starter Code
Complete the recursive functions below to analyze the compromised file system.
"""

import os

# ============================================================================
# PART 1: RECURSION WARM-UPS
# ============================================================================

def sum_list(numbers):
    """
    Recursively calculate the sum of a list of numbers.
    """
    if len(numbers) == 0:
        return 0
    return numbers[0] + sum_list(numbers[1:])


def count_even(numbers):
    """
    Recursively count how many even numbers are in a list.
    """
    if len(numbers) == 0:
        return 0

    if numbers[0] % 2 == 0:
        return 1 + count_even(numbers[1:])
    else:
        return count_even(numbers[1:])


def find_strings_with(strings, target):
    """
    Recursively find all strings that contain a target substring.
    """
    if len(strings) == 0:
        return []

    rest = find_strings_with(strings[1:], target)

    if target in strings[0]:
        return [strings[0]] + rest
    else:
        return rest


# ============================================================================
# PART 2: COUNT ALL FILES
# ============================================================================

def count_files(directory_path):
    """
    Recursively count all files in a directory and its subdirectories.
    """
    # Base case: if path is a file, count it
    if os.path.isfile(directory_path):
        return 1

    total_files = 0

    # Recursive case: directory
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        total_files += count_files(full_path)

    return total_files


# ============================================================================
# PART 3: FIND INFECTED FILES
# ============================================================================

def find_infected_files(directory_path, extension=".encrypted"):
    """
    Recursively find all files with a specific extension in a directory tree.
    """
    infected_files = []

    # Base case: if path is a file, check extension
    if os.path.isfile(directory_path):
        if directory_path.endswith(extension):
            return [directory_path]
        return []

    # Recursive case: directory
    for item in os.listdir(directory_path):
        full_path = os.path.join(directory_path, item)
        infected_files.extend(find_infected_files(full_path, extension))

    return infected_files


# ============================================================================
# TESTING & BENCHMARKING
# ============================================================================

if __name__ == "__main__":
    print("RECURSION ASSIGNMENT - STARTER CODE")
    print("Complete the functions above, then run this file to test your work.\n")

    # ---- COUNT FILE TESTS ----
    print("=" * 60)
    print("PART 1: RECURSION WARM-UPS")
    print("=" * 60)
    print("\nTest sum_list:")
    print(f"  sum_list([1, 2, 3, 4]) = {sum_list([1, 2, 3, 4])} (expected: 10)")
    print(f"  sum_list([]) = {sum_list([])} (expected: 0)")
    print(f"  sum_list([5, 5, 5]) = {sum_list([5, 5, 5])} (expected: 15)")
    
    print("\nTest count_even:")
    print(f"  count_even([1, 2, 3, 4, 5, 6]) = {count_even([1, 2, 3, 4, 5, 6])} (expected: 3)")
    print(f"  count_even([1, 3, 5]) = {count_even([1, 3, 5])} (expected: 0)")
    print(f"  count_even([2, 4, 6]) = {count_even([2, 4, 6])} (expected: 3)")
    
    print("\nTest find_strings_with:")
    result = find_strings_with(["hello", "world", "help", "test"], "hel")
    print(f"  find_strings_with(['hello', 'world', 'help', 'test'], 'hel') = {result}")
    print(f"  (expected: ['hello', 'help'])")
    result = find_strings_with(["cat", "dog", "bird"], "z")
    print(f"  find_strings_with(['cat', 'dog', 'bird'], 'z') = {result}")
    print(f"  (expected: [])")
    
    print("\n" + "=" * 60)
    print("PART 2: COUNT ALL FILES")
    print("=" * 60)
    print("Total files (Test Case 1):", count_files("test_cases/case1_flat"))     # 5
    print("Total files (Test Case 2):", count_files("test_cases/case2_nested"))   # 4
    print("Total files (Test Case 3):", count_files("test_cases/case3_infected")) # 5

    # ---- BREACH FILE COUNT ----
    print("Total files (breached files):", count_files("breach_data"))

    # ---- INFECTED FILE TESTS ----
    print("\n" + "=" * 60)
    print("PART 3: FIND INFECTED FILES")
    print("=" * 60)
    print("Total Infected Files (Test Case 1):", len(find_infected_files("test_cases/case1_flat")))     # 0
    print("Total Infected Files (Test Case 2):", len(find_infected_files("test_cases/case2_nested")))   # 0
    print("Total Infected Files (Test Case 3):", len(find_infected_files("test_cases/case3_infected"))) # 3

    # ---- BREACH INFECTED FILES ----
    print("Total Infected Files (breached files):", len(find_infected_files("breach_data")))

    # ---- BY DEPARTMENT ----
    print("\n" + "=" * 60)
    print("INFECTED FILES BY DEPARTMENT")
    print("=" * 60)
    if os.path.exists("breach_data/HR"):
        print("HR infected:", len(find_infected_files("breach_data/HR")))
    if os.path.exists("breach_data/Creative"):
        print("Creative infected:", len(find_infected_files("breach_data/Creative")))
    if os.path.exists("breach_data/Finance"):
        print("Finance infected:", len(find_infected_files("breach_data/Finance")))
    if os.path.exists("breach_data/Sales"):
        print("Sales infected:", len(find_infected_files("breach_data/Sales")))