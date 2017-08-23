# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 22:13:18 2017

@author: Administrator
"""

# train model

import numpy as np
import xgboost as xgb
import matplotlib.pyplot as plt
from sklearn.linear_model import ElasticNetCV
from sklearn.preprocessing import scale,normalize
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from xgboost import plot_importance
from matplotlib import pyplot
from sknn.mlp import Regressor,Layer

# %%
# data

# 工作日数据
if 1:
    RworkingData345 = np.load(r'E:\智慧交通预测挑战\Model\data\RworkingData345.npy')
    RworkingData6 = np.load(r'E:\智慧交通预测挑战\Model\data\RworkingData6.npy')
    
    
    data1 = RworkingData345
    data2= RworkingData6
    
    N1 = len(RworkingData345)   # 训练样本的数量;len(RworkingData345)
    N2 = len(RworkingData6)   # 测试样本的数量 len(RworkingData6)
    
# 周末数据
if 0:
    RweekendDdata345 = np.load(r'E:\智慧交通预测挑战\Model\data\RweekendDdata345.npy')
    RweekendDdata6 = np.load(r'E:\智慧交通预测挑战\Model\data\RweekendDdata6.npy')
    
    data1 = RweekendDdata345
    data2 = RweekendDdata6
    
    N1 = len(RweekendDdata345)   # 训练样本的数量;len(RworkingData345)
    N2 = len(RweekendDdata6)   # 测试样本的数量 len(RworkingData6)

# %%

deleteFeatures = list([22]) # 删除特征list([22]) //////4/10//////////////////////////////////////////

# train data and label
trainingdata = np.delete(data1[:,0:-1][0:N1,:],deleteFeatures,axis=1) # axis=1删除列
traininglabel = data1[:,-1][0:N1]
      

# test data
testdata = np.delete(data2[:,0:-1][0:N2,:],deleteFeatures,axis=1) # axis=1删除列
testlabel = data2[:,-1][0:N2]

# %%
# preprocessing data

# 预处理（归一化）
if 0:
    X = normalize(trainingdata,norm = 'l2',axis=1)  # traing data;axis = 1, 独立地归一化每一个样本(每一行)
    y = traininglabel               # traing label

    T = normalize(testdata,norm = 'l2',axis=1)  # test data; axis = 1,独立地归一化每一个样本(每一行)
    t = testlabel               # test label


# 预处理（标准化每一列）   
if 0:
    X = scale(trainingdata,axis=0)  # traing data; axis=0 是对列（特征）标准化
    y = traininglabel               # traing label

    T = scale(testdata,axis=0)  # test data;axis=0 是对列（特征）标准化
    t = testlabel               # test label
    

# 不预处理（比预处理的结果好！）
if 1:
    X = trainingdata  
    y = traininglabel 

    T = testdata
    t = testlabel 
    
  
# %%

########################### training model #########################################

# %%      

# glmNet 
if 0:
    # train 
    
    l1 = [0.0001,0.0005,0.001,0.005,0.01,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,
     0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9, 0.95, 1.0]
    glmNet_model = ElasticNetCV(l1,n_alphas=100, alphas=None, max_iter=1000, tol=0.0001, cv=5, n_jobs=-1)
    glmNet_model.fit(X,y)

    # test 

    pre_label = glmNet_model.predict(T) 
    
# MLP 
if 0: # RworkingData:最优的random_state = 422，其次是75.RweekendDdata:最优的random_state = 221
    Mape = []
    state = []
    for seed in np.array(list(range(1)))+0:
    
        MLP = MLPRegressor(hidden_layer_sizes=(100,),activation='relu', solver='adam', alpha=0.0001,batch_size=500,
                           learning_rate='invscaling', max_iter=100,random_state=200, tol=0.001, verbose=True,shuffle=True, 
                           learning_rate_init=0.001,power_t=0.5,momentum=0.9, early_stopping=True, validation_fraction=0.1)
    
        # train
        MLP.fit(X,y)
    
        # test
        pre_label = MLP.predict(T)
        loss = t-pre_label # 误差
        MAPE = (sum(abs(loss)/t))/len(t)
        Mape.append(MAPE)
        state.append(seed)
        print(seed)
        print('MAPE = ',MAPE)
    
# Support Vector Regression
if 0:
    svr = SVR(kernel='rbf', degree=3, gamma=1.0/850, coef0=0.0, tol=0.001,
              C=8.0, epsilon=0.0001, shrinking=True, cache_size=200, verbose=True, max_iter=-1)
    svr.fit(X,y) # train
    pre_label = svr.predict(T)
    
# xgboost   
if 1:
    a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # num_round
    b =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # max_depth
    c = np.linspace(0.05,0.99,30) # eta
    para = [] # 参数
    mapeSet = []
    count = 0
    
    xgbtrain = xgb.DMatrix(X,y) # 生成xgb格式的数据
    xgbtest = xgb.DMatrix(T)
    # 搜索最优的参数
    for inn in a:
        for im in b:
            for ie in c:
                num_round = inn
    
                parameters = {'max_depth':im,'eta':ie,'objevtive':'reg:linear','booster':'gbtree',
                'lambda':6.5,'alpha':0.2}
    
                bst=xgb.train(parameters,xgbtrain,num_round) # 训练
#               bst.save_model('xgbmodel') # 保存模型
#               bst.load_model('xgbmodel') # 导入模型

#               importance = bst.get_fscore() # 特征的重要性
#               plot_importance(bst)
#               pyplot.show()
    
                pre_label = bst.predict(xgbtest)
                loss = t-pre_label 
                MAPE = (sum(abs(loss)/t))/len(t)
                mapeSet.append(MAPE)
                para.append([inn,im,ie])
                count=count+1
                print('---> ',count,'......')
    
# scikit-neuralnetwork for regression(有问题，无法训练)
if 0:
    
    mlp = Regressor(layers=[Layer('Rectifier',units=100,weight_decay=0.0001,dropout=0.5),Layer('Linear')],learning_rule='sgd', learning_rate=0.01,
                            batch_size=500, n_iter=10,loss_type = 'mse')
    mlp.fit(X,y)
    pre_label = mlp.predict(T)
'''
# %%
# plot 
loss = t-pre_label # 误差
Z = np.zeros([len(loss)])
plt.plot(loss,'g')
plt.plot(Z,'r')
plt.xlabel('Number of the sample')
plt.ylabel('loss(s)')
plt.title('Visualizing loss')
plt.show()

# %%
# MAPE
MAPE = (sum(abs(loss)/t))/len(t)
print('MAPE = ',MAPE)

# %%
'''
