'''
    Write a program that takes in a positive integer as input, and outputs a string of
    1's and 0's representing the integer in binary. For an integer x, the algorithm is:
        As long as x is greater than 0
           Output x % 2 (remainder is either 0 or 1)
           x = x // 2
    Note: The above algorithm outputs the 0's and 1's in reverse order. You will need
          to write a second function to reverse the string.

    Ex: If the input is:
        6
    the output is:
    110

    The program must define and call the following two functions.
        Define a function named int_to_reverse_binary() that takes an integer as a
            parameter and returns a string of 1's and 0's representing the integer in
            binary (in reverse).
        Define a function named string_reverse() that takes an input string as a
            parameter and returns a string representing the input string in reverse.

        def int_to_reverse_binary(integer_value)
        def string_reverse(input_string)
'''

# Define your functions here.
def int_to_reverse_binary(integer_value):
    binary = ''
    while integer_value > 0:
        binary += str(integer_value % 2)
        integer_value = integer_value // 2
    return binary

def string_reverse(input_string):
    return input_string[::-1]


if __name__ == '__main__':
    number = int(input('Enter a number: '))
    temp_binary = int_to_reverse_binary(number)
    print(string_reverse(temp_binary))

