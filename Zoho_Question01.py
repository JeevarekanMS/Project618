def print_pattern_fixed(n):
    # First half of the pattern
    current_num = 1
    row_values = []
    
    for i in range(1, n+1):
        row = []
        temp_num = current_num + i - 1
        for j in range(i):
            row.append(temp_num)
            temp_num -= 1
        row_values.append(row)
        current_num += i
    
    # Print the first half
    for i in range(n):
        print("  " * (n - i - 1), end="")
        print(" ".join(f"{num:2}" for num in row_values[i]))

    # Print the second half (reversed rows)
    for i in range(n-1, -1, -1):
        print("  " * (n - i - 1), end="")
        print(" ".join(f"{num:2}" for num in row_values[i]))

# Example usage
rows = int(input("Enter number of rows: "))
print_pattern_fixed(rows)
