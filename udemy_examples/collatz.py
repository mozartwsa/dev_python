def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print ('Enter number: ')
try:
    number = int(input())

    while True:
        if number == 1:
            break
        number = collatz(number)
        print (str(number), sep=',', end=' ')

    print('\nNumber 1 reached! Bye.')

except ValueError:
    print ('You must type an integer, motherfucker!')
    