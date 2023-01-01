<<<<<<< HEAD
  # -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 09:01:20 2022

@author: laksh
"""

import matplotlib .pyplot as plt
import psutil as p
app_name_dict = {}
count = 0
for process in p.process_iter():
    count = count +1
    if count <= 6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print('name : ', name,'-- cpu_usage : ', cpu_usage)
        app_name_dict.update({name:cpu_usage})
        
#--------app_names------------------
keymax=max(app_name_dict,key=app_name_dict.get)
print(keymax)
keymin=min(app_name_dict,key=app_name_dict.get)
print(keymin)
name_list=[keymax,keymin]
print(name_list)

#--------------------CPU USAGE-------
app=app_name_dict.values()
max_app=max(app)
print("maximum", max_app)
min_app=min(app)
print("min",min_app)
max_min_list=[max_app,min_app]
print(max_min_list)

#----------------------plotting------------
plt.figure(figsize=(15,8))
plt.xlabel("Min-Max CPU Consumption")
plt.ylabel("Usage")
plt.bar(name_list,max_min_list,width=0.6,color=("blue","red") )
=======
  # -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 09:01:20 2022

@author: laksh
"""

import matplotlib .pyplot as plt
import psutil as p
app_name_dict = {}
count = 0
for process in p.process_iter():
    count = count +1
    if count <= 6:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print('name : ', name,'-- cpu_usage : ', cpu_usage)
        app_name_dict.update({name:cpu_usage})
        
#--------app_names------------------
keymax=max(app_name_dict,key=app_name_dict.get)
print(keymax)
keymin=min(app_name_dict,key=app_name_dict.get)
print(keymin)
name_list=[keymax,keymin]
print(name_list)

#--------------------CPU USAGE-------
app=app_name_dict.values()
max_app=max(app)
print("maximum", max_app)
min_app=min(app)
print("min",min_app)
max_min_list=[max_app,min_app]
print(max_min_list)

#----------------------plotting------------
plt.figure(figsize=(15,8))
plt.xlabel("Min-Max CPU Consumption")
plt.ylabel("Usage")
plt.bar(name_list,max_min_list,width=0.6,color=("blue","red") )
>>>>>>> 972fac8b80e0f8ce7db178ee03bc640018baeebb
plt.show()