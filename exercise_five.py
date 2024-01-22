# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

#pseudocode
#given numbers
first_given_numbers = [10, 20, 30, 40, 10]

second__given_numbers = [75, 65, 35, 75, 30]

#creating functions
def check_first_and_last_number(list_of_numbers):
    first_number = list_of_numbers[0]
    last_number = list_of_numbers[-1]

    if first_number == last_number:
        return True
        
    else:
        return False


#printing result for true
print("The given numbers are: ", first_given_numbers)
print("The given list is: ", check_first_and_last_number(first_given_numbers))

# printing result for false
print("The given numbers are: ", second__given_numbers)
print("The given list is: ", check_first_and_last_number(second__given_numbers))


