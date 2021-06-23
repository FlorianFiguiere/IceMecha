#!/usr/bin/env python
# coding: utf-8

# # Area sample
# 
# We cut off a piece of the sample so we need to calculate the area left for our sample in order to calculate the theoretical weight needed to do a creep test with $\sigma$ = 0,8 MPa.

# In[1]:


from Various_Functions import*


# Give the value Dlarge (and Dsmall if required) in millimeter (see figure below) :

# In[2]:


Dlarge=54.8 # millimeter
Dsmall=42.6 # millimeter


# rVeau=<img src="../images/circle_Dlarge_Dsmall.png" alt="circle_diameters" class="bg-primary mb-1" width="400px">

# In[3]:


help(area_tronc_cyl)
help(theor_weight)


# In[4]:


Af=area_tronc_cyl(Dlarge,Dsmall)
Mth=theor_weight(Af)


# In[5]:


print("Area of the sample = {:.2f} mm²".format(Af))
print("Theoretical weight= {:.1f} g or {:.3f} kg".format(Mth,Mth*0.001))


# If needed, there is [the demonstration of the calcul](Demonstration_Area_Calcul.ipynb) made above.
