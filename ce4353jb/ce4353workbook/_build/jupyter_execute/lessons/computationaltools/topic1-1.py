#!/usr/bin/env python
# coding: utf-8

# # Jupyter Notebooks
# 
# The course is mathematically focused and will require developing scripts (computer programs) or spreadsheets.  The default computational environment is a Jupyter Notebook running an iPython kernel.
# 
# :::{note}
# In fact this on-line document is a collection of Jupyter Notebooks rendered using a program called Sphinx that converts the notebooks into a website (which you are now accessing).  For me the author its cool because I just make notebooks and bind them at my leisure (there are some nuances to get figures into the books and embedding code - but its not too hard to do so.  Jupyter as a literate programming environment is quite useful even outside of the University.
# :::
# 
# To follow along with any python examples in these notes, you need to have access to Jupyter Notebook. Jupyter Notebook is an open-source interactive computational environment that is based on a server-client structure. It includes a web server and a web application that works like an integrated development environment (IDE). This web application allows us to create Jupyter Notebook documents (commonly referred to simply as notebooks or IPYNB files) that consist of code, text, and images. To use Jupyter notebook, we have several options:
# 
# #### 1. Anaconda 
# The first option is to install an instance on your own system. The easiest way to do that is to install a software distribution known as [Anaconda](https://www.anaconda.com/). Anaconda comes with over 250 packages pre-installed, including NumPy, pandas, Matplotlib, and Scikit-Learn, all of which we’ll be using in this book. In addition, it includes many useful applications and IDEs,such as the Jupyter Notebook application mentioned above. <font color="magenta">*This is probably the easiest approach if you already have a laptop and want to work offline.*</font>
# 
# #### 2. Google Colaboratory 
# The second option to access Jupyter Notebook is to use Google Colab (short for Google Colaboratory). 
# Google Colab is a free cloud-based Jupyter Notebook environment hosted by Google that requires no installation and offers free access to online computing resources. 
# However, **you need to be connected** to the internet when you use Google Colab. 
# This connection is mainly used to run the code and does not consume much data.
# 
# :::{note}
# Most of the scripts in this book can be cut-and-pasted into a Colab instance and seem to run as expected.  The only realistic limitation is likely bandwidth (and possibly storage for big-data).  Otherwise this is a good compromise and training environment for this course. Files need to be uploaded each connection and are destroyed when you disconnect, so you may need to write code to get files every time.  Anyway it is a useable option.
# :::
# 
# #### 3. Build from Repositories
# A third option is to build a JupyterLab Server on a machine you own (such as AWS Virtual Private Server; Raspberry Pi runing on a home network, or similar set-up) and essentially replicate a Colab-type environment.  This option is not for the faint of heart; it it the structure I used for this document.  If your host machine is running Linux a good starting place is [Installing Jupyter](https://docs.jupyter.org/en/latest/install.html).  This method is most definitely not point-and-click but can build a fully capable system on hardware you can control and scale.  
# 
# :::{note}
# The hardware requirements are modest.  This JupyterBook is developed on my home machine which is a Raspberry Pi 4B 8GB SBC using a 256GB MicroSD card to house the OS and data files.  At current prices the hardware cost is about \$240 so hardware is not a limiting issue.  
# :::
# 

# In[ ]:




