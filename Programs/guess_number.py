low = 0
high = 1000
print("Please think of a number between", str(low), "and", str(high))
ans = int(((low+high)/2))

while int((low+high)/2) != (low+high):
    print('Is your secret number ' + str(ans) + '?')
    user = input("Enter 'h' if your number is higher. Enter 'l' if your number is lower. Enter 'c' if the guess is correct.\n\n")

    if user == 'l':
        high = ans
        ans = int(((low+high)/2))
        
    elif user == 'h':
        low = ans
        ans = int(((low+high)/2))
        
    elif user == 'c':
        print('Game over. Your secret number was: ' + str(ans))
        break
        
    else:
        print('Error. Try again')