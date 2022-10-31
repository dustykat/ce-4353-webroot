#!/usr/bin/env python
# coding: utf-8

# # Junctions
# 
# An important component of hydraulic modeling is handling the behavior of systems with branches and junctions.  HEC-RAS is a link-node type modeling tool at its computation engine level, but a junction logically falls between two nodes (cross sections) yet is not fully a reach.
# 
# Junctions are programmed to either mangae energy losses, or momentum changes, based on user input.

# ## Example
# 
# The figure below is a sketch of a channel and tributary system with a road (bridge) crossing the main channel.
# 
# ![](confluence.png)
# 
# The cross sections are surveyed and the sections are included in the Figure below:
# 
# ![](crosssections.png)
# 
# The figure is a screen capture of the data table that contains the location of the cross sections relative to the diagram (Section 1 is located at distance 0 from the outlet, Section 10 is
# located 1760 feet upstream of the outlet, etc.). 
# The numbers to the right of each section title in the table are the distances upstream from section 1 and should be used as the section names in HEC-RAS. 
# Section 11 connects to the main channel between Section 6 and 7, and that is the meaning of the “\*” symbol in the table. 
# 
# The angle that the tributary forms with the main channel is about 60-degrees. X-LB and Z-LB are distance and elevation relative to the left bank of each section.
# The road is cut into the surrounding grade so that the low chord of the bridge at the main
# channel is at elevation 290, and the roadway surface is at elevation 295 feet.
# 
# The figure below is a table of steady flow conditions to consider.
# 
# ![](boundaryconditions.png)
# 
# Determine if the current bridge low chord can accommodate the different flows. If flow
# cannot clear the low chord, treat the bridge as a large culvert and determine if the roadway
# surface is still passable (not flooded).
# 
# Repeat the analysis assuming the bridge abutments extend 100 feet into the left and right
# over-bank.
# 
# The spreadsheet with the data tables is located at [ConfluenceExampleData.xls](http://54.243.252.9/ce-4353-webroot/ce4353jb/ce4353workbook/lessons/hecras/ConfluenceExampleData.xls)

# In[ ]:




