#!/usr/bin/env python
# coding: utf-8

# Q1. What are the two values of the Boolean data type? How do you write them?
# 
# Ans: Two values of boolean data types are: True and False.
#      This can be done by assigning it to variables and print it as shown below:   

# In[1]:


a = True


# In[2]:


b = False


# In[3]:


print(a)


# In[4]:


print(b)


# Q2. What are the three different types of Boolean operators?
# 
# Ans: Following are the three types of boolean operators: AND, OR and NOT

# Q3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and 
#     what it evaluate ).
# 
# Ans: True AND True = True; 
#      True AND False = False; 
#      False AND True = False; 
#      False AND False = False; 
#      True OR True = True; 
#      True OR False = True; 
#      False OR True = True; 
#      False OR False = False; 
#      NOT True = False; 
#      NOT False = True; 

# Q4. What are the values of the following expressions?

# In[5]:


(5 > 4) and (3 == 5)


# In[6]:


not (5 > 4)


# In[7]:


(5 > 4) or (3 == 5)


# In[8]:


not ((5 > 4) or (3 == 5))


# In[9]:


(True and True) and (True == False)


# In[10]:


(not False) or (not True)


# Q5. What are the six comparison operators?
# 
# Ans: == ; 
#      != ; 
#      > ; 
#      < ; 
#      >= ; 
#      <=

# Q6. How do you tell the difference between the equal to and assignment operators? Describe a condition and when you would use one.
# 
# Ans: For comparing variables we use two equal operators (==) to chech whether the variables are equal or not, whereas while assigning values to the variables we use single equal operator (=).
#      Given below is the condition:

# In[11]:


x = 30             # Here assigning 30 to variable x
2*x == 3*x           # Here comparing the two variables whether they are equal or not


# Q7. Identify the three blocks in this code:

# In[12]:


spam = 0

if spam == 10:
    print('eggs')          #Block1

if spam > 5:
    print('bacon')         #Block2

else:
    print('ham')           #Block3
    print('spam')
    print('spam')


# Q8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything     else is stored in spam.
# Ans:

# In[13]:


spam = int(input("Enter a digit to be stored: "))

if (spam==1):
    print("Hello")

elif (spam==2):
    print("Howdy")

else:
    print("Greetings!")


# Q9. If your programme is stuck in an endless loop, what keys you’ll press?
# 
# Ans: We have to press ctrl + c

# Q10. How can you tell the difference between break and continue?
# 
# Ans: The break statement will terminate the loop execution and will take outside the loop, wheras the continue statement will skip the execution of code present in the current iteration and continue to the execution of next iteration of the loop.

# In[14]:


print("printing break statement")
for i in range(10):
    if i==4:
        break;
    print(i)

print("\n")
print("printing cotinue statement")
print("\n")
for i in range(10):
    if i==4:
        continue;
    print(i)


# Q11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)
# 
# Ans: 

# In[16]:


# range(10) will produce series of whole number in ascending order starting from 0 (as a default) and will stop at 10 with default stepsize of 1.
for i in range(10):
    print(i)

print("\n")
print("-"*20)
print("\n")
    
# As a deafault range(0,10) will produce series of whole number in ascending order starting from 0 and stops at 10 with default stepsize of 1
for i in range(0,10):
    print(i)

print("\n")
print("-"*20)
print("\n")
    
# The range(0,10,1) will produce series of whole number in ascending order starting from 0 and stops at 10 with stepsize of 1
for i in range(0,10):
    print(i)


# Q12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
# 
# Ans:

# In[17]:


# using for loop:
for i in range(0,10):
    print(i+1)

print("\n")
print("-"*20)
print("\n")

# using while loop:
num = 1
while num <= 10:
    print(num)
    num += 1


# Q13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
# 
# Ans: To call this function we have to execute spam.bacon()
