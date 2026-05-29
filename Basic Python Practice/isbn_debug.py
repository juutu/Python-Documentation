def validate_isbn(isbn, length):
    # Fix TypeError: len() only takes the string argument
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return
        
    # Fix off-by-one and IndexError: 
    # The main digits are everything EXCEPT the last character
    main_digits = isbn[0:length - 1]
    given_check_digit = isbn[-1]
    
    # Fix ValueError for non-numeric characters inside the main digits
    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print('Invalid character was found.')
        return

    # Calculate the check digit from other digits
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)
        
    # Check if the given check digit matches with the calculated check digit
    if given_check_digit == expected_check_digit:
        print('Valid ISBN Code.')
    else:
        print('Invalid ISBN Code.')

def calculate_check_digit_10(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)
    result = 11 - digits_sum % 11
    if result == 11:
        expected_check_digit = '0'
    elif result == 10:
        expected_check_digit = 'X'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def calculate_check_digit_13(main_digits_list):
    digits_sum = 0
    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit * 1
        else:
            digits_sum += digit * 3
    result = 10 - digits_sum % 10
    if result == 10:
        expected_check_digit = '0'
    else:
        expected_check_digit = str(result)
    return expected_check_digit

def main():
    user_input = input('Enter ISBN and length: ')
    values = user_input.split(',')
    
    # Handle missing comma scenario safely
    try:
        isbn = values[0]
        length_str = values[1]
    except IndexError:
        print('Enter comma-separated values.')
        return

    # Handle non-numeric length scenario safely
    try:
        length = int(length_str)
    except ValueError:
        print('Length must be a number.')
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print('Length should be 10 or 13.')

# Important: Comment out the main() call for the test runner
# main()