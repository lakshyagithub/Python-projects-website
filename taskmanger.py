<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 18:12:25 2022

@author: laksh
"""

import matplotlib.pyplot as plt
import psutil as p

app_name_list = []
app_usage_list = []
count = 0

for process in p.process_iter():
    count = count+1
    if count <= 10:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print("Name : ", name, "-- cpu usage : ", cpu_usage)
        app_usage_list.append(cpu_usage)
        app_name_list.append(name)
        
plt.figure(figsize=(15, 7))
plt.xlabel("Applications")
plt.ylabel("CPU Usage")
plt.bar(app_name_list, app_usage_list, width=0.4, color=("aqua", "green", "aqua", "green", "aqua", "green", "aqua", "green", "aqua", "green"))
=======
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 18:12:25 2022

@author: laksh
"""

import matplotlib.pyplot as plt
import psutil as p

app_name_list = []
app_usage_list = []
count = 0

for process in p.process_iter():
    count = count+1
    if count <= 10:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print("Name : ", name, "-- cpu usage : ", cpu_usage)
        app_usage_list.append(cpu_usage)
        app_name_list.append(name)
        
plt.figure(figsize=(15, 7))
plt.xlabel("Applications")
plt.ylabel("CPU Usage")
plt.bar(app_name_list, app_usage_list, width=0.4, color=("aqua", "green", "aqua", "green", "aqua", "green", "aqua", "green", "aqua", "green"))
>>>>>>> 972fac8b80e0f8ce7db178ee03bc640018baeebb
plt.show()