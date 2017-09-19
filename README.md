

```python
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.colors
import seaborn
import os

# Retrieve current working directory (`cwd`)
cwd = os.getcwd()
print(cwd)

path=os.getcwd()

# Change directory 
#os.chdir("/path/to/your/folder")

cdata_csv = os.path.join('Desktop', 'city_data.csv')
rdata_csv = os.path.join('Desktop', 'ride_data.csv')

# Read file with Pandas, and store its contents in a new variable
cdata_csv_df = pd.read_csv(cdata_csv)
rdata_csv_df = pd.read_csv(rdata_csv)
#print(cdata_csv_df)
#print(rdata_csv_df)
print(cdata_csv_df.head())
print(rdata_csv_df.head())
```


```python
# Merge the two data frames on city 

merged_city_and_rides_df = pd.merge(left=cdata_csv_df, right=rdata_csv_df, how='left', on=["city","city"])
#print(merged_city_and_rides_df)

```


```python
#new pd frame for plot values
#city:  group by city name for each 
#average fare per type: mean of city fares  group by type
#type:  from the original city_df.  
#total no rides per type: count instances of ids 
#total no drivers per type: each city row contains the total driver count for that city, group by type 

```


```python
merged_city_and_rides_df.columns
```


```python
y=(merged_city_and_rides_df.groupby('type').agg({'fare':'mean'}))
print(y)
```


```python
z1=(merged_city_and_rides_df.groupby('type').agg({'fare':'sum'}))
print(z1)
```


```python
x=(merged_city_and_rides_df.groupby('type').agg({'ride_id':'count'}))
print(x)
```


```python
d = (cdata_csv_df.groupby("type").agg({"driver_count":"sum"}))
print(d)
```


```python
s= (cdata_csv_df.groupby("city").agg({"driver_count":"sum"}))
#print(s)
```


```python
plt.figure()
# set the figure boundaries

# Build a scatter plot for each City type

colors = ["gold", "lightskyblue", "lightcoral"]
labels = ['Rural','Suburban', 'Urban']
gold_dot = plt.scatter(x,y, marker='o', color=colors[0])
blue_dot = plt.scatter(x,y, marker='o', color=colors[1])
coral_dot = plt.scatter(x,y, marker='o', color=colors[2])


plt.scatter(x,y,d,  c=colors, 
            alpha=0.8,  edgecolors='none')

plt.style.use('seaborn-white')


plt.xlim([10, 1800])
plt.ylim([10, 100])

plt.title("Pyber Ride Sharing Data(2016)")
plt.xlabel("Total Number Rides Per City Type")
plt.ylabel("Average Fare by city type")
plt.grid(True)



```


```python
plt.legend((blue_dot, gold_dot, coral_dot),
           ('Suburban', 'Rural', 'Urban'), mode ="Expanded",
           scatterpoints=1, markerscale = 1.0,
           loc='upper right',
           ncol=1,
           fontsize=10, title='City Types', labelspacing=0.5)


plt.show()

# Save the figure
plt.savefig("City_RideShare.png")

```


```python
fig = plt.figure()
ax = fig.add_subplot(111)

labels = ["Rural", "Suburban", "Urban"]
fares = (merged_city_and_rides_df.groupby('type').agg({'fare':'sum'}))

colors = ["gold", "lightskyblue", "lightcoral"]
# how big is the explosion, and what should explode?
explode = (0.1, 0, 0)

ax.set_title("% of Total Fares per City Type")

# the first two %'s format the number. The last one is what is displayed on the graph
ax.pie(fares, explode=explode, labels=labels,autopct="%1.1f%%",colors=colors, shadow=True, startangle=160)

plt.savefig("pie_fares.png")
plt.show()
```


```python
fig = plt.figure()
ax = fig.add_subplot(111)

labels = ["Rural", "Suburban", "Urban"]
rides = (merged_city_and_rides_df.groupby('type').agg({'ride_id':'count'}))

colors = ["gold", "lightskyblue", "lightcoral"]
# how big is the explosion, and what should explode?
explode = (0.1, 0, 0)

ax.set_title("% of Total Rides per City Type")

# the first two %'s format the number. The last one is what is displayed on the graph
ax.pie(rides, explode=explode, labels=labels,autopct="%1.1f%%",colors=colors, shadow=True, startangle=160)

plt.savefig("pie_rides.png")
plt.show()
```


```python
fig = plt.figure()
ax = fig.add_subplot(111)

labels = ["Rural", "Suburban", "Urban"]
drivers = (cdata_csv_df.groupby("type").agg({"driver_count":"sum"}))

colors = ["gold", "lightskyblue", "lightcoral"]
# how big is the explosion, and what should explode?
explode = (0.1, 0, 0)

ax.set_title("% of Total Drivers per City Type")

# the first two %'s format the number. The last one is what is displayed on the graph
ax.pie(drivers, explode=explode, labels=labels,autopct="%1.1f%%",colors=colors, shadow=True, startangle=160)

plt.savefig("pie_drivers.png")
plt.show()
```


```python

```
