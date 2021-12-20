#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium
from branca.element import Figure


# In[2]:


# Creating Basemap
fig3=Figure(width=550,height=350)
m3=folium.Map(location=[0,0],tiles='OpenStreetMap',zoom_start=2.5)
fig3.add_child(m3)


# In[3]:


#Adding markers to the map
folium.Marker(location=[27.1755041799186, 78.04209611773581],popup='<h4 style="color:green;">Taj Mahal, India</h3>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)
folium.Marker(location=[41.890401842524774, 12.49222017757944],popup='<h4 style="color:green;">Colosseum,Italy</h3>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)
folium.Marker(location=[20.684586972701645, -88.56608219135173],popup='<h4 style="color:green;">Chichén Itzá, Mexico</h3>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)
folium.Marker(location=[-13.163023719585967, -72.54490599600202],popup='<h4 style="color:green;">Machu Picchu, Peru</h3>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)
folium.Marker(location=[-22.95174233268602, -43.21028412306276],popup='<h4 style="color:green;">Christ the Redeemer, Brazil</h3>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)
folium.Marker(location=[30.329086481775096, 35.444362237162835],popup='<h4 style="color:green;">Petra, Jordan</h3>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)
folium.Marker(location=[40.43222591414546, 116.57083084905777],popup='<h4 style="color:green;">Great Wall of China, China</h3>',tooltip='<strong>Click here to see Popup</strong>').add_to(m3)


# m3

# In[4]:


m3.save("index.html")

