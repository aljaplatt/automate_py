def spam():
    # global allows you to specify that you want to change a global variable, not local
    # useful if both have the same name
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)