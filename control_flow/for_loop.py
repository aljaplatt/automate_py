# print('My name is')
# for i in range(5):
#     print(f'Alex Five Times ({str(i)})')

print('My name is')
for i in range(5):
    if i % 2 == 0:
        continue
    print(f'Alex Five Times ({str(i)})')

print("odd:")
for i in range(1, 11, 2):
    print(i)

print("even:")
for i in range(0, 11, 2):
    if i == 0:
        continue
    print(i)

print("backwards")
for i in range(10, 0, -1):
    print(i)


total = 0
for num in range(101):
    total+= num
print("TOTAL: ", total)