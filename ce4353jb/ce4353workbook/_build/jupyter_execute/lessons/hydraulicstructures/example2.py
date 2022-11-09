#!/usr/bin/env python
# coding: utf-8

# # Example 16.2.2 from Mays
# 
# Develop the performance curve for an existing 7-ft X 7-ft box culvert, 200-ft long on 5-percent slope designed to convey a 50-year discharge of 600 cfs at a design headwasser elevation of 114-ft as depicted below.
# 
# ![](ex16212.png)
# 
# The roadway is a 40-foot wide gravel road approximated as a broad crested weir with a centerline elevation of 116 ft.  The culvert inlet elevation is 100 ft. Tailwater-depth discharge relationship is:

# In[1]:


tw = [2.6,3.1,3.8,4.1,4.5]
qtw = [400,600,800,1000,1200]
weirL = [0,100,150,200,250,300]
weirH = [116,116.5,117,117.5,118,119]


# Look up in Table 16.2.4 for:
# 
# - $C_d = 2.70$ @ $HW_r =0.57$
# - $Q = C_d(HW_r)^{1.5}$
# - $C_d = 2.97$ @ $HW_r =1.9$
# - $k_t = 1$

# In[2]:


D = 7 # given

qtest = [400,600,700,800,850,1000]


# In[ ]:




