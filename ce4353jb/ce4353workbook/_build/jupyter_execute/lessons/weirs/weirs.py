#!/usr/bin/env python
# coding: utf-8

# # Weirs
# 
# Used as flow measuring devices and to maintain specific pool elevations in hydraulic systems.
# 
# ## Flow Measurement
# 
# ![](stream_weir.png)
# 
# ## Stage Control - Water Quality Enhancement
# 
# ![](Dobbsweirvdropsjan2006.png)
# 
# ## Stage Control - Erosion Management
# 
# ![](Weir_on_the_river_wear.png)
# 
# ## Stage Control - Navigation
# 
# ![](bath-weir.png)
# 
# ## Stage Control - Diversion/Extraction
# 
# ![](Typical-weir-system-in-Northern-Thailand-consists-of-weirs-and-canals.png)
# 
# ## Examples
# 
# Many types of weirs in the textbook are typically employed for flow measurement.  Most of the weirs pictured are morphologically the same as a handful of well studied types

# ### Sharp-Crested Rectangular Notch Weir
# 
# ![](sharp-crest.png)
# 
# A sketch of a sharp-crested weir (weir plate is thin in the flow direction) is shown below
# 
# ![](sharp-crest-sketch.png)
# 
# Assuming no head loss, atmospheric pressure across AB (implies flow over the crest is like a jet, that is $\Delta p$  is small from top to bottom - the assumption becomes weak when the weir becomes flooded), negligible contraction of the [nappe](https://en.wikipedia.org/wiki/Nappe_(water)).
# 
# Integrating the velocity profile from A to B to obtain a mean section speed in the nappe, and multiplying by the cross section width produces (Eqn 2.39)
# 
# $$ Q = \frac{2}{3}\sqrt{2g}C_d~L~H^{3/2} $$
# 
# Where $L$ is the width (weir length) of the notch crest perpindicular to flow, and $H$ is the static head above the crest height (the flow depth of the nappe at the crest).
# 
# The weir coefficient $C_d$ is determined by weir morphology:
# 
# ![](weir-charts-one.png)
# 
# These charts are used with an adjusted formula
# 
# $$ Q = \frac{2}{3}\sqrt{2g}C_{de}~L_{e}~H_e^{3/2} $$
# 
# where
# 
# $$L_{de}=L + k_L$$
# 
# and
# 
# $$H_e=H + k_H$$
# 
# $k_L$ is read from the chart and $k_H$ is a constant 0.001 m (0.003 ft)
# 
# An alternate approach is a formula for $C_{de}$ (Kindsvater-Carter formula)
# 
# $C_{de} = \beta_1 + \beta_2 \frac{H}{P}$
# 
# where 
# 
# |$\frac{L}{b}$|$\beta_1$|$\beta_2$|
# |---:|---:|---:|
# |1.0|0.602|0.075|
# |0.9|0.599|0.064|
# |0.8|0.597|0.045|
# |0.7|0.595|0.030|
# |0.6|0.593|0.018|
# |0.5|0.592|0.011|
# |0.4|0.591|0.0058|
# |0.3|0.590|0.0020|
# |0.2|0.589|-0.0018|
# |0.1|0.588|-0.0021|
# |0.0|0.587|-0.0023|
# 
# 

# 

# ### Shart-Crested Triangular Notch Weir
# 
# ![](V-notch.png)
# 
# ![](vee-notch-weir-in-brick-tunnel-t.png)

# In[ ]:





# ### Broad-Crested Weir

# In[ ]:





# ### Submerged Rectangular Weir

# In[ ]:





# ### Flumes
# 

# In[ ]:





# ## References
# 
# 1. [What is a weir? (YouTube)](https://www.youtube.com/watch?v=YkR79oDAgOg)

# 

# 

# In[ ]:




