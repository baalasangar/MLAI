# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:08:28 2020

@author: admin
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

tips = sns.load_dataset("tips")
tips.dtypes
tips.head(10)

# Relational plots - Statistical analysis is a process of understanding how variables in a dataset relate to each other and how those relationships depend on other variables
# Scatter plot 
sns.scatterplot(x="total_bill", y="tip",hue="sex",size="size",style="time", data=tips)
# Size can determine the bill ?- yes it's there is a relation in the min bill
tips["size"].unique()
sns.scatterplot(x="size",y="total_bill", data=tips,x_jitter = True,y_jitter=True)

# Plotting the same chart using relplot()
sns.relplot(x="total_bill", y="tip",hue="sex",size="size",style="time", data=tips)

# Using Color palette 
cmap = sns.cubehelix_palette(as_cmap=True,light=0.1,dark=0.5,reverse=True)
sns.relplot(x="total_bill", y="tip",hue="size", data=tips, palette=cmap)


# Line Chart

df = pd.DataFrame(dict(time=np.arange(500),
                       value=np.random.randn(500).cumsum()))
g = sns.relplot(x="time", y="value", kind="line", data=df)

# if there are multiple measure for the X value.default behavior in seaborn is to aggregate the multiple measurements at each x value by plotting the mean

fmri = sns.load_dataset("fmri")
fmri.head(10)
sns.relplot(kind='line', x="timepoint",y="signal",data=fmri) # plots  with 95% confident internal

# To turn off the aggregration set estimator = None
sns.relplot(kind='line', x="timepoint",y="signal",
            data=fmri,estimator=None,markers=True)

sns.relplot(x="timepoint", y="signal", hue="region", style="event",
            markers=True,  kind="line", data=fmri)



sns.relplot(x="timepoint", y="signal", hue="region",
             units="subject",estimator=None,
            kind="line", data=fmri.query("event == 'stim'"));


# using cols and Rows for multiple plots in same canvas

sns.relplot(x="total_bill", y="tip", hue="smoker",
            col="time", data=tips) # For each Time variable we will have different plot

# col & row will help to create matrix 

sns.relplot(x="timepoint", y="signal", hue="subject",
            col="region", row="event", height=3,
            kind="line", estimator=None, data=fmri)


# Plotting with Categorial data

# Categorial scatterplot - "Strip"   

tips = sns.load_dataset("tips")
tips.head(10)

sns.catplot(x="sex", y="total_bill",hue="smoker", data=tips)

# setting jitter=False

sns.catplot(x="sex", y="total_bill",hue="smoker",jitter=False, data=tips)

# Categorial scatterplot - "swarm" - 
# adjusts the points along the categorical axis using an algorithm that prevents them from overlapping. It can give a better representation of the distribution of observations, although it only works well for relatively small datasets

sns.catplot(x="day", y="total_bill", kind="swarm", data=tips);


# Categorial distripution plot
# Kind = "boxen" and "violin"
sns.catplot(data=tips,x="smoker",y="tip",hue="sex", kind="box")

sns.catplot(data=tips,x="smoker",y="tip",hue="sex", kind="violin",inner="stick")

# Combining plots

viplot = sns.catplot(data=tips,x="smoker",y="tip", kind="violin")
sns.swarmplot(data=tips,x="smoker",y="tip",ax=viplot.ax)


# Plots for doing statistical estimation 

titanic = sns.load_dataset("titanic")
titanic.dtypes
titanic.head(10)
titanic["fare"].describe()
#df = titanic.groupby(["sex","class"]).describe()
#df["survived"]

# bar plot
sns.catplot(kind="bar", data=titanic,x="sex",y="survived", hue="class")

sns.catplot(kind="count", data=titanic.query("survived == 1"), x="class")

sns.catplot(kind="point",data=titanic, x="class", y="survived", hue="sex")


# Visualizing the distripution of a dataset

# plotting univariable distripution

sns.distplot(titanic['age'])

sns.distplot(titanic['age'],kde = False)

sns.distplot(titanic['age'],hist= False)

# plotting bivariable distripution
# Joinplot - show both scatterplot and distripution density for individual variables

sns.jointplot(data=titanic,x="age",y="fare")

sns.jointplot(data=titanic,x="age",y="fare",kind="hex")

sns.jointplot(data=titanic,x="age",y="fare",kind="kde")


# pairwise relationship in data

titanic[["age","fare","parch"]]

sns.pairplot(titanic[["age","fare","parch"]])


# linear regression

tips.dtypes

sns.lmplot(data=tips,x="total_bill", y="tip")

tips["sex_bool"] = tips["sex"] == "Female"
tips["big_tip"] = (tips.tip / tips.total_bill) > .15

# logistic=True can be used for ploting logistic regression - need to explore more
sns.lmplot(x="total_bill", y="big_tip", data=tips,
           logistic=True, y_jitter=.03);

#  Multiple plot 

g = sns.FacetGrid(tips, col="sex", hue="smoker")
g.map(sns.scatterplot, "total_bill", "tip", alpha=.7)
g.add_legend();

g = sns.FacetGrid(tips, row="smoker", col="time", margin_titles=True)
g.map(sns.regplot, "size", "total_bill", color=".3", fit_reg=False, x_jitter=.1);
















