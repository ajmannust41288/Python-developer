from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
# df=sns.load_dataset("tips")
# df.corr()# corr is for correlation
# df.head()
# df.tail()
# df.dtypes
# sns.heatmap(df.corr())
# Bivaraiate Analysis
# sns.jointplot(x='tip',y='total_bill',data=df,kind='hex')
# sns.jointplot(x='tip',y='total_bill',data=df,kind='reg') # reg means Regression
# sns.pairplot(df,hue="day")
# sns.displot(df['tip'])
# sns.displot(df["tip"],kde=False,bins=10)
# sns.displot(df["tip"],kde=True,bins=10)
# sns.countplot(x="sex",data=df)
# sns.countplot(x="smoker",data=df)
# sns.countplot(x="day",data=df)
# sns.countplot(y="day",data=df)
# sns.barplot(x="total_bill",y="sex",data=df)
# sns.barplot(x="total_bill",y="sex",data=df,palette="rainbow")
# sns.boxplot(x="sex",y="total_bill",data=df,palette="rainbow")
# sns.boxplot(x="total_bill",y="day",hue="smoker",data=df,palette="rainbow")
# sns.boxplot(x="total_bill",y="day",hue="smoker",data=df)
# sns.violinplot(x="total_bill",y="day",hue="smoker",data=df)
# sns.violinplot(x="total_bill",y="day",hue="smoker",data=df,palette="rainbow")
# Stack plots examples
# stack plot
# from matplotlib import pyplot as plt
# days=[1,2,3,4,5]
# sleeping=[7,8,6,11,7]
# eating=[2,3,4,3,2]
# working=[7,8,7,2,2]
# playing=[8,5,7,8,13]
# plt.plot([],[],color='m',label='Sleeping',linewidth=5)
# plt.plot([],[],color='c',label='Eating',linewidth=5)
# plt.plot([],[],color='r',label='Working',linewidth=5)
# plt.plot([],[],color='k',label='Playing',linewidth=5)
# plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','k'])
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('stck plot')
# plt.legend()
# plt.show()
# pie chart plot examples
# slices=[85,2,29,3]
# activities=['Businessman','Healthy','Richman','Doctor']
# cols=['c','m','r','b']
# plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,
#         explode=(0,0.1,0,0),autopct='%1.1f%%')
# plt.title('Abdusalam  Life Expectaion ')
# plt.show()
# second examples of pie chart
# slices=[9,3,2,1,15]
# activities=['Businessman','SSP','Chowkidar','Engineer','Doctor']
# cols=['c','m','g','r','b']
# plt.pie(slices,labels=activities,colors=cols,explode=[0,0.1,0,0,0],autopct='%1.1f%%')
# plt.title('Abdusalam Expectation')
# plt.show()
#stackplot examples
# days=[1,2,3,4,5]
# security=[9,4,6,2,7]
# businessman=[5,6,7,8,9]
# healthy=[8,9,4,6,2]
# engineer=[8,5,3,1,9]
# doctor=[11,13,14,15,17]
# plt.plot([],[],color='c',label='businessman',linewidth=5)
# plt.plot([],[],color='m',label='security',linewidth=5)
# plt.plot([],[],color='g',label='healthy',linewidth=5)
# plt.plot([],[],color='r',label='engineer',linewidth=5)
# plt.plot([],[],color='b',label='doctor',linewidth=5)
# plt.stackplot(days,security,businessman,healthy,engineer,doctor,colors=['c','m','g','r','b'])
# plt.legend()
# plt.title("Abdusalam Expectation")
# plt.show()
# bar plot examples
# plt.bar([1,3,5,7,9],[5,2,7,8,2],label="abdusalam1")
# plt.bar([2,4,6,8,10],[8,6,2,5,6],label="abdusalam2",color='g')
# plt.legend()
# plt.xlabel('ab speed study')
# plt.ylabel('ab life')
# plt.title('Abdusalam life ')
# plt.show()
# sns.catplot(x="day",y="total_bill",kind="boxen",data=df)
# a=sns.load_dataset("iris")
# b=sns.FacetGrid(a,col="species")
# b.map(plt.hist,"sepal_length")
# a=sns.load_dataset("flights")
# b=sns.FacetGrid(a)
# b.map(plt.scatter)

#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# from matplotlib import inline
# train=sns.load_dataset("titanic")
# print(train.head())
# print(train.isnull())
# sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
# sns.set_style('whitegrid')
# sns.countplot(x='survived',data=train)
# sns.countplot(x='survived',hue='sex',data=train,palette='RdBu_r')
# sns.countplot(x='survived',hue='pclass',data=train,palette='rainbow')
# sns.displot(train['age'].dropna(),kde=False,color='darkred',bins=40)
# i will use matplotlib functions hist to see the distributions
# train['age'].hist(bins=30,color='darkred',alpha=0.3)
# sns.countplot(x='sibsp',data=train)
# train['fare'].hist(color='green',bins=40,figsize=(8,4))
# plt.figure(figsize=(12,7))
# sns.boxplot(x='pclass',y='age',data=train,palette='winter')
# def imput_age(cols):
#     age=cols[0]#if class is age first class
#     pclass=cols[1]#if class is passenger class
#     if pd.isnull(age):
#         if pclass==1:
#             return 37
#         elif pclass==2:
#             return 29
#         else:
#             return 24
#     else:
#         return age
# train['age']=train[['age','pclass']].apply(imput_age,axis=1)
# sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap='viridis')
# train.drop('deck',axis=1,inplace=True)
# print(train.head())
# print(train.info)
# sex=pd.get_dummies(train['sex'],drop_first=True)
# embark=pd.get_dummies(train['embarked'],drop_first=True)
# train.drop(['sex','embarked','class','who'],axis=1,inplace=True)
# print(train.head())
# add again
# train=pd.concat([train,sex,embarked],axis=1)
# print(train.head())
# print(train.drop('survived',axis=1).head())
# print(train['survived'].head())
# from sklearn.model_selection import train_test_split
# x_train,x_test,y_train,y_test=train_test_split(train.drop('survived',axis=1),train['survived'],test_size=0.30,random_state=101)
# print(x_train)
# print(y_train)
# print(y_test)
# from sklearn.linear_model import LogisticRegression
# logmodel=LogisticRegression()
# logmodel.fit(x_train,y_train)
# predictions=logmodel.predict(x_test)
# from sklearn.metrics import confusion_matrix
# accuracy=confusion_matrix(y_test,predictions)
# print(accuracy)
