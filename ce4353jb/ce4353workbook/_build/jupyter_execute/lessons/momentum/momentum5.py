#!/usr/bin/env python
# coding: utf-8

# # Spur Dikes
# 
# Momentum balances are useful when analyzing obstructions caused by elements placed in the flow, spur dikes being a meaningful example.  Spur dikes are stone spurs that extend into the stream from the bank to minimize erosion by forcing flow away from the bank. Two to five structures are typically placed in series along straight or concave bank lines where flow lines are roughly parallel to the bank.
# 
# ![](spurdike1.png)
# 
# Spurs are used in river engineering to minimize bank erosion and lateral stream migration, thereby protecting infrastructure such as roads, bridges, and dwellings. It is clear that the physical characteristics of spurs and the resulting flow modifications result in desirable habitat benefits. Redirecting and concentrating flow patterns away from the banks results in key features for aquatic habitat:
# 
# - Deep pools at the tips;
# - Cover for fish, especially when spurs are combined with Large Woody Debris, Willow Posts and Poles or Live Brushlayering;
# - Protection of eroding banks, and resultant reduced sediment loads;
# - Physical habitat diversity characterized by regions of swift and slow current adjacent to one another.
# 
# Single and opposing wing deflectors are used to concentrate water into a selected area of the channel to create scour, thereby accelerating the flow. Wing deflectors can create quiet water resting places for upstream migrating spawners. Opposing wing deflectors are built to deflect the flow to create a scour pool, and sort spawning gravel. They are best used in long uniform glides and riffles to diversify habitat and create velocity shear zones. ([CA Fish and Game, 1998, Stream Restoration Manual](http://www.extranet.vdot.state.va.us/locdes/hydraulic_design/nchrp_rpt544/content/html/WorksCited/California_Salmonid_Stream_Habitat_Restoration_Manual.pdf))
# 
# ![](spurdikephoto.png)
# 
# An array of dikes causes a local scour, with the material redepositing behind the dike  and is thought to be a viable river training method.
# 
# ![](spurdikemodel.png)
# 
# <!--Another use is to direct flows to generate intentional scour and deposition; this use is largely art but one can leverage submerged spurs to impart a component of flow velocity in a desired direction.
# 
# ![](guadelupearroyodrawing.png)-->
# 
# 

# The hydraulics is inherently three dimensional, although meaningful 2D approximations are possible.  Practical consideration beyond any average backwater effect would probably best be served using a high-dimensional CFD model (ie. [SToRM](https://i-ric.org/en/solvers/storm/), [Telemac](http://www.opentelemac.org/))
# 
# :::{note}
# The above models are not trivial, and are examined in other classes (CE-5362).  The download and install can take days, and careful computer configuration is needed.
# :::

# ## References
# 
# 1. [Spur Dikes Hydraulics (YouTube)](https://www.youtube.com/watch?v=tF7wSJzkD4c)
# 2. [Experimental Study on the Influence of Spur Dikes Spacing on Local
# Scouring](http://54.243.252.9/ce-4353-webroot/3-Readings/25903064.pdf)
# 3. [Backwater Effect from Single Spur Dike](http://54.243.252.9/ce-4353-webroot/3-Readings/Backwater_effect_due_to_a_single_spur_dike.pdf)

# In[ ]:




