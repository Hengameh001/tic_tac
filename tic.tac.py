#!/usr/bin/env python
# coding: utf-8

# Your boss has asked you to create a simple random forest model on the tic_tac_toe dataset. She doesn't want you to spend much time selecting parameters; rather she wants to know how well the model will perform on future data. For future Tic-Tac-Toe games, it would be nice to know if your model can predict which player will win.
# 

# In[14]:


import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# In[15]:



tic_tac_toe = pd.read_csv('/Users/hfakhrav/Desktop/Data scientist2023/Scikit-learn/tic-tac/tic-tac-toe.csv')


# In[16]:


# Create dummy variables using pandas
X = pd.get_dummies(tic_tac_toe.iloc[:,0:9])
y = tic_tac_toe.iloc[:, 9]

# Create training and testing datasets. Use 10% for the test set
X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.1, random_state=1111)


# In[17]:


# Create temporary training and final testing datasets
X_temp, X_test, y_temp, y_test  =    train_test_split(X, y, test_size=0.2, random_state=1111)

# Create the final training and validation datasets
X_train, X_val, y_train, y_val =    train_test_split(X_temp, y_temp, test_size=0.25, random_state=1111)


# In[ ]:




