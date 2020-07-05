#!/usr/bin/env python
# coding: utf-8

# In[11]:


"""
The code below generates a given number of random strings that consists of numbers and 
lower case English letters. You can also define the range of the variable lengths of
the strings being generated.

The code is functional but has a lot of room for improvement. Use what you have learned
about simple and efficient code, refactor the code.
"""

#The main problem that I see in this code is that is hard to understand. The variables are not names properly and it's hard to follow.
"""def RandomStringGenerator(l=12, a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    p = 0
    s = ''
    while p<l:
        import random
        s += random.choice(a)
        p += 1
    return s

def BatchStringGenerator(n, a=8, b=12):
    r = []
    for i in range(n):
        c = None
        if a < b:
            import random
            c = random.choice(range(a, b))
        elif a == b:
            c = a
        else:
            import sys
            sys.exit('Incorrect min and max string lengths. Try again.')
        r.append(RandomStringGenerator(c))
    return r

a = input('Enter minimum string length: ')
b = input('Enter maximum string length: ')
n = input('How many random strings to generate? ')

print(BatchStringGenerator(int(n), int(a), int(b)))"""


# In[19]:


#First we define the variables, we are going to rename some of the variables so the code makes more sense.

#by replacing l for length and a for choice, its clear what these two variables do.

def RandomStringGenerator(lngth=12, choice=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']):
    tries = 0 #p had no meaning so we changed it for tries  
    word = '' #s had no meaning so we changed it to word
    while tries < lngth :
        import random
        word += random.choice(choice)
        tries += 1
    return word

def BatchStringGenerator(num1, num2=8, num3=12): #we replace it by num, num1, num2 to correlate them and know what the machine wants
    result = [] #This is the variable that will keep the final result, so we changed it from r to result
    
    for i in range(num1):
        num3 = None
        if num1 < num2:
            import random
            num3 = random.choice(range(num1, num2))
        elif num1 == num2:
            num3 = num1
        else:
            import sys
            sys.exit('Incorrect min and max string lengths. Try again.')
        result.append(RandomStringGenerator(num3))
    return result

#These will be the input asked to the player
num1 = input('Enter minimum string length: ')
num2 = input('Enter maximum string length: ')
num = input('How many random strings to generate? ')

print(BatchStringGenerator(int(num), int(num1), int(num2)))

