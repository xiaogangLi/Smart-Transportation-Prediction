# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 19:18:47 2017

@author: Administrator
"""

### 预测2016年6月早上8：00--9:00的旅行时间 ###


import numpy as np
import xgboost as xgb
import scipy.io as sio

# Prepare data 

link_ID = list(np.load(r'E:\智慧交通预测挑战\Code_ReadData\link_ID.npy'))
link_length = np.load(r'E:\智慧交通预测挑战\Code_ReadData\link_length.npy')
link_wedth = np.load(r'E:\智慧交通预测挑战\Code_ReadData\link_wedth.npy')
link_top_in_links = np.load(r'E:\智慧交通预测挑战\Code_ReadData\link_top_in_links.npy')
link_top_out_links = np.load(r'E:\智慧交通预测挑战\Code_ReadData\link_top_out_links.npy')
link_top_link_ID = list(np.load(r'E:\智慧交通预测挑战\Code_ReadData\link_top_link_ID.npy'))


week6date = np.load(r'E:\智慧交通预测挑战\Model\week6date.npy')
work6date = np.load(r'E:\智慧交通预测挑战\Model\work6date.npy')
Date = np.load(r'E:\智慧交通预测挑战\Model\Date.npy')
OneHotCode = np.load(r'E:\智慧交通预测挑战\lastTrainingData\其他\OneHotCode.npy')
times = list(np.load(r'E:\智慧交通预测挑战\lastTrainingData\其他\time.npy'))

count = 0  # 计数：应该为 118800
resu = []  # 保存8:00-9:00之间生成的样本
for d in range(len(Date)):
    
    filepath = r'E:\智慧交通预测挑战\Model\0758_0800_new_supp2_sort_LXG\time_interval_month6_date_'
    filename = Date[d][8::]+'_features.mat'
    temp_samples = sio.loadmat(filepath+filename)['time_interval_07_features']
    flag = '58'
    
    for t in range(30): # 30个时间片段 //////////////////////////////////////////
        
        # 连接 one hot code
        initial_samples = []
        for i in range(len(temp_samples)):
            if (flag == '58'):
                
                initial_samples.append(list(temp_samples[i][0:22])+list(OneHotCode[-1]))
                
            else:
                ix = times.index(flag)
                initial_samples.append(list(temp_samples[i][0:22])+list(OneHotCode[ix]))
        flag = times[t]
            
        # 初始化样本预测
        initial_samples = xgb.DMatrix(np.array(initial_samples))
        if Date[d] in work6date:
            bst.load_model('xgbmodel_work') # 导入模型     
        if Date[d] in week6date:
            bst.load_model('xgbmodel_week') # 导入模型
        pre_travel_time = bst.predict(initial_samples) # 0列
        
        # 保存数据
        for i in range(132):
            if (times[t] == '58'):
                sss = link_ID[i]+'#'+Date[d]+'#['+Date[d]+' 08:'+times[t]+':00,'+Date[d]+' 09:'+'00'+':00)#'+str(pre_travel_time[i])
            else:
                sss = link_ID[i]+'#'+Date[d]+'#['+Date[d]+' 08:'+times[t]+':00,'+Date[d]+' 08:'+times[t+1]+':00)#'+str(pre_travel_time[i])
            resu.append(sss)

        ############################## 特征 ########################################                            
        length = link_length                           # 1列
        width = link_wedth                             # 2列
        ben_v = link_length/pre_travel_time            # 3列
        haveSY = []                                    # 4列
        haveXY = []                                    # 10列
        for i in range(len(link_ID)):
            idx = link_top_link_ID.index(link_ID[i])
            # 上游
            if len(link_top_in_links[idx]) == 0:
                haveSY.append(0.0)
            else:
                haveSY.append(1)
            # 下游
            if len(link_top_out_links[idx]) == 0:
                haveXY.append(0.0)
            else:
                haveXY.append(1)
            
        SY_num = []                                    # 5列
        XY_num = []                                    # 11列       
        for i in range(len(link_ID)):
            idx = link_top_link_ID.index(link_ID[i])
            if len(link_top_in_links[idx]) == 0:
                SY_num.append(0.0)
            else:
                SY_num.append(link_top_in_links[idx].count('#')+1)
            if len(link_top_out_links[idx]) == 0:
                XY_num.append(0.0)
            else:
                XY_num.append(link_top_out_links[idx].count('#')+1)
            
        SY_sumlen = []                                   # 6列 
        XY_sumlen = []                                   # 12列 
        SY_sumwidth = []                                  # 7列 
        XY_sumwidth = []                                  # 13列 
        SY_meantime = []                                  # 8 列
        XY_meantime = []                                  # 14 列 
        SY_meanV = []                                     # 9 列 
        XY_meanV = []                                      # 15 列 
        for i in range(len(link_ID)):
            idx = link_top_link_ID.index(link_ID[i])
            if len(link_top_in_links[idx]) == 0:
                SY_sumlen.append(0.0)
                SY_sumwidth.append(0.0)
                SY_meantime.append(0.0)
                SY_meanV.append(0.0)
            else:
                length0 = 0
                wedth = 0
                time = 0
                speed = 0
                for j in range(link_top_in_links[idx].count('#')+1):
                    idex1=link_ID.index(link_top_in_links[idx][j*19+j+0:j*19+j+19])
                    length0 = length0 + link_length[idex1]
                    wedth = wedth + link_wedth[idex1]
                    time = time + pre_travel_time[idex1]
                    speed = speed + link_length[idex1]/pre_travel_time[idex1]
                SY_sumlen.append(length0)
                SY_sumwidth.append(wedth)
                SY_meantime.append(time/(link_top_in_links[idx].count('#')+1))
                SY_meanV.append(speed/(link_top_in_links[idx].count('#')+1))
            if len(link_top_out_links[idx]) == 0:
                XY_sumlen.append(0.0)
                XY_sumwidth.append(0.0)
                XY_meantime.append(0.0)
                XY_meanV.append(0.0)
            else:
                length0 = 0
                wedth = 0
                time = 0
                speed = 0
                for j in range(link_top_out_links[idx].count('#')+1):
                    idex1=link_ID.index(link_top_out_links[idx][j*19+j+0:j*19+j+19])
                    length0 = length0 + link_length[idex1]
                    wedth = wedth + link_wedth[idex1]
                    time = time + pre_travel_time[idex1]
                    speed = speed+link_length[idex1]/pre_travel_time[idex1]
                XY_sumlen.append(length0)
                XY_sumwidth.append(wedth)
                XY_meantime.append(time/(link_top_out_links[idx].count('#')+1))
                XY_meanV.append(speed/(link_top_out_links[idx].count('#')+1))
    
        bjs_w = width - SY_sumwidth                       # 16 列
        xjb_w = XY_sumwidth - width                       # 17 列
        xjs_v = np.array(XY_meanV) - np.array(SY_meanV)                       # 18 列
        xjs_w = np.array(XY_sumwidth) - np.array(SY_sumwidth)                # 19 列
        sjx_t = np.array(SY_meantime) - np.array(XY_meantime)                # 20 列
        allwide = width +SY_sumwidth+XY_sumwidth         # 21 列
        # 转换
        pre_travel_time=np.transpose(np.array(pre_travel_time,ndmin=2))
        length=np.transpose(np.array(length,ndmin=2))
        width=np.transpose(np.array(width,ndmin=2))
        ben_v=np.transpose(np.array(ben_v,ndmin=2))
        haveSY=np.transpose(np.array(haveSY,ndmin=2))
        SY_num=np.transpose(np.array(SY_num,ndmin=2))
        SY_sumlen=np.transpose(np.array(SY_sumlen,ndmin=2))
        SY_sumwidth=np.transpose(np.array(SY_sumwidth,ndmin=2))
        SY_meantime = np.transpose(np.array(SY_meantime,ndmin=2))
        SY_meanV=np.transpose(np.array(SY_meanV,ndmin=2))
        haveXY=np.transpose(np.array(haveXY,ndmin=2))
        XY_num=np.transpose(np.array(XY_num,ndmin=2))
        XY_sumlen=np.transpose(np.array(XY_sumlen,ndmin=2))
        XY_sumwidth=np.transpose(np.array(XY_sumwidth,ndmin=2))
        XY_meantime=np.transpose(np.array(XY_meantime,ndmin=2))
        XY_meanV=np.transpose(np.array(XY_meanV,ndmin=2))
        bjs_w=np.transpose(np.array(bjs_w,ndmin=2))
        xjb_w = np.transpose(np.array(xjb_w,ndmin=2))
        xjs_v=np.transpose(np.array(xjs_v,ndmin=2))
        xjs_w=np.transpose(np.array(xjs_w,ndmin=2))
        sjx_t=np.transpose(np.array(sjx_t,ndmin=2))
        allwide=np.transpose(np.array(allwide,ndmin=2))
    
        ##########################################################################
    
        temp_samples = np.concatenate((pre_travel_time,length,width,ben_v,haveSY,SY_num,SY_sumlen,
                                       SY_sumwidth,SY_meantime,SY_meanV,haveXY,XY_num,XY_sumlen,
                                       XY_sumwidth,XY_meantime,XY_meanV,bjs_w,xjb_w,xjs_v,xjs_w,sjx_t,allwide),axis = 1)  
    
# 写入数据
with open(r'E:\智慧交通预测挑战\Model\Results.txt','w') as f:
    for i in range(len(resu)):
        f.write(resu[i])
        count = count+1
        if i < (len(resu)-1):
            f.write('\n')
           
