
def even_number():
    """ Check if number is even"""
    
    try:
        num = int(input('Enter a number: '))
        if num % 2 == 0:
            print(f'Your number {num} is even')
        else:
            print('Your number is odd')
    except ValueError as v:
        print(f' Please enter number! {v}')

    finally:
        print('Good day!')

even_number()