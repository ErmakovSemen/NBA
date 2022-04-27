#!/usr/bin/env python
# coding: utf-8

# In[254]:


import pandas as pd
import json


# In[273]:


with open('BIGDATA_dr.json','r') as picked_json:
    picked = json.load(picked_json)


# In[274]:


picked = pd.DataFrame(picked)


# In[275]:


with open('BIGDATA_undr-.json','r') as losers_json:
    losers = json.load(losers_json)


# In[276]:


losers = pd.DataFrame(losers)


# In[277]:


data = pd.concat([picked,losers],axis = 0,  ignore_index = 'True')


# In[278]:


data


# In[289]:


fd = data


# In[290]:


positions = pd.get_dummies(fd.pos)


# In[291]:


fd = pd.concat([fd,positions],axis = 1)


# In[297]:


#fd.info()


# In[293]:



fd  = fd.drop('draft_year',axis = 1).drop('name',axis = 1).drop('pos',axis = 1)


# In[294]:


fd,y = fd.drop('drafted',axis = 1),fd['drafted']


# In[295]:


fd.head()


# In[296]:


scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))

d = scaler.fit_transform(fd)

scaled_df = pd.DataFrame(d, columns=fd.columns)
scaled_df.columns


# In[194]:


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


# In[304]:


X = scaled_df

# X1 = X.drop('fgm',axis = 1).corr()
# for col in X1.columns:
#     print(col, X1[col].sort_values().apply(lambda x: abs(x))[:3])


# In[404]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3,random_state = 18)


# In[415]:


cl = SGDClassifier(loss= 'log',penalty = 'l2', alpha = 0.001, max_iter=1000)


# In[416]:


cl.fit(X_train,y_train)


# In[417]:


cl.coef_


# In[418]:


cl.intercept_


# In[419]:


accuracy_score(cl.predict(X_test),y_test)


# In[386]:


confusion_matrix(cl.predict(X_test),y_test)


# In[387]:


from sklearn.model_selection import GridSearchCV
base_estimator = SGDClassifier()

best_model = GridSearchCV( 
    base_estimator,
    param_grid = 
        {'alpha' : [0.001,0.01,0.1,1],
        'loss' : ['log','squared_error','modified_huber'],
        'l1_ratio' : [0,0.15,0.3,0.5,0.7,1],
         'max_iter' : [1000]},
    
                        )


# In[421]:


# best_model.fit(X_train,y_train)
# pr = best_model.predict(X_test)
# accuracy_score(pr,y_test)


# In[389]:


from sklearn.linear_model import  LogisticRegression


# In[401]:


cl_1 = LogisticRegression(C=0.4)
cl_1.fit(X_train,y_train)


# In[402]:


accuracy_score(cl_1.predict(X_test),y_test)


# In[ ]:




