# -*- coding: utf-8 -*-
"""K_nearest_neighbor.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jN3JWzEz0pyfD4q-HJVY8cfWVhvnzFbD

# Association Rule Learning
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/gdrive')

!pip install apyori

df=pd.read_csv('/content/gdrive/MyDrive/BDS_practice_data/Market_Basket_Optimisation.csv')
df.head(30)

"""# K-Nearest Neighbor"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""## Loading iris data set and converting into data frame"""

from sklearn.datasets import load_iris
iris=load_iris()
iris

iris.feature_names

df_iris=pd.DataFrame(iris.data, columns=iris.feature_names)
df_iris.head(20)

df_iris['target']=iris.target
df_iris.head(20)

flower=[]
for i in iris.target:
  flower.append(iris.target_names[i]) ## getting flower name with indexing of iris.target_names
df_iris['flower']=flower
df_iris.flower.unique()

# another one line code to do the above
## df['flower_name'] = df.target.apply(lambda x: iris.target_names[x])

"""## data visulization"""

plt.scatter(df_iris[df_iris['flower']=='setosa']['sepal length (cm)'],df_iris[df_iris['flower']=='setosa']['petal length (cm)'], color='green', label='setosa')
plt.scatter(df_iris[df_iris['flower']=='versicolor']['sepal length (cm)'],df_iris[df_iris['flower']=='versicolor']['petal length (cm)'], color='blue', label='versicolor')
plt.scatter(df_iris[df_iris['flower']=='virginica']['sepal length (cm)'],df_iris[df_iris['flower']=='virginica']['petal length (cm)'], color='red', label='virginica')
plt.xlabel('sepal length (cm)')
plt.ylabel('petal length (cm)')
plt.legend()

plt.scatter(df_iris[df_iris['flower']=='setosa']['sepal width (cm)'],df_iris[df_iris['flower']=='setosa']['petal width (cm)'], color='green', label='setosa')
plt.scatter(df_iris[df_iris['flower']=='versicolor']['sepal width (cm)'],df_iris[df_iris['flower']=='versicolor']['petal width (cm)'], color='blue', label='versicolor')
plt.scatter(df_iris[df_iris['flower']=='virginica']['sepal width (cm)'],df_iris[df_iris['flower']=='virginica']['petal width (cm)'], color='red', label='virginica')
plt.xlabel('sepal width (cm)')
plt.ylabel('petal width (cm)')
plt.legend()

"""## split the data set into test and train"""

df_iris.columns

x1=df_iris.iloc[:,:4].values
y1=df_iris['target'].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x1,y1,test_size=0.25,random_state=1)
print(len(x_train))
print(len(x_test))

"""## call KneighorsClassifier class from the sklearn.Neighors api and fit model"""

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=10)## set n_neighbors value in int, this calculates euc dist from int data points on each group
knn.fit(x1,y1)

"""### get the accuracy score/fit score and predict"""

knn.score(x1,y1)

knn.predict([[6.25,3.0,5.0,1.6]])

"""# knn on social network data"""

from google.colab import drive
drive.mount('/content/gdrive')

df_social=pd.read_csv('/content/gdrive/MyDrive/TakeoData/Social_Network_Ads.csv')
df_social.head(20)

type(df_social.Purchased[0])

df_social['Bought']=df_social['Purchased'].apply(lambda x: 'no' if x==0 else 'yes')
df_social.head(5)

"""## Data visualization"""

plt.scatter(df_social[df_social['Purchased']==0]['Age'],df_social[df_social['Purchased']==0]['EstimatedSalary'], color='green', label='not purchased')
plt.scatter(df_social[df_social['Purchased']==1]['Age'],df_social[df_social['Purchased']==1]['EstimatedSalary'], color='blue', label='purchased')
plt.xlabel('Age')
plt.ylabel('EstimatedSalary')
plt.legend()

"""## split into test and train"""

df_social.columns

x2=df_social.drop(['Purchased','Bought'], axis=1).values
y2=df_social.iloc[:,-2:-1].values

x2.ndim

y2.ndim

from sklearn.model_selection import train_test_split
x2_train,x2_test,y2_train,y2_test=train_test_split(x2,y2,test_size=0.15,random_state=4)
len(x2_train),len(x2_test)

"""## fit KNN algorithm"""

from sklearn.neighbors import KNeighborsClassifier
knn_social=KNeighborsClassifier(n_neighbors=10)
knn_social.fit(x2_train,y2_train)
knn_social.score(x2_test,y2_test)

"""following above warning the y2 seems to be 2d array.. converting it into 1d array with ravel() function"""

y2=y2.ravel()

"""rerun the fit model"""

from sklearn.neighbors import KNeighborsClassifier
knn_social=KNeighborsClassifier(n_neighbors=20)
knn_social.fit(x2_train,y2_train)
knn_social.score(x2_test,y2_test)

knn_social.predict([[30,120000]])

"""k mEANS == unsupervised learning approach
k n n ==supervised learning approach you pass features(x) and label(y)
"""