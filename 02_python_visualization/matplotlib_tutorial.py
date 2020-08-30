import matplotlib.pyplot as plt
import numpy as np

# Plot a line Graph
# Sympols for marks 

# - Solid line style
# -- Dashed line style
# -. Dash-dot line style
# : Dotted line style
# . Point marker
# , Pixel marker
# o Circle marker
# v Triangle_down marker
# ^ Triangle_up marker
# < Triangle_left marker
# > Triangle_right marker
# 1 Tri_down marker
# 2 Tri_up marker
# 3 Tri_left marker
# 4 Tri_right marker
# s Square marker
# p Pentagon marker
# * Star marker
# h Hexagon1 marker
# H Hexagon2 marker
# + Plus marker
# x X marker
# D Diamond marker
# d Thin_diamond marker
# | Vline marker
# _ Hline marker



x = np.random.rand(10)
y = x * 2
# 
plt.plot(x,y) # plot the Graph with Blue line
plt.plot(x,y,"g>") # g> green Traingle 

plt.title("Title")
plt.xlabel("Xlabel")
plt.ylabel("ylable")

plt.annotate('annotation marking', 
             (0.4,0.75),
            xytext=(0.5, 0.9),
            textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', 
            verticalalignment='top')


plt.show()

month = ["jan","Feb","march"]
mdata = [250,350,150]
max(mdata)
plt.bar(month, mdata)
#plt.xticks(np.array(0,max(mdata),step=50))
plt.show() 

# Horizontally  Bar chart ()

month = ["Jan","Feb","Mar","Apr","May"]
HYDsales = [50,60,55,75,65]
BNGsales = [55,50,70,60,80]

index = np.arange(5)
width = 0.30
plt.bar(index,HYDsales,width,color="green",label="Hyd Sales")
plt.bar(index+width,BNGsales,width,color="blue",label="Bang Sales") # Index+Width move the second bar next to firts bar
plt.xticks(index+ width/2, month) 
plt.legend(loc="best")
plt.show()

# Horizontal  Stacked bar chart
plt.bar(index,HYDsales,width,color="blue",label="Hyd Sales")
plt.bar(index,BNGsales,width,color="red",label="Bang Sales",bottom=HYDsales)
plt.title("Vertically Stacked Bar Graphs")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.xticks(index, month)
plt.legend(loc="best")
plt.ylim(10,300)
plt.show()


plt.barh(index,HYDsales,width,color="green",label="Hyd Sales")
plt.barh(index+width,BNGsales,width,color="blue",label="Bang Sales")
plt.yticks(index+width/2,month)
plt.legend(loc="best")
plt.show()


plt.barh(index,HYDsales,width,color="green",label="Hyd Sales")
plt.barh(index,BNGsales,width,color="blue",label="Bang Sales",left=HYDsales)
plt.yticks(index,month)
plt.legend(loc="best")
plt.show()

# Pie Chart

HYDsales = [30,60,55,90,35]
perArr = list(map(lambda x : round((x/sum(HYDsales))*100),HYDsales))
plt.pie(perArr,labels=month,explode=5*[0.1])
plt.show()

# Histogram

data1 = np.random.randn(1000)
plt.hist(data1)
plt.show()

# Scatter plot

data2 = np.random.randn(1000)
plt.scatter(data1, data2)
plt.show()

# 3D ploting

#from mpl_toolkits import mplot3d

height = np.array([130,135,120,145,165,175,180,145,150,160,140,170,165,135,155])
weight = np.array([60,70,65,75,80,90,95,85,70,78,88,72,68,77,88])

ax = plt.axes(projection="3d")
ax.scatter3D(height,weight)
ax.set_xlabel("Height")
ax.set_ylabel("Weight")
plt.show()



# Multiple Charts in single graph 

# When subplot is single row or single column
plt.subplot(1,2,1)
plt.plot([1,2,3,4],[10,20,30,40],"go")
plt.title("1st subplot")
plt.subplot(1,2,2)
x = np.arange(1,5)
y = x**5
plt.plot(x,y,"r^")
plt.title("2nd subplot")
plt.suptitle("Sales Plots")
plt.show()


# When subplot is matrix

x = np.arange(1,5)
y = x**5
fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(6,6))
ax[0,1].plot([1,2,3,4],[10,20,30,40],"go")
ax[0,0].plot(x,y,'r^')
ax[0,1].set_title("Squares")
ax[0,0].set_title("Cubes")
plt.show()

# Pltting headmap 
# https://matplotlib.org/gallery/images_contours_and_fields/image_annotated_heatmap.html#sphx-glr-gallery-images-contours-and-fields-image-annotated-heatmap-py

vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

harvest = np.array([[0.8, 2.4, 2.5, 3.9, 0.0, 4.0, 0.0],
                    [2.4, 0.0, 4.0, 1.0, 2.7, 0.0, 0.0],
                    [1.1, 2.4, 0.8, 4.3, 1.9, 4.4, 0.0],
                    [0.6, 0.0, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 6.3]])

fig, ax = plt.subplots()
ax.imshow(harvest)

ax.set_xticks(np.arange(len(farmers)))
ax.set_xticklabels(farmers)
plt.setp(ax.get_xticklabels() ,rotation=45)

# to show the value 
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")


fig.tight_layout()
plt.show()



