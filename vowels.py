def count_sorted_strings(n):
    # Calculate the total count of valid strings
    total_count = (n * (n + 1)) // 2
    
    return total_count

# Sample input
n = 2
result = count_sorted_strings(n)
print("Number of lexicographically sorted strings of length", n, ":", result)
