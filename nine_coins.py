#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
class Nine_Coins:
    def __init__(self): #init pass 
#         self.ht_list=[]
#         self.toss_int=0
#         self.toss_decimal=0
        pass
    def toss(self): #toss definition
        result=[0,1] #throwing coins has two options(0 for head, 1 for tail)
        toss_result=[]
        ht_list=[]
        for i in range(9): #due to nine coins, do nine times to decide head or tail
            head_tail=random.choice(result)
            toss_result.append(head_tail)
            
            if head_tail==0: #ht_list列表(record:head or tail)
                ht_list.append('H') 
            else:
                ht_list.append('T')
            ht_result_string = ''.join(ht_list) #convert into string
          
        return f"Nine_Coins:{ht_result_string}" 
    def __str__(self):
        result=[0,1] #throwing coins has two options(0 for head, 1 for tail)
        toss_result=[]
        ht_list=[]
        for i in range(9): #due to nine coins, do nine times to decide head or tail
            head_tail=random.choice(result)
            toss_result.append(head_tail)
            
            if head_tail==0: #ht_list列表(record:head or tail)
                ht_list.append('H') 
            else:
                ht_list.append('T')
            ht_result_string = ''.join(ht_list) #convert into string
            
            toss_convert=[str(j)for j in toss_result]
            toss_int=int(''.join(toss_convert)) #二進制並成int

            toss_decimal=int(str(toss_int),2) #十進制
        return f"binary:{toss_int} and decimal:{toss_decimal}"
        
  
        

# c=Nine_Coins()
# print(c.toss())
# print(c)


        


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




