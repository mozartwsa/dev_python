name = ''
while True:
    print('please type your name')
    name = input()
    if(name == 'your name'):
        break
print('thanks')


spam = 0
while spam < 5:
    spam += 1
    if spam == 3:
        continue
    print('spam == ' + str(spam))