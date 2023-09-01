# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 19:21:51 2023

@author: HP
"""

import pandas as pd
df1=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\boys_names.xlsx")
df2=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\girls_names.xlsx")
pd.concat([df1,df2],axis=0,ignore_index=True)
pd.concat([df1,df2],axis=1)
df2.shape
df1.shape


# In[]:
df3=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\FatherFamily_members.xlsx")
df4=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\motherFamily_members.xlsx")
pd.concat([df3,df4],axis=1)


# In[]:
df5=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\sisters_names.xlsx")
df6=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\brothers_names.xlsx")
pd.concat([df5,df6],axis=1)    


# In[]:
dal_items=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\dal_items.xlsx")
veg_items=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\vegfood_items.xlsx")
pd.concat([dal_items,veg_items],axis=1)


# In[]:
soup_items=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\soup_items.xlsx")
fry_items=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\fry_items.xlsx")
pd.concat([soup_items,fry_items],axis=1)


# In[]:
chicken_items=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\Chicken_items.xlsx")
mutton_items=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\mutton_items.xlsx")
pd.concat([chicken_items,mutton_items],axis=1)


# In[]:
winter=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\winterseason_names.xlsx")
summer=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\summerseason_names.xlsx")
rainy=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\rainyseason_names.xlsx")
pd.concat([winter,summer,rainy],axis=1)
pd.concat([winter,summer,rainy],axis=0,ignore_index=True)


# In[]:
red=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\red_colour.xlsx")
white=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\whiteflowers_names.xlsx")
pink=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\pinkflowers_names.xlsx")
yellow=pd.read_excel(r"C:\Users\HP\OneDrive\Desktop\Fathima\importing_files\yellowflowers_names.xlsx")
pd.concat([red,white,pink,yellow],axis=0,ignore_index=True)

