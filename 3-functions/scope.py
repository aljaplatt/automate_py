def spam():
    eggs = 'spam local'
    print("2. SPAM", eggs)    # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print("1. bacon 1", eggs)    # prints 'bacon local'
    spam()
    print("3. bacon 2", eggs)    # prints 'bacon local'

eggs = 'global'
bacon()
print("4. global", eggs)        # prints 'global'

# bacon local
# spam local
# bacon local
# global

# bacon 1 bacon local
# SPAM spam local
# bacon 2 bacon local
# global global