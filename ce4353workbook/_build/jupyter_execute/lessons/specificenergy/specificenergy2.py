#!/usr/bin/env python
# coding: utf-8

# # Froude Number
# 
# Recall the Froude number,
# 
# $$ Fr = \frac{V}{\sqrt{gy}}$$
# 
# The specific energy diagram identifies three flow regimes:
# 
# 1. supercritical; characterized by small $y$, large $V$, greater than wave celerity $c$, $Fr >1$
# 2. critical; minimum specific energy for the channel and flow; $y=y_c$, $Fr = 1$, velocity is wave celerity.
# 3. subcritical;characterized by large $y$, small $V$, smaller than wave celerity $c$, $Fr <1$
# 
# Wave celerity is speed of shallow waves on watre surface.  Drop a pebble on water, ripples move away from the impact, speed of the ripples is the celerity - controlled largely by water depth.
# 
# Choking is the situation where the channel bottom is high enough or downstream width is small enough to just start to slow flow and cause the flow depth to increase.

# ## Critical Depth Non-Rectangular
# Generally use the depth measured from thalweg point, and apply principles of continunity already described, key is
# 
# ![](cross-section.png)
# 
# $$dA = T(y)dy$$
# 
# So the hydraulic characteristics are quite important. We obtain the depth-area, depth-perimeter, depth-topwidth functions for odd shapes by numerical tabulations and interpolation.
# 
# $$E = y + \frac{\alpha Q^2}{2gA^2}$$
# 
# at critical depth
# 
# $$ \frac{dE}{dy} = 0 = 1 - \frac{\alpha Q^3}{gA^3}\frac{dA}{dy}$$
# 
# In terms of hydraulic depth we have
# 
# $$ D = \frac{A}{T}$$
# 
# and at critical flow
# 
# $$D_c = \frac{A_c}{T_c}$$
# 
# and substitution gives
# 
# $$E_c = y_c + \frac{D_c}{2}$$
# 
# Table 2.1 copied below has geometric element equations for a few common geometries:
# 
# ![](table2-1.png)
# 
# 
# >An on-line calculator that can handle trapezoidal, triangular and rectangular is at <br>
# > [Trapezoidal Channel Geometric Elements](http://54.243.252.9/toolbox/swhydraulics/TrapezoidChannelUS/TrapezoidChannelUS.html)
# > <br>and a similar tool for circular channels is at <br>
# > [Circular Channel Geometric Elements](http://54.243.252.9/toolbox/swhydraulics/CircularChannelUS/CircularChannelUS.html)

# ## Contractions & Expansions
# 
# The general equation for steady flow in expansions
# 
# ![](expansion.png)
# 
# and/or contractions
# 
# ![](contraction.png)
# 
# is
# 
# $$ y_1 + \frac{\alpha V_1^2}{2g} + z_1 = y_2 + \frac{\alpha V_2^2}{2g} + z_2 + K_L |\frac{1}{A_2^2}-\frac{1}{A_1^2}|\frac{Q^2}{2g}$$
# 
# where the last term is the change in velocity head multiplied by a loss coefficient (structurally like a Darcy-Wiseass head loss model)
# 
# $$K_L = \frac{1 - \frac{b_1}{b_2}}{1 + \frac{b_1}{b_2}}$$
# 
# applicable when $Fr<\frac{1}{2}$
# 
# Expansions tend to have higher head loss because of the flow separation in the wake/shadow formed by the walls at the abrubt change in width.  If the designer arranges for a smooth transition the head loss can be minimized but not eliminated. 
# 
# For contractions the following is often applied
# 
# $$h_L = (0.11 ~\text{to}~ 0.23)\frac{V^2}{2g}$$
# 
# the lower value for a rounded transition, the larger for a sharp transition.

# ## Overbank Flow
# 
# ![](overbank.png)
# 
# Different resistance to flow in different parts of the cross section.  Can obtain different $y_c$ in each part of the cross section. Can also have large velocity differences across the section with high velocities in the main channel section (usually) and possibly very low velocities in the overbanks.  It creates a problem for 1-D models if the velocity itself is important (as opposed to just getting the total discharge right).

# ## Examples
# 
# ## References
