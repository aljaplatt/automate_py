name = ''
while not name:
    print('Enter your name: ')
    name = input().strip()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Have fun!')
print('Done')