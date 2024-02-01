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

# #### General Formula
# 
# The general formula for a V-Notch weir (with experimentally determined discharge coefficients for the geometry in the sketch below 
# 
# ![](v-notch-sketch.png)
# 
# is
# 
# $$Q = C_d \frac{8}{15} \sqrt{2g}~tan(\frac{\theta}{2})H^{5/2}$$
# 
# #### Kindsvater-Carter formula
# 
# In the Kindsvater-Carter form using the concept of effective head ($H_e = H + k_H$) is 
# 
# $$Q = C_{de} \frac{8}{15} \sqrt{2g}~tan(\frac{\theta}{2})H_e^{5/2}$$

# In[ ]:





# ### Broad-Crested Weir

# A broad crested weir is distinct from the sharp edged wiers by virtue of having a substantial portion of the crest in the direction of flow of at least several approach depth equivalents.
# 
# The wier below is nearly flooded, but yopu can see the crest length relative to the approach depth, the central "channel" is a notch in the system for lower flows/pool elevations.
# 
# ![](BCweir4.png)
# 
# The weir below is clearly either a flow measuring weir or a debris trap - the notch is to guarentee enough flow to scour the trap after a substantial solids flow event.  The "crest" is pretty long (in the direction of flow) no doubt to withstand the shear forces that would be imparted by a slurry (water and solids) impacting the upstream face.  Notice the geometry - it is a notch-type weir with at least three notches.  The small width portion.  The wider portion near at elevation a little below the gaging vault (or prison cell), and a widest portion using the gaging vault as part of the vertical wall of the notch.  This kind of weir is called acomposite-geometry  weir.  
# 
# ![](BCweir3.png)
# 
# The next two images show a broad crested weir set into a trapezoidal channel, first just after construction waiting for the concrete to harden,
# 
# ![](BCweir2.png)
# 
# and then with water flowing in the weir.
# 
# Notice the two hydrographers admiring the weir and awaiting their chance to fish in the newly constructed fish race.
# 
# ![](BCweir1.png)
# 
# The sketch below shows the geometry of a broad crested weir, the width of the weir across the channel is $L$ whereas the length of the weir in the direction of flow is $I$ in the drawing.  
# 
# ![](broad-crested-sketch.png)
# 
# Key points in the broad crested weir are that the crest is long enough so that parallel flow and critical depth occur somewhere along the crest.
# 
# The critical energy at this location is 
# 
# $$H_e = \frac{3}{2}[\frac{(Q/L)^2}{g}]^{1/3}$$
# 
# The discharge equation is
# 
# $$Q = C_d~(\frac{H_e}{H})^{3/2}~\frac{2}{3}[\frac{2}{3}g]^{1/2}~LH^{3/2}  $$
# 
# The typical discharge coefficient $C_d$ is 0.848, but increases as the weir "floods" as indicated by the chart above that relates $C_d$ to the depth to crest length ratio.  A flooded weir is called "submerged" and Sturm pages 48-50 have a nice discussion regarding submerged weirs if flow measurement is the goal.
# 
# The gist of the pages is a submergence correction for discharge as
# 
# $$Q_s = Q_{free} * [1-(\frac{H_t}{H})^{10.0}]^{0.95}$$
# 
# The equation above is essentially eqn 2.52 in the textbook with the constants for a broad-crested weir.

# ### Example 2.5 (from Sturm)
# 
# A rectangular broad-crested weir is used in a stormwasser detention pond as part of the outlet structure (most likely to control pool elevation - hence probably a wet bottom pond).  The crest length is 10 feets and the maximum allowable head on the crest is 1.0 ft.  What is the discharge capacity of the weir at free willy?  If the tailwater head is 0.8 ft, what will be the discharge?

# In[1]:


# BC weir - free willy flow
import math
Cd = 0.848
g = 32.2 # feet per second per second
H = 1.0 # feet 
Va = 0.0 # approach velocity, negligible in pond
He = H + (Va**2)/(2*g)
I = 10.0 # actually unknown in this example, but are told it is a broad crest
L = 10.0 # feet

Q = Cd*((He/H)**(3/2))*(2/3)*math.sqrt((2*g/3))*L*H**(3/2)
print("Discharge: ",round(Q,1)," cfs")


# In[2]:


# BC weir - submerged flow
# compute submergence reduction factor
Ht = 0.8 # feet
a = 10
b = 0.95
S = (1.0-(Ht/H)**a)**b
Qs = S*Q
print("Discharge: ",round(Qs,1)," cfs")


# ### Flumes
# 
# A flume is another device to measure flow in open channels.  A flume employs contractions and/or a raised bottom section to force flow through critical depth within the measurement section of the flume. A rating curve is provided by manufacturers or if the geometry is known in the critical sectionthat fact can be leveraged to rate the flume.
# 
# Flumes can be pretty small
# 
# ![](flume-small.png)
# 
# Moderate in size
# 
# ![](flume-medium.png)
# 
# And semi-portable installations can be fairly large
# 
# ![](flume-field.png)
# 
# Or even pretty large (notice the dude on the right side trying to figure out how to steal the abandoned bicycle!)
# 
# ![](flume-large.png)

# In[ ]:





# ## References
# 
# 1. [What is a weir? (YouTube)](https://www.youtube.com/watch?v=YkR79oDAgOg)
# 2. [Discharge over Broad-Crested Weir (YouTube)](https://www.youtube.com/watch?v=8QIqPOnpT9Q)
# 3. [Discharge over a Wrecked Angular Weir (YouTube)](https://www.youtube.com/watch?v=JhYmhYuy1bY)
# 4. [Discharge over a Submerged Weir (YouTube)](https://www.youtube.com/watch?v=DE-cb6gH_Js)
# 5. [Discharge over a Trapezoidal Weir (YouTube)](https://www.youtube.com/watch?v=_T_nJD9-su4)
# 6. [Discharge over a Triangle Notched Weir (YouTube)](https://www.youtube.com/watch?v=OeOzDzBBHO0)
# 7. [Parshall Flume (YouTube)](https://www.youtube.com/watch?v=bxHagMo6nm0)
# 8. [Cut-Throat Flume (YouTube)](https://www.youtube.com/watch?v=eY3fDHMxxRg)
# 9. [Flume for Rapid Chemical Mixing (YouTube)](https://www.youtube.com/watch?v=LphKo8YU8jU)
