#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Python program to count the number of characters (character frequency) in a string.

def c(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(c('google.com'))


# In[4]:


#python program to Check for Key in Dictionary Value list.

test_dict = {'Simply' : [{'CS' : 5}, {'Python' : 6}], 'for' : 2, 'CS' : 3} 
 
print("The original dictionary is : " + str(test_dict)) 
 
key = "Python"
res = any(key in ele for ele in test_dict['Simply'])
 
print("Is key present in nested dictionary list ?  : " + str(res)) 


# In[5]:


#python program to Concatenate Dictionary string values.

test_dict1 = {'SC' : 'a', 'is' : 'b', 'best' : 'c'}
test_dict2 = {'SC' : '1', 'is' : '2', 'best' : '3'}
 
print("The original dictionary 1 : " + str(test_dict1))
print("The original dictionary 2 : " + str(test_dict2))
 
res = {key: test_dict1[key] + test_dict2.get(key, '') for key in test_dict1.keys()}
 
print("The string concatenation of dictionary is : " + str(res))


# In[6]:


#python program to print Keys with Maximum value from dictionary.

test_dict = {'Simply' : 2, 'Coding' : 1, 'Python' : 3, 'java': 2}
 
print("The original dictionary is : " + str(test_dict))
 
temp = max(test_dict.values())
res = [key for key in test_dict if test_dict[key] == temp]
 
print("Keys with maximum values are : " + str(res))


# In[7]:


#python program to find dictionary Keys Product.

test_dict1 = {'gfg' : 6, 'is' : 4, 'best' : 7}
test_dict2 = {'gfg' : 10, 'is' : 6, 'best' : 10}
 
print("The original dictionary 1 : " + str(test_dict1))
print("The original dictionary 2 : " + str(test_dict2))
 
res = {key: test_dict2[key] * test_dict1.get(key, 0)for key in test_dict2.keys()}
 
print("The product dictionary is : " + str(res))


# In[ ]:




