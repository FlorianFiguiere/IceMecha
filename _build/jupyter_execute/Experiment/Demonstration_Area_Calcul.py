#!/usr/bin/env python
# coding: utf-8

# # Demonstration
# 
# We will demonstrate below the formula used to calcule the area of our sample.
# During this demonstration, we will consider the following circle and areas : 
# 
# - $A_{c}$ The area of the circle (radius [OA]).
# - $A_{t}$ The area of the isosceles triangles within the circle (OAB).
# - $A_{s}$ The area of the circular sector alpha.
# - $A_{1}$ The area of the segment circle (center O define by the chord [AB]).
# - $A_{f}$ The area wanted.
# 
# INSERER IMAGE DU CERCLE AVEC LEGENDE

# ## Trivial area
# 
# We will admite the following formula because there are pretty simple and wellknown equation/simple math.
# 
# $$ A_{c}= \pi r^{2} $$
# $$ A_{t}= \frac{[AB][OH]}{2}$$
# $$ A_{1}=A_{s}-A_{t}$$
# $$ A_{f}=A_{c}-A_{1}$$

# ## Area of the circular sector alpha
# 
# We consider the equation of a circle : $x^{2} + y^{2} = r^{2}$ but also
# $$
# \left\{
#     \begin{array}{ll}
#         x=rcos(\theta) \\
#         y=rsin(\theta)
#     \end{array}
# \right.
# $$
# $$
# \left\{
#     \begin{array}{ll}
#         \frac{dx}{d\theta}=-rsin(\theta) \\
#         \frac{dy}{d\theta}=rcos(\theta)
#     \end{array}
# \right.
# $$

# If we take a look at a triangle with $\frac{dx}{d\theta}$, $\frac{dy}{d\theta}$ and $\frac{dl}{d\theta}$ as lenght, we can write that :
# $$
# dl=\sqrt{\frac{dx}{d\theta}^{2}+\frac{dy}{d\theta}^{2}}d\theta
# $$
# So we have 
# $$
# dl=\sqrt{r^{2}sin(\theta)^{2}+r^{2}cos(\theta)^{2}}d\theta \\
# dl=rd\theta 
# $$
# Thus
# $$
# l=\int_0^\alpha rd\theta = r\alpha
# $$
# And
# $$
# A_{s}=\int_0^r ldr=\frac{r^{2}\alpha}{2}
# $$

# ## Final Area
# 
# With a bit of trigonometry, we can easily get the following equations :
# $$ \frac{[OH]}{[OA]}=cos(\frac{\alpha}{2}) $$
# $$ \frac{[AB]}{[OA]}=sin(\frac{\alpha}{2}) $$
# So we have, with $[OH]= r$ : 
# $$A_{t} = r^{2}sin(\frac{\alpha}{2})cos(\frac{\alpha}{2})$$
# However, according to the following trigonometric equation, we have :
# $$ sin(a)cos(b)= \frac{1}{2}[sin(a+b)+sin(a-b)]$$
# Thus, with $a=b=\frac{\alpha}{2}$ :
# $$A_{t} = \frac{r^{2}}{2}sin(\alpha)$$
# 
# 
# 

# We can deduce :
# $$A_{1}=\frac{A_{c}\alpha}{2\pi} - \frac{r^{2}}{2}sin(\alpha)$$
# Than :
# $$A_{f}=A_{c}(1-\frac{\alpha}{2\pi}) + \frac{r^{2}}{2}sin(\alpha)$$

# Left to to : 
# 
# Add ref number in equation
# 
# sources : https://calculis.net/aire/segment-disque
# https://fr.wikipedia.org/wiki/Longueur_d%27un_arc
# 
