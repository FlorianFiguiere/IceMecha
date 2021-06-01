#!/usr/bin/env python
# coding: utf-8

# # Area sample
# 
# We cut off a piece of the sample so we need to calculate the area left for our sample in order to calculate the theoretical weight needed to do a creep test with $\sigma$ = 0,8 MPa.

# In[1]:


import cmath

Dlarge=52.2
Dsmall=42.0

#attribution of variables used during the program.

r=Dlarge/2 #larger radius of the circle.
h=Dsmall-r #smaller radius of the sample.
f=Dlarge-Dsmall #deflection
alpha=2*cmath.acos(h/r).real
g=9.80665 #m.s^-2
sigmath=0.8 #MPa

#print(alpha*360/(2*cmath.pi))


# In[2]:


#Determination of the area of the bot/top surface of the sample. (in mm²)
Ac=cmath.pi*pow(r,2) #Area of a circle
As=Ac*alpha/(2*cmath.pi) #Area of the circular sector alpha
At=1/2*pow(r,2)*cmath.sin(alpha).real #Area of the isosceles triangle in the circle
A1=As-At #Area of the segment circle

Af=Ac-A1#Final area wanted

#print("Ac=",Ac, "As=",As,"At=",At,"A1=",A1)
print("Area of the sample = {:.2f} mm²".format(Af))


# In[3]:


#Determination of the theoretical weight

Mth=(sigmath*Af-22.38)/(0.14)
M2=(sigmath*Af-19.42)/(0.14)
print("Theoretical weight= {:.1f} g or {:.3f} kg".format(Mth,Mth*0.001))


# In[ ]:




