#!/usr/bin/env python
# coding: utf-8

# # Momentum

# Momentum is a property of moving things and is the product of mass and velocity.  Angular momentum is the similar property in rotating geometries.  It takes an external force to change the momentum of an object.
# 
# :::{note}
# Except at faster than light travel (FTL) when impulse-momentum no longer applies; instead ones survival depends largely on the skill of the scriptwriter.  As engineers we wear the red shirts and are usually sacrificed, although Scottish engineers seem to last many episodes!
# :::
# 
# In the context of hydraulics many phenomenon which cannot be analyzed using the energy equation succumb nicely to momentum. The primary advantage of the momentum equation are that details of internal (to the control volume) flow paqtterns are irrelevant, only the external forces and momentum fluxes need to be considered.  The momentum balance was used earlier to solve the head loss caused by a bridge pier and this is a typical application of momentum balances.
# 
# It matters greatly in computational hydraulics in unsteady flow. 

# ## Hydraulic Jump
# 
# A [hydraulic jump](https://www.youtube.com/watch?v=7tjf8HWiR3Y) occurs:
# 
# 1. when you startle a sugary liquid, it jumps and spills.  
# 2. when flow transitions for supercritical flow to subcritical flow over a short distance.
# 3. when a lowrider activates the car hydraulics and hops.
# 
# well for this lesson its the second answer.
# 
# :::{note}
# The highest lowrider hop 414.65 cm (163.25 in) and was achieved by Robert White (USA) at the Los Magnificos car show in Austin, Texas, USA on 21 November 2015. The hop was made by a converted school bus called the Honeybadger.
# :::
# 
# 
# Here's a useful sketch.  Supercritical flow upstream meets subcritical downstream.  Downstream controls the flow, $Q$ is same but the downstream velocity os exchanged for flow depth, a bit of energy is lost in the transition.  The jump itself is quite turbulent and has a practical value in chemical mixing as well as energy dissipation.
# 
# ![](hydjump-sketch.png)
# 
# Engineering design is typically concerned with forcing jumps in armored channel sections otherwise the energy will chew away at the channel and destroy thangs.
# 
# A control volume around the jump might look like
# 
# ![](controlvolume.png)
# 
# The jumps occur over a short distance, so the friction term is usually small compared to the other forces and change in momentum flux.
# 
# Conservation of momentum is
# 
# $$ \sum F_x = Fp_1 - Fp_2 - Fr = \rho Q(V_2 - V_1)$$
# 
# The pressure forces assume hydrostatic distributions so that 
# 
# $$ Fp = p_i A_i = \rho g \bar h_{i} A_i$$
# 
# where $\bar h_i$ is the depth to the centroid of the cross section ($\frac{y}{2}$
# 
# Making the substitutions and neglecting the friction term yields
# 
# $$  (\rho~g~\bar h_{1}~A_1) - (\rho~g~\bar h_{2}~A_2) = \rho Q(V_2 - V_1)$$
# 
# Rearrangement gives
# 
# $$  (\rho~g~\bar h_{1}~A_1) + \rho Q~V_1 = (\rho~g~\bar h_{2}~A_2) + \rho Q~V_2$$
# 
# Divide by $\rho~g$
# 
# 
# $$  (h_{1}~A_1) + \frac{Q^2}{gA_1} = (h_{2}~A_2) + \frac{Q^2}{gA_2}$$
# 
# The result above is called the momentum function, and interestingly looks similar to the specific energy function with the section geometry explicitly part of the balance.
# 
# $$ M_1 = M_2$$
# 
# The balance is at the two sections implies that the two different depths have the same momentum function, and these are called the alternate (upstream) and sequent (downstream) depths.
# 
# The function itself is dependent on section geometry a few analytical examples are:
# 
# ![](momentumfunctions.png)
# 
# 
# For other cross sections, numerical methods are employed.
# 
# ## References
# 
# 1. [Hydraulic Jump (YouTube)](https://www.youtube.com/watch?v=7tjf8HWiR3Y )

# 
