def num(elements, M, N):
    sort = sorted(elements)
    first_max = sort[-M]
    third_min = sort[N - 1]
    sum_nums = first_max + third_min
    diff_nums = first_max - third_min
    return first_max, third_min, sum_nums, diff_nums
elements = list(map(int, input("Enter the elements separated by spaces: ").split()))
M = int(input("Enter the value of M: "))
N = int(input("Enter the value of N: "))
first_max, third_min, sum_nums, diff_nums = num(elements, M, N)
print(f"{M}st Maximum Number = {first_max}")
print(f"{N}rd Minimum Number = {third_min}")
print(f"Sum = {sum_nums}")
print(f"Difference = {diff_nums}")
