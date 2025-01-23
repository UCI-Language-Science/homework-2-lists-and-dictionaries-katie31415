# Write code that calculates the sum of the square of every even 
# number in the list below and prints it (that is, you take each 
# even number, square it, and then add them all together).
# 
# You can use a list comprehension or a regular loop. You can also
# use the sum function to sum the values in a list if it's helpful.
# sum(<list>)
# 
# For the list below, your code should print 44984
#
def even_square_sum():
    numbers = [1, 62, 3, 57, 26, 8, 101, 200, 43, 20, 11]
    even_numbers = []
    squared_even_numbers = []
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even_numbers = even_numbers + [numbers[i]]
    
    for i in range(len(even_numbers)):
        squared_even_numbers = squared_even_numbers + [even_numbers[i]**2]
    
    print (sum(squared_even_numbers))

if __name__ == "__main__":
    even_square_sum()