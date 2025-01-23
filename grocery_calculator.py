# Write a program that asks the user to input their grocery list
# and then tells them the price. You can make the following two
# assumptions:
# - the only available groceries are:
#       - bread: $3
#       - eggs: $6
#       - milk: $4
#       - butter: $2
# - users must enter one item at a time, even if they are buying
#   multiple
#       - e.g. if the user is buying three loaves of bread, they
#         will have to input 'bread' 3 times.
#
# If the user inputs something that is not one of the four options
# above, the program should print "The store doesn't have that" and
# then prompt the user for more input.
#
# When the user inputs an empty line (i.e. hits enter without typing
# anything), the program should print the total cost of their groceries.
#
# For example:
# Input grocery item:
# >> bread
# Input next grocery item:
# >> milk
# Input next grocery item
# >>
# Your total grocery bill is $7

def grocery_calculator():
    grocery_items = ['bread', 'eggs', 'milk', 'butter', '']
    cost_of_items = [3, 6, 4, 2, 0]
    total_cost = 0
    print ('Input grocery item: ')
    name = input()
    if name not in grocery_items:
        print ("The store doesn't have that")
    total_cost = total_cost + cost_of_items [grocery_items.index(name)]
    while True:
        print ('Input next grocery item: ')
        name = input()
        if name == '':
            break
        elif name not in grocery_items:
            print ("The store doesn't have that")
        else:
            total_cost = total_cost + cost_of_items [grocery_items.index(name)]
    
    print ('Your total grocery bill is $' + str(total_cost))

if __name__ == "__main__":
    grocery_calculator()