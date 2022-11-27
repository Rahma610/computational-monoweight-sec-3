#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pyopenms import *


# In[14]:


seq = AASequence.fromString("AVKA")    
mtotal = seq.getMonoWeight()
mz = seq.getMZ(1) 
print("Monoisotopic mass of peptide [M] is", mtotal)


# In[18]:


seq = AASequence.fromString("AVKA")

print("The peptide", str(seq), "consists of the following amino acids:")
aatotal = 0
for aa in seq:
    print(aa.getName(), ":", aa.getMonoWeight())
    aatotal += aa.getMonoWeight()


# In[19]:


if mtotal == aatotal:
    print("the monoisotopic weight of the sequence is equal to the monoisotopic weight od its amino acids individually")
else:
    print("they are not equal")


# In[ ]:




