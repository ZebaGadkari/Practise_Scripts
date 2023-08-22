#right triange pattern

def right_triangle_pattern(rows):
    for i in range(1,rows+1):
        for j in range(i):
            print("*", end="")
        print()

# Example usage:
right_triangle_pattern(5)

#hollow square pattern

def hollow_square_pattern(rows):
    for i in range(rows):
        for j in range(rows):
            if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Example usage:
hollow_square_pattern(4)

#pyramid_pattern
def pyramid_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print()

# Example usage:
pyramid_pattern(5)
