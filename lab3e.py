#!/usr/bin/env python3


my_list = [100, 200, 300, 'six hundred']

# Create the list called "my_list" here, not within any function defined below.
# That makes it a global object. We'll talk about that in another lab.


def give_list():
    return my_list[0:] 
    
    # Does not accept any arguments
    # Returns all of items in the global object my_list unchanged

def give_first_item():
    return str(my_list[0])
    
    # Does not accept any arguments
    # Returns the first item in the global object my_list as a string

def give_first_and_last_item():
        return [my_list[0], my_list[-1]]
    
    # Does not accept any arguments
    # Returns a list that includes the first and last items in the global object my_list

def give_second_and_third_item():
    return my_list[1:3]
    
    # Does not accept any arguments
    # Returns a list that includes the second and third items in the global object my_list

if __name__ == '__main__':   # This section also referred to as a "main block"
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())