#!/usr/bin/env python
# coding: utf-8

# # HEC-RAS 
# 
# [HEC-River Analysis System (RAS)](https://www.hec.usace.army.mil/software/hec-ras/)  the U.S. Army Corps of Engineers’ software package for modeling constant flows and flood-wave movement through a series of river cross sections, including the presence of a culvert structure. The software and documentation are available free of charge.
# 
# There are multiple versions. Choose the version for your particular architecture (computer)
# 
# 

# ## Installation
# 
# Navigate to the HEC-RAS website, select software appropriate for your computer.  Apple users will choose the Linux versions and have to figure out an interface, or get a [CodeWeaver](https://www.codeweavers.com/) application layer, or get [Parallels](https://www.parallels.com/pd/general/?gclid=CjwKCAjw79iaBhAJEiwAPYwoCFORJ8sEPl3m0sP2EEj6TExbC4rKqt6LUsS22AVAmTK8PkgnfLqbkxoC_dcQAvD_BwE), or build a [Cloud Application](https://aws.amazon.com/free/compute/lightsail/?trk=56417dfe-8849-4622-bfa4-7ec30bd6f5a3&sc_channel=ps&s_kwcid=AL!4422!3!536323500429!e!!g!!aws%20lightsail&ef_id=CjwKCAjw79iaBhAJEiwAPYwoCKquJK3Cnwmaf8sZZURFgvZO3FdYDyiQufkvEyD4DGuUCtGIGII50BoC77EQAvD_BwE:G:s&s_kwcid=AL!4422!3!536323500429!e!!g!!aws%20lightsail)
# 
# :::{note}
# The HEC-RAS On-Line below is such a cloud application hosted on AWS.  You can get your own for \$12.00/month.
# :::
# 
# For a typical winders machine:
# 
# ![](hecrasinstall.png)
# 
# Then run the installer
# 
# ![](installer.png)
# 
# Upon sucessful install you should be able to select the program and launch it and get the control interface
# 
# ![](success.png)
# 
# To install the examples, navigate to the help tab and select download examples
# 
# ![](examples.png)
# 
# :::{note}
# Usually the above works, unless you try something fancy and are [clueless](https://www.imdb.com/title/tt0112697/).  If you cannot figure it out go [here](https://apply.mysubwaycareer.com/us/en/)
# :::

# ## HEC-RAS On-Line
# 
# A fully provisioned Windows Implementation of HEC-RAS is located at:
# 
# - server_name: **kittyinthewindow.ddns.net**
# - user_name: **texas-skew**
# - passwd: **peakfq73$hare**
# 
# Users must access using [Remote Desktop Protocol](https://learn.microsoft.com/en-us/windows-server/remote/remote-desktop-services/clients/remote-desktop-mac) (Built into Windows, Apple Store has a free Mac application).

# ## Example 5.5 (Sturm pp. 188-191)
# 
# The example in the textbook loosely corresponds to the steady flow example in HEC-RAS from Chapter 4 of the users manual.
# 
# ![](hecrasexample4.png)
# 
# In class we will examine the HEC-RAS supplied example to learn how to drive HEC-RAS.  The motivated reader may be able to convert the existing HEC-RAS supplied example into the book example by changing stationing of the cross sections, assuming the geometry is essentially the same.

# ## References
# 

# In[ ]:




