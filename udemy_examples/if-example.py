print('Say your name: ')
name = input()
if name == 'Alice':
    print('Hi Alice')
elif name == 'Bob':
    print('Hi Bob')
elif name == 'Mozart':
    print('Hi Mozart')
elif name:
    print("whatever")
else:
    print('Hi someone else')