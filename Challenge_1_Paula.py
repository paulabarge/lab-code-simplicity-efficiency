#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('Welcome to this calculator!')
print('It can add and subtract whole numbers')


def calculator():
        #Asking for the numbers 
        a = int(input('Please choose your first number: '))
        if type(a) != int:
            return "You haven't said a number.Please write a number to perform the calculation"
        c = int(input('Please choose your second number: '))
        if type(c) != int:
            return "You haven't said a number.Please write a number to perform the calculation"
        
        #Asking for what operation you want to perform 
        b = input('What do you want to do? plus or minus: ')
                  
        #Performing the calculation
        if b == "plus":
            return int(a + c)
        elif b == "minus":
            return int(a - c)
        else:
            return print("Please type minus or plus to perform the calculation") + input('What do you want to do? plus or minus: ')
        
calculator()

