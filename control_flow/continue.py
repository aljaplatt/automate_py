# while True:
#     print('Who are you?')
#     name = input()
#     if name.title() != 'Joe':
#         break
#     print('Hello, Joe. What is the password?')

while True:
    print('Who are you?')
    name = input()
    if name.title() != 'Joe':
        print('Not joe')
        continue
    while True:
        print('Hello, Joe. What is the password?')
        password = input()
        if password == 'shark':
            break
    break
print('Access granted.')