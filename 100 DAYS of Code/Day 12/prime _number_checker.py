
def is_number_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

quit_app = False

while quit_app == False:
    num = input("Give me a number for prime number test (or Q for Quit): ")
    print('\n' * 20)
    
    if num != 'q':
        num = int(num)
        prime = True        

        prime = is_number_prime(num)          
        if prime:
            print(f"Number {num} IS a PRIME number.")
        else:
            print(f"Number {num} is NOT a prime number.")
    
    else:
        quit_app = True

print("Thank you for using program for PRIME NUMBERS.")
            