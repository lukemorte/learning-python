
quit_app = False

while quit_app == False:
    num = input("Give me a number for prime number test (or Q for Quit): ")
    print('\n' * 20)
    
    if num != 'q':
        num = int(num)
        prime = True

        for i in range(2, num):
            if num % i == 0:
                prime = False
                
        if prime:
            print(f"Number {num} IS a PRIME number.")
        else:
            print(f"Number {num} is NOT a prime number.")
    
    else:
        quit_app = True

print("Thank you for using program for PRIME NUMBERS.")
            