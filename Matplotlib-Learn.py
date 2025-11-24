import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

            # Line-Chart Section
x= np.array([2023,2024,2025,2026])
y1= np.array([16,21,30,41])
y2=np.array([22,32,43,51])
y3=np.array([41,21,32,61])
plt.grid(axis='both',color="violet",linestyle="dashed",linewidth=3)
styles= dict(marker=".",markersize=21,
         markerfacecolor="#406e4b",
         markeredgecolor="#116e4b",
         linestyle="dotted",linewidth=4
         )
plt.title("Class_Size", fontsize=26, family="Arial",fontweight="bold",color="black")
plt.xlabel("Year",fontsize=21,family="Arial",fontweight="bold",color="blue")
plt.ylabel("Students",fontsize=21,family="Arial",fontweight="bold",color="blue")
plt.plot(x,y1,color="tomato",**styles)
plt.plot(x,y2,color="orange", **styles)
plt.plot(x,y3,color="purple", **styles)
plt.tick_params(axis='both',colors="indigo")
plt.xticks(x)
plt.show()

            # Bar Char
categories= ['Apple','Potato','Mango','Sweets']
values = np.array([3,11,9,19])
plt.title('Daily Consumption')
plt.xlabel('Food')
plt.ylabel('Quantity')
# plt.bar(categories,values,color="lightblue")
plt.barh(categories,values,color="green")
plt.show()

        # Pie chart
categories = ['Freshman','Sophomores','Juniors','Seniors']
values =  np.array([300,100,221,301])
colors =['red','yellow','blue','green']
plt.pie(values, labels=categories, colors=colors,autopct="%1.2f%%",explode=[0,0,0,0.1],shadow= True,startangle=90)
plt.title('Company\'s Employees')
plt.show() 

        # Scatter graph:
'''
A scatter plot uses Cartesian coordinates to display values for typically 
two variables for a set of data. It is the primary tool for visualizing correlation and clustering. 
Each dot represents a single observation, mapped by an x-value and a y-value.
'''
x1=np.array([0,1,1,2,3,4,5,6,7])
y1=np.array([50,60,65,70,75,80,85,90,95])
x2=np.array([0,1,1,2,3,4,5,6,8])
y2=np.array([50,60,65,68,74,80,85,89,98])
plt.scatter(x1,y1,color="skyblue",alpha=0.8,s=21,label="class-A")
plt.scatter(x2,y2,color="green",alpha=0.5,s=19,label="class-B")
plt.xlabel('Study-Hrs')
plt.ylabel('Marks-Obtained')
plt.legend()
plt.show()


        #Histogram:
'''
 A histogram is a representation of the distribution of numerical data. 
        Unlike a bar chart (which compares categories), 
        a histogram groups continuous data into ranges called "bins" 
        and counts how many data points fall into each bucket. 
        It is the go-to tool for checking if your data is skewed, normal, or has outliers.
        '''
scores = np.random.normal(loc=80,scale=10,size=100)
scores = np.clip(scores,0,100)
plt.hist(scores,bins=10,color='lightgreen',edgecolor='black')
plt.title('Exam Score')
plt.xlabel('Scores')
plt.ylabel('No. of Student')
plt.show()

        # Subplots:
'''
Subplots are a layout mechanism that allows you to stack or grid multiple 
distinct plots within a single "Figure" (canvas). It turns a single image into a matrix of charts, 
allowing for side-by-side comparison or multi-variable analysis in one view.
'''        
x= np.array([1,3,5,7,9,11])
figure,axis= plt.subplots(2,2)
axis[0,0].plot(x,x*2,color='green')
axis[0,0].set_title('x*2')

axis[0,1].plot(x,x**2,color='cyan')
axis[0,1].set_title('x**2')

axis[1,0].plot(x,x**3,color='purple')
axis[1,0].set_title('x**3')

axis[1,1].plot(x,x**4,color='blue')
axis[1,1].set_title('x**4')
plt.tight_layout()
plt.show()

            # pandas Plotting
df= pd.read_csv('data.csv')
type_count = df['Type1'].value_counts(ascending=True)
plt.barh(type_count.index,type_count.values,color="#03dffc",edgecolor="black")
plt.title('No. of Pokemon by Primary Type.')
plt.xlabel('Count')
plt.ylabel('Type')
plt.tight_layout()
plt.show()