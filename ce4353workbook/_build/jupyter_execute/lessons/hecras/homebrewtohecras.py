#!/usr/bin/env python
# coding: utf-8

# # Homebrew Examples to HEC-RAS
# 
# Here we take our homebrew examples and perform the simulations using HEC-RAS
# 
# ## Backwater Curve
# The figure below is a backwater curve for a rectangular channel with discharge over a weir (on the right hand side — not depicted).The channel width is 5 meters, bottom slope 0.001, Manning’s n = 0.02 and discharge Q = 55.4m$^3$.
# 
# ![](bw_curve1.png)
# 
# :::{note}
# The figure is from: Page 85. Koutitas, C.G. (1983). Elements of Computational Hydraulics. Pentech Press, London 138p. ISBN 0-7273-0503-4
# :::
# 
# Our goal is to replicate the figure using HEC-RAS.
# 
# ## Frontwater Curve
# 
# The figure below is another illustrative case. Here the water discharges into a horizontal channel at a rate of 1 m$^3$ per second per meter width. Assuming Manning’s n = 0.01 we wish
# to compute the profile downstream of the gate and determine if it will extend to the sharp edge.
# 
# ![](bw_curve2.png)
# 
# :::{note} 
# The figure is from: Jaeger, C. (1957). Engineering Fluid Mechanics. St. Martin’s Press. 529p. 
# :::
# 
# 
# We would need to know the critical depth for the section (≈ 0.47meters), then compute the profile moving from the gate downstream (a frontwater curve with respect to the gate).
# 
# Again just replicate the case using HEC-RAS.
# 
# ## Non-Prismatic Channel Backwater Curve
# A plan view of a rectangular channel of variable width as shown below
# 
# ![](NonPrismaticExample.png)
# 
# 
# The channel conveys $Q=100~m^3/sec$, with a bottom slope of $0.001$ and average Manning's $n$ value of $0.033$.  
# A backwater curve is caused by a weir at the downstream end (to the right in the figure) by a 7 meter tall weir.
# Flow depth over the weir is at critical depth $h_c = 2.17$ meters.  Normal flow in the upstream portion for 10-meter channel width is $h_n = 5.6$ meters.  Using the fixed space step method determine and plot a profile view of the water surface and channel bottom.
# 
# 

# In[ ]:




