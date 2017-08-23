# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 16:32:26 2017

@author: Administrator
"""
# reading raw data

import numpy as np
import scipy.io as sio
import random
# reading link_info

if 0:
    link_info = list()
    flag = 0
    with open('E:\智慧交通预测挑战\Raw_data\gy_contest_link_info.txt','r') as f1:
        for line in f1:
            if flag:
                link_info.append(list(map(int,line.split(';')))) # int/float
            flag = 1
    
    link_ID = []
    link_length = []
    link_wedth = []
    link_class = []
    for link in link_info:
        link_ID.append(str(link[0]))
        link_length.append(link[1])
        link_wedth.append(link[2])
        link_class.append(link[3])
    np.save(r'E:\智慧交通预测挑战\Code_ReadData\link_ID',link_ID)
    np.save(r'E:\智慧交通预测挑战\Code_ReadData\link_length',link_length)
    np.save(r'E:\智慧交通预测挑战\Code_ReadData\link_wedth',link_wedth)
    np.save(r'E:\智慧交通预测挑战\Code_ReadData\link_class',link_class)
#link_ID=np.load('E:\智慧交通预测挑战\Code_ReadData\link_ID.npy')


# reading link_top
if 0:
    link_top = list()
    flag = 0
    with open('E:\智慧交通预测挑战\Raw_data\gy_contest_link_top.txt','r') as f2:
        for line in f2:
            if flag:
                link_top.append(list(map(str,line.split(';')))) # str
            flag = 1
    link_top_link_ID = []
    link_top_in_links = []
    link_top_out_links = []
    for link in link_top:
        link_top_link_ID.append(link[0])
        link_top_in_links.append(link[1])
        link_top_out_links.append(link[2][0:-1])
    np.save(r'E:\智慧交通预测挑战\Code_ReadData\link_top_link_ID',link_top_link_ID)
    np.save(r'E:\智慧交通预测挑战\Code_ReadData\link_top_in_links',link_top_in_links)
    np.save(r'E:\智慧交通预测挑战\Code_ReadData\link_top_out_links',link_top_out_links)


# reading link_traveltime_training_data

if 0:
    link_traveltime = list()
    flag = 0
    with open(r'E:\智慧交通预测挑战\new_data\newDATA\[新-训练集]gy_contest_traveltime_training_data_second.txt','r') as f3:
        for line in f3:
            if flag:
                link_traveltime.append(list(map(str,line.split(';')))) # str
            flag = 1
#    link_traveltime_link_ID = []
#    link_traveltime_date = []
#    link_traveltime_time_interval = []
#    link_traveltime_travel_time = []
#    for line in link_traveltime:
#        link_traveltime_link_ID.append(line[0])
#        link_traveltime_date.append(line[1])
#        link_traveltime_time_interval.append(line[2])
#        link_traveltime_travel_time.append(line[3][0:-1])
#    unique_date = list(set(link_traveltime_date))
#    np.save(r'E:\智慧交通预测挑战\Code_ReadData\link_traveltime_link_ID',link_traveltime_link_ID)
#    np.save(r'E:\智慧交通预测挑战\Code_ReadData\link_traveltime_date',link_traveltime_date)
#    np.save(r'E:\智慧交通预测挑战\Code_ReadData\link_traveltime_time_interval',link_traveltime_time_interval)
#    np.save(r'E:\智慧交通预测挑战\Code_ReadData\unique_date',unique_date) #
#    np.save(r'E:\智慧交通预测挑战\Code_ReadData\link_traveltime_travel_time',link_traveltime_travel_time)


# 把3月，4月，5月份6点至9点的数据都提出来，然后把6月份6点至8点的数据也提出来
    
if 0:
    link_traveltime = list()
    flag = 0
    with open('E:\智慧交通预测挑战\Raw_data\gy_contest_link_traveltime_training_data.txt','r') as f3:
        for line in f3:
            if flag:
                link_traveltime.append(list(map(str,line.split(';')))) # str
            flag = 1
#    link_traveltime_link_ID = []
#    link_traveltime_date = []
#    link_traveltime_time_interval = []
#    link_traveltime_travel_time = []
#    for line in link_traveltime:
#        link_traveltime_link_ID.append(line[0])
#        link_traveltime_date.append(line[1])
#        link_traveltime_time_interval.append(line[2])
#        link_traveltime_travel_time.append(line[3][0:-1])
#    unique_date = list(set(link_traveltime_date))
    
    # get data from 3月，4月，5月份早上6点至9点的数据;6月份早上6点至8点的数据
    trainingData_6months = []
    trainingData_345months = []
    for line in range(len(link_traveltime)):
        if (link_traveltime[line][1][6] is '6'):
            trainingData_6months.append(link_traveltime[line])
#            trainingData_6months[-1][-1]=trainingData_6months[-1][-1][0:-1]# 去掉"\n"
        if (link_traveltime[line][2][12:14] == '06') and (link_traveltime[line][1][6] is not '6'):
            trainingData_345months.append(link_traveltime[line])
#            trainingData_345months[-1][-1]=trainingData_345months[-1][-1][0:-1]
        if (link_traveltime[line][2][12:14] == '07') and (link_traveltime[line][1][6] is not '6'):
            trainingData_345months.append(link_traveltime[line])
#            trainingData_345months[-1][-1]=trainingData_345months[-1][-1][0:-1]
        if (link_traveltime[line][2][12:14] == '08') and (link_traveltime[line][1][6] is not '6'):
            trainingData_345months.append(link_traveltime[line])
#            trainingData_345months[-1][-1]=trainingData_345months[-1][-1][0:-1]
        
#    np.save(r'E:\智慧交通预测挑战\trainingData_3456months\trainingData_345months',trainingData_345months)
#    np.save(r'E:\智慧交通预测挑战\trainingData_3456months\trainingData_6months',trainingData_6months)

# 合并道路信息，上下游信息，旅行时间
# 先生成link_info（列表类型）
if 0:
    link_info = list()
    flag = 0
    with open('E:\智慧交通预测挑战\Raw_data\gy_contest_link_info.txt','r') as f1:
        for line in f1:
            if flag:
                link_info.append(list(map(int,line.split(';')))) # int/float
            flag = 1
    
    trainingData_6months=np.load(r'E:\智慧交通预测挑战\trainingData_3456months\trainingData_6months.npy')
    trainingData_345months=np.load(r'E:\智慧交通预测挑战\trainingData_3456months\trainingData_345months.npy')
    link_ID = list(np.load(r'E:\智慧交通预测挑战\Code_ReadData\link_ID.npy'))
    
    trainingData_345monthsM = list()
    trainingData_6monthsM = list()
    
    # 6 月
    for i in range(199496):
        idx = link_ID.index(trainingData_6months[i][0])
        trainingData_6monthsM.append(list(trainingData_6months[i])+link_info[idx][1::])
    # 3,4,5月
    for i in range(910797):
        idx = link_ID.index(trainingData_345months[i][0])
        trainingData_345monthsM.append(list(trainingData_345months[i])+link_info[idx][1::])
    
    months6 = list() #  /
    months345 = list() #  /
    for i in range(199496): #  /
        months6.append(trainingData_6monthsM[i][0]+trainingData_6monthsM[i][1]+trainingData_6monthsM[i][2]) #  /
    for i in range(910797): #  /
        months345.append(trainingData_345monthsM[i][0]+trainingData_345monthsM[i][1]+trainingData_345monthsM[i][2]) #  /
                        
    link_top_in_links = np.load('E:\智慧交通预测挑战\Code_ReadData\link_top_in_links.npy')
    link_top_link_ID = np.load('E:\智慧交通预测挑战\Code_ReadData\link_top_link_ID.npy')
    link_top_out_links = np.load('E:\智慧交通预测挑战\Code_ReadData\link_top_out_links.npy')
    link_top_link_ID = list(link_top_link_ID)
    countt = 0
    trainingData_345monthsMT = list()
    trainingData_6monthsMT = list()
    # 6月份
    for i in range(199496):
        print(i)
        length = 0
        wedth = 0
        
        time = 0 # /
        speed = 0 # /
        
        link_top_info = list()
        idx = link_top_link_ID.index(trainingData_6monthsM[i][0])
        # 上游
        if len(link_top_in_links[idx]) == 0:
            link_top_info.append(trainingData_6monthsM[i][4]/float(trainingData_6monthsM[i][3])) # 该link的速度 
            link_top_info.append(0) #该link没有上游
            link_top_info.append(0) #该link的上游数量为0
            link_top_info.append(0) #该link的各个上游的长度之和
            link_top_info.append(0) #该link的各个上游的宽度之和
            
            link_top_info.append(0) #该link上游路段的平均旅行时间为0 /
            link_top_info.append(0) #该link上游路段的平均速度为0 /
            
        else:
            link_top_info.append(trainingData_6monthsM[i][4]/float(trainingData_6monthsM[i][3])) # 该link的速度
            link_top_info.append(1) #该link有上游
            link_top_info.append(link_top_in_links[idx].count('#')+1) #该link的上游数量  
            for j in range(link_top_in_links[idx].count('#')+1):
                idex1=link_ID.index(link_top_in_links[idx][j*19+j+0:j*19+j+19])
                length = length + link_info[idex1][1]
                wedth = wedth + link_info[idex1][2]
                
                if (link_top_in_links[idx][j*19+j+0:j*19+j+19]+trainingData_6monthsM[i][1]+trainingData_6monthsM[i][2]) not in months6:
                    countt = countt+1
                    linkid = trainingData_6monthsM[i][0]
                else:
                    linkid = link_top_in_links[idx][j*19+j+0:j*19+j+19]
                        
                ix = months6.index(linkid+trainingData_6monthsM[i][1]+trainingData_6monthsM[i][2]) # /
                time = time + float(trainingData_6monthsM[ix][3]) # /
                speed = speed + trainingData_6monthsM[ix][4]/float(trainingData_6monthsM[ix][3]) # /
                
            link_top_info.append(length) #该link的各个上游的长度之和
            link_top_info.append(wedth) #该link的各个上游的宽度之和
            
            link_top_info.append(time/(link_top_in_links[idx].count('#')+1)) # 该link上游路段的平均旅行时间 /
            link_top_info.append(speed/(link_top_in_links[idx].count('#')+1)) # 该link上游路段的平均速度 /
        
         # 下游
        length = 0
        wedth = 0
        
        time = 0 # /
        speed = 0 # /
        
        if len(link_top_out_links[idx]) == 0:
            link_top_info.append(0) #该link没有下游
            link_top_info.append(0) #该link的下游数量为0
            link_top_info.append(0) #该link的各个下游的长度之和
            link_top_info.append(0) #该link的各个下游的宽度之和
            
            link_top_info.append(0) #该link下游路段的平均旅行时间为0 /
            link_top_info.append(0) #该link下游路段的平均速度为0 /    
                                
        else:
            link_top_info.append(1) #该link有下游
            link_top_info.append(link_top_out_links[idx].count('#')+1) #该link的下游数量  
            for j in range(link_top_out_links[idx].count('#')+1):
                idex1=link_ID.index(link_top_out_links[idx][j*19+j+0:j*19+j+19])
                length = length + link_info[idex1][1]
                wedth = wedth + link_info[idex1][2]
                
                if (link_top_out_links[idx][j*19+j+0:j*19+j+19]+trainingData_6monthsM[i][1]+trainingData_6monthsM[i][2]) not in months6:
                    countt = countt+1
                    linkid = trainingData_6monthsM[i][0]
                else:
                    linkid = link_top_out_links[idx][j*19+j+0:j*19+j+19]
                
                ix = months6.index(linkid+trainingData_6monthsM[i][1]+trainingData_6monthsM[i][2]) # /
                time = time + float(trainingData_6monthsM[ix][3]) # /
                speed = speed + trainingData_6monthsM[ix][4]/float(trainingData_6monthsM[ix][3]) # /
                                   
            link_top_info.append(length) #该link的各个下游的长度之和
            link_top_info.append(wedth) #该link的各个下游的宽度之和
            
            link_top_info.append(time/(link_top_out_links[idx].count('#')+1)) # 该link下游路段的平均旅行时间 /
            link_top_info.append(speed/(link_top_out_links[idx].count('#')+1)) # 该link下游路段的平均速度 /
                                
        trainingData_6monthsMT.append(trainingData_6monthsM[i]+link_top_info) # 合并
    
    
    # 3,4,5月份
    for i in range(910797):
        print(i)
        length = 0
        wedth = 0
        
        time = 0 # /
        speed = 0 # /
        
        link_top_info = list()
        idx = link_top_link_ID.index(trainingData_345monthsM[i][0])
        # 上游
        if len(link_top_in_links[idx]) == 0:
            link_top_info.append(trainingData_345monthsM[i][4]/float(trainingData_345monthsM[i][3])) # 该link的速度 
            link_top_info.append(0) #该link没有上游
            link_top_info.append(0) #该link的上游数量为0
            link_top_info.append(0) #该link的各个上游的长度之和
            link_top_info.append(0) #该link的各个上游的宽度之和
            
            link_top_info.append(0) #该link上游路段的平均旅行时间为0 /
            link_top_info.append(0) #该link上游路段的平均速度为0 /
                                
        else:
            link_top_info.append(trainingData_345monthsM[i][4]/float(trainingData_345monthsM[i][3])) # 该link的速度
            link_top_info.append(1) #该link有上游
            link_top_info.append(link_top_in_links[idx].count('#')+1) #该link的上游数量  
            for j in range(link_top_in_links[idx].count('#')+1):
                idex1=link_ID.index(link_top_in_links[idx][j*19+j+0:j*19+j+19])
                length = length + link_info[idex1][1]
                wedth = wedth + link_info[idex1][2]
                
                if (link_top_in_links[idx][j*19+j+0:j*19+j+19]+trainingData_345monthsM[i][1]+trainingData_345monthsM[i][2]) not in months345:
                    countt = countt+1
                    linkid = trainingData_345monthsM[i][0]
                else:
                    linkid = link_top_in_links[idx][j*19+j+0:j*19+j+19]
                
                ix = months345.index(linkid+trainingData_345monthsM[i][1]+trainingData_345monthsM[i][2]) # /
                time = time + float(trainingData_345monthsM[ix][3]) # /
                speed = speed + trainingData_345monthsM[ix][4]/float(trainingData_345monthsM[ix][3]) # /
                
                
            link_top_info.append(length) #该link的各个上游的长度之和
            link_top_info.append(wedth) #该link的各个上游的宽度之和
            
            link_top_info.append(time/(link_top_in_links[idx].count('#')+1)) # 该link上游路段的平均旅行时间 /
            link_top_info.append(speed/(link_top_in_links[idx].count('#')+1)) # 该link上游路段的平均速度 /
        
         # 下游
        length = 0
        wedth = 0
        
        time = 0 # /
        speed = 0 # /
        
        if len(link_top_out_links[idx]) == 0:
            link_top_info.append(0) #该link没有下游
            link_top_info.append(0) #该link的下游数量为0
            link_top_info.append(0) #该link的各个下游的长度之和
            link_top_info.append(0) #该link的各个下游的宽度之和
            
            link_top_info.append(0) #该link下游路段的平均旅行时间为0 /
            link_top_info.append(0) #该link下游路段的平均速度为0 /                      
                                
        else:
            link_top_info.append(1) #该link有下游
            link_top_info.append(link_top_out_links[idx].count('#')+1) #该link的下游数量  
            for j in range(link_top_out_links[idx].count('#')+1):
                idex1=link_ID.index(link_top_out_links[idx][j*19+j+0:j*19+j+19])
                length = length + link_info[idex1][1]
                wedth = wedth + link_info[idex1][2]
                
                if (link_top_out_links[idx][j*19+j+0:j*19+j+19]+trainingData_345monthsM[i][1]+trainingData_345monthsM[i][2]) not in months345:
                    countt = countt+1
                    linkid = trainingData_345monthsM[i][0]
                else:
                    linkid = link_top_out_links[idx][j*19+j+0:j*19+j+19]
                    
                ix = months345.index(linkid+trainingData_345monthsM[i][1]+trainingData_345monthsM[i][2]) # /
                time = time + float(trainingData_345monthsM[ix][3]) # /
                speed = speed + trainingData_345monthsM[ix][4]/float(trainingData_345monthsM[ix][3]) # /
                           
                
            link_top_info.append(length) #该link的各个下游的长度之和
            link_top_info.append(wedth) #该link的各个下游的宽度之和
            
            link_top_info.append(time/(link_top_out_links[idx].count('#')+1)) # 该link下游路段的平均旅行时间 /
            link_top_info.append(speed/(link_top_out_links[idx].count('#')+1)) # 该link下游路段的平均速度 /                   
                                
        trainingData_345monthsMT.append(trainingData_345monthsM[i]+link_top_info) # 合并
        
        
    np.save(r'E:\智慧交通预测挑战\traininData_3456_20features\trainingData_6monthsMT',trainingData_6monthsMT)
    np.save(r'E:\智慧交通预测挑战\traininData_3456_20features\trainingData_345monthsMT',trainingData_345monthsMT)


# 生成其他特征

if 0:
    trainingData_6monthsMT = np.load(r'E:\智慧交通预测挑战\traininData_3456_20features\trainingData_6monthsMT.npy')
    trainingData_345monthsMT = np.load(r'E:\智慧交通预测挑战\traininData_3456_20features\trainingData_345monthsMT.npy')
    trainingData_6monthsMTallFeatures = []
    trainingData_345monthsMTallFeatures = []
    
    # 3,4,5月份
    for i in range(len(trainingData_345monthsMT)):
        temp_featrues = []
        # 本路段宽度 减去 该路段上游路段的宽度之和
        temp_featrues.append(float(trainingData_345monthsMT[i][5])-float(trainingData_345monthsMT[i][11]))
        # 下游路段的宽度之和 减去 本路段路宽
        temp_featrues.append(float(trainingData_345monthsMT[i][17])-float(trainingData_345monthsMT[i][5]))
        # 下游路段的平均速度 减去 上游路段的平均速度
        temp_featrues.append(float(trainingData_345monthsMT[i][19])-float(trainingData_345monthsMT[i][13]))
        # 下游的宽度之和 减去 上游的宽度之和
        temp_featrues.append(float(trainingData_345monthsMT[i][17])-float(trainingData_345monthsMT[i][11]))
        # 上游路段的平均旅行时间 减去 下游路段的平均旅行时间
        temp_featrues.append(float(trainingData_345monthsMT[i][12])-float(trainingData_345monthsMT[i][18]))
        # 本路段宽度 + 上游的宽度之和 + 下游的宽度之和
        temp_featrues.append(float(trainingData_345monthsMT[i][5])+float(trainingData_345monthsMT[i][11])+float(trainingData_345monthsMT[i][17]))
        # 本路段长度 + 上游的长度之和 + 下游的长度之和
        temp_featrues.append(float(trainingData_345monthsMT[i][4])+float(trainingData_345monthsMT[i][10])+float(trainingData_345monthsMT[i][16]))
        trainingData_345monthsMTallFeatures.append(list(trainingData_345monthsMT[i])+temp_featrues)
    del trainingData_345monthsMT
    
    # 6月份
    for i in range(len(trainingData_6monthsMT)):
        temp_featrues = []
        # 本路段宽度 减去 该路段上游路段的宽度之和
        temp_featrues.append(float(trainingData_6monthsMT[i][5])-float(trainingData_6monthsMT[i][11]))
        # 下游路段的宽度之和 减去 本路段路宽
        temp_featrues.append(float(trainingData_6monthsMT[i][17])-float(trainingData_6monthsMT[i][5]))
        # 下游路段的平均速度 减去 上游路段的平均速度
        temp_featrues.append(float(trainingData_6monthsMT[i][19])-float(trainingData_6monthsMT[i][13]))
        # 下游的宽度之和 减去 上游的宽度之和
        temp_featrues.append(float(trainingData_6monthsMT[i][17])-float(trainingData_6monthsMT[i][11]))
        # 上游路段的平均旅行时间 减去 下游路段的平均旅行时间
        temp_featrues.append(float(trainingData_6monthsMT[i][12])-float(trainingData_6monthsMT[i][18]))
        # 本路段宽度 + 上游的宽度之和 + 下游的宽度之和
        temp_featrues.append(float(trainingData_6monthsMT[i][5])+float(trainingData_6monthsMT[i][11])+float(trainingData_6monthsMT[i][17]))
        # 本路段长度 + 上游的长度之和 + 下游的长度之和
        temp_featrues.append(float(trainingData_6monthsMT[i][4])+float(trainingData_6monthsMT[i][10])+float(trainingData_6monthsMT[i][16])) 
        trainingData_6monthsMTallFeatures.append(list(trainingData_6monthsMT[i])+temp_featrues)
    del trainingData_6monthsMT
    
    np.save(r'E:\智慧交通预测挑战\traininData_3456_27features\trainingData_6monthsMTallFeatures',trainingData_6monthsMTallFeatures)
    np.save(r'E:\智慧交通预测挑战\traininData_3456_27features\trainingData_345monthsMTallFeatures',trainingData_345monthsMTallFeatures)
    
# 生成 one hot code
if 0:
    j = 0
    OneHotCode = np.zeros([30,30])
    for i in range(30):
        OneHotCode[i][j] = 1
        j = j + 1
    np.save(r'E:\智慧交通预测挑战\lastTrainingData\time',time)
    np.save(r'E:\智慧交通预测挑战\lastTrainingData\OneHotCode',OneHotCode)
    
# 对时间片段进行编码（one hot encode）
if 0:
    time = list(np.load(r'E:\智慧交通预测挑战\lastTrainingData\time.npy'))
    OneHotCode = np.load(r'E:\智慧交通预测挑战\lastTrainingData\OneHotCode.npy')
    
    # 6月
    if 0:
        features6 = []
        trainingData_6monthsMTallFeatures = np.load(r'E:\智慧交通预测挑战\traininData_3456_27features\trainingData_6monthsMTallFeatures.npy')
        for i in range(len(trainingData_6monthsMTallFeatures)):
            idx=time.index(trainingData_6monthsMTallFeatures[i][2][15:17])
            features6.append(list(trainingData_6monthsMTallFeatures[i][0:6])+list(trainingData_6monthsMTallFeatures[i][7::])+list(OneHotCode[idx]))
        del trainingData_6monthsMTallFeatures
        np.save(r'E:\智慧交通预测挑战\lastTrainingData\features6',features6)
    # 3,4,5月
    if 0:
        features345 = []
        trainingData_345monthsMTallFeatures = np.load(r'E:\智慧交通预测挑战\traininData_3456_27features\trainingData_345monthsMTallFeatures.npy')
        for i in range(len(trainingData_345monthsMTallFeatures)):
            idx=time.index(trainingData_345monthsMTallFeatures[i][2][15:17])
            features345.append(list(trainingData_345monthsMTallFeatures[i][0:6])+list(trainingData_345monthsMTallFeatures[i][7::])+list(OneHotCode[idx]))
        del trainingData_345monthsMTallFeatures
        np.save(r'E:\智慧交通预测挑战\lastTrainingData\features345',features345)
    
    # 把3,4,5月份的数据分开（已经生成了features345）
    if 0:
        features3=[]
        features4=[]
        features5=[]
        for i in range(len(features345)):
            if (features345[i][1][6] == '3'): # 3月
                features3.append(features345[i]) 
            if (features345[i][1][6] == '4'): # 4月
                features4.append(features345[i])
            if (features345[i][1][6] == '5'): # 5月
                features5.append(features345[i])
        np.save(r'E:\智慧交通预测挑战\lastTrainingData\features3',features3)
        np.save(r'E:\智慧交通预测挑战\lastTrainingData\features4',features4)
        np.save(r'E:\智慧交通预测挑战\lastTrainingData\features5',features5)
  
#　＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠＠
# 排序：对每一个样本按时间顺序排序
    
# 对3月份的数据排序
if 1:
#    features3 = np.load(r'E:\智慧交通预测挑战\lastTrainingData\features3.npy')
    time = list(np.load(r'E:\智慧交通预测挑战\lastTrainingData\其他\time.npy'))
    iddatetime = []
    sample3 = []
    countt = 0
    for i in range(len(features3)):
        iddatetime.append(features3[i][0]+features3[i][1]+features3[i][2])
    for i in range(len(features3)): 
        print(i,'...')
        str1 = features3[i][0]+features3[i][1]+features3[i][2]
        if (time.index(str1[44:46]) == 28):
            x1 = time.index(str1[44:46])+1 #(或x1 = 29)
            x2 = 0
        elif (time.index(str1[44:46]) == 29):
            x1 = 0
            x2 = 1
        else:
            x1 = time.index(str1[44:46])+1
            x2 = time.index(str1[44:46])+2
        strTmp1 =time[x1]
        strTmp2 =time[x2]
        
        if x1 == 0:
            str2 = str1[0:42]+str(int(str1[42])+1)+str1[43]+strTmp1+str1[46:64]+strTmp2+str1[66::]
        else:
            str2 = str1[0:44]+strTmp1+str1[46:64]+strTmp2+str1[66::] # 当前下一个样本的时间点的id,时间及日期信息
        if x2 == 0:
            str2 = str1[0:44]+strTmp1+str1[46:62]+str(int(str1[62])+1)+str1[63]+strTmp2+str1[66::]
        
        if str2 not in  iddatetime:
            countt = countt + 1
            label = float(features3[i][3])
        else:
            idx = iddatetime.index(str2)
            label = features3[idx][3] # 当前时间片段的下一个时间片段的旅行时间，被作为当前时间片段的样本的label
        sample3.append(list(features3[i])+ [label])
#    np.save(r'E:\智慧交通预测挑战\Samples\sample3',sample3)


# 对4月份的数据排序

if 0:
    features4 = np.load(r'E:\智慧交通预测挑战\lastTrainingData\features4.npy')
    time = list(np.load(r'E:\智慧交通预测挑战\lastTrainingData\其他\time.npy'))
    iddatetime = []
    sample4 = []
    countt = 0
    for i in range(len(features4)):
        iddatetime.append(features4[i][0]+features4[i][1]+features4[i][2])
    for i in range(len(features4)): 
        print(i,'...')
        str1 = features4[i][0]+features4[i][1]+features4[i][2]
        if (time.index(str1[44:46]) == 28):
            x1 = time.index(str1[44:46])+1 #(或x1 = 29)
            x2 = 0
        elif (time.index(str1[44:46]) == 29):
            x1 = 0
            x2 = 1
        else:
            x1 = time.index(str1[44:46])+1
            x2 = time.index(str1[44:46])+2
        strTmp1 =time[x1]
        strTmp2 =time[x2]
        
        if x1 == 0:
            str2 = str1[0:42]+str(int(str1[42])+1)+str1[43]+strTmp1+str1[46:64]+strTmp2+str1[66::]
        else:
            str2 = str1[0:44]+strTmp1+str1[46:64]+strTmp2+str1[66::] # 当前下一个样本的时间点的id,时间及日期信息
        if x2 == 0:
            str2 = str1[0:44]+strTmp1+str1[46:62]+str(int(str1[62])+1)+str1[63]+strTmp2+str1[66::]
        
        if str2 not in  iddatetime:
            countt = countt + 1
            label = float(features4[i][3])
        else:
            idx = iddatetime.index(str2)
            label = features4[idx][3] # 当前时间片段的下一个时间片段的旅行时间，被作为当前时间片段的样本的label
        sample4.append(list(features4[i])+ [label])
    np.save(r'E:\智慧交通预测挑战\Samples\sample4',sample4)


# 对5月份的数据排序

if 0:
    features5 = np.load(r'E:\智慧交通预测挑战\lastTrainingData\features5.npy')
    time = list(np.load(r'E:\智慧交通预测挑战\lastTrainingData\其他\time.npy'))
    iddatetime = []
    sample5 = []
    countt = 0
    for i in range(len(features5)):
        iddatetime.append(features5[i][0]+features5[i][1]+features5[i][2])
    for i in range(len(features5)): 
        print(i,'...')
        str1 = features5[i][0]+features5[i][1]+features5[i][2]
        if (time.index(str1[44:46]) == 28):
            x1 = time.index(str1[44:46])+1 #(或x1 = 29)
            x2 = 0
        elif (time.index(str1[44:46]) == 29):
            x1 = 0
            x2 = 1
        else:
            x1 = time.index(str1[44:46])+1
            x2 = time.index(str1[44:46])+2
        strTmp1 =time[x1]
        strTmp2 =time[x2]
        
        if x1 == 0:
            str2 = str1[0:42]+str(int(str1[42])+1)+str1[43]+strTmp1+str1[46:64]+strTmp2+str1[66::]
        else:
            str2 = str1[0:44]+strTmp1+str1[46:64]+strTmp2+str1[66::] # 当前下一个样本的时间点的id,时间及日期信息
        if x2 == 0:
            str2 = str1[0:44]+strTmp1+str1[46:62]+str(int(str1[62])+1)+str1[63]+strTmp2+str1[66::]
        
        if str2 not in  iddatetime:
            countt = countt + 1
            label = float(features5[i][3])
        else:
            idx = iddatetime.index(str2)
            label = features5[idx][3] # 当前时间片段的下一个时间片段的旅行时间，被作为当前时间片段的样本的label
        sample5.append(list(features5[i])+ [label])
    np.save(r'E:\智慧交通预测挑战\Samples\sample5',sample5)


# 对6月份的数据排序

if 0:
    features6 = np.load(r'E:\智慧交通预测挑战\lastTrainingData\features6.npy')
    time = list(np.load(r'E:\智慧交通预测挑战\lastTrainingData\其他\time.npy'))
    iddatetime = []
    sample6 = []
    countt = 0
    for i in range(len(features6)):
        iddatetime.append(features6[i][0]+features6[i][1]+features6[i][2])
    for i in range(len(features6)): 
        print(i,'...')
        str1 = features6[i][0]+features6[i][1]+features6[i][2]
        if (time.index(str1[44:46]) == 28):
            x1 = time.index(str1[44:46])+1 #(或x1 = 29)
            x2 = 0
        elif (time.index(str1[44:46]) == 29):
            x1 = 0
            x2 = 1
        else:
            x1 = time.index(str1[44:46])+1
            x2 = time.index(str1[44:46])+2
        strTmp1 =time[x1]
        strTmp2 =time[x2]
        
        if x1 == 0:
            str2 = str1[0:42]+str(int(str1[42])+1)+str1[43]+strTmp1+str1[46:64]+strTmp2+str1[66::]
        else:
            str2 = str1[0:44]+strTmp1+str1[46:64]+strTmp2+str1[66::] # 当前下一个样本的时间点的id,时间及日期信息
        if x2 == 0:
            str2 = str1[0:44]+strTmp1+str1[46:62]+str(int(str1[62])+1)+str1[63]+strTmp2+str1[66::]
        
        if str2 not in  iddatetime:
            countt = countt + 1
            label = float(features6[i][3])
        else:
            idx = iddatetime.index(str2)
            label = features6[idx][3] # 当前时间片段的下一个时间片段的旅行时间，被作为当前时间片段的样本的label
        sample6.append(list(features6[i])+ [label])
    np.save(r'E:\智慧交通预测挑战\Samples\sample6',sample6)

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# ***************************************************************************************************
# 将字符型转为数值型
# 6 月
if 0:
   sample6 = np.load(r'E:\智慧交通预测挑战\Samples\sample6.npy')
   sample_6 = []
   for i in range(len(sample6)):
       print(i)
       feature = []
       for j in range(54):
           feature.append(float(sample6[i][j+3]))
       sample_6.append(list(sample6[i][0:3])+feature)
   np.save(r'E:\智慧交通预测挑战\Samples\sample_6',sample_6)

# 5 月
if 0:
   sample5 = np.load(r'E:\智慧交通预测挑战\Samples\sample5.npy')
   sample_5= []
   for i in range(len(sample5)):
       print(i)
       feature = []
       for j in range(54):
           feature.append(float(sample5[i][j+3]))
       sample_5.append(list(sample5[i][0:3])+feature)
   np.save(r'E:\智慧交通预测挑战\Samples\sample_5',sample_5)


# 4 月
if 0:
   sample4 = np.load(r'E:\智慧交通预测挑战\Samples\sample4.npy')
   sample_4 = []
   for i in range(len(sample4)):
       print(i)
       feature = []
       for j in range(54):
           feature.append(float(sample4[i][j+3]))
       sample_4.append(list(sample4[i][0:3])+feature)
   np.save(r'E:\智慧交通预测挑战\Samples\sample_4',sample_4)


# 3 月
if 0:
   sample3 = np.load(r'E:\智慧交通预测挑战\Samples\sample3.npy')
   sample_3 = []
   for i in range(len(sample3)):
       print(i)
       feature = []
       for j in range(54):
           feature.append(float(sample3[i][j+3]))
       sample_3.append(list(sample3[i][0:3])+feature)
   np.save(r'E:\智慧交通预测挑战\Samples\sample_3',sample_3)


# ***************************************************************************************************


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# 把工作日，非工作日以及节假日的数据分开

# 3月

if 0:
    sample_3 = np.load(r'E:\智慧交通预测挑战\Samples\sample_3.npy')
    festival = np.load(r'E:\智慧交通预测挑战\Samples\周末及假日\festival.npy')
    weekend = np.load(r'E:\智慧交通预测挑战\Samples\周末及假日\weekend.npy')
    workingData3 = []
    weekendDdata3 = []
    for i in range(len(sample_3)):
        temp = []
        if (sample_3[i][1] not in festival) and  (sample_3[i][1] not in weekend):
            for j in range(54):
                temp.append(float(sample_3[i][j+3]))
            workingData3.append(temp)  # 周一至周五数据
        if (sample_3[i][1] in weekend) and (sample_3[i][1] != '2016-06-12'):
            for j in range(54):
                temp.append(float(sample_3[i][j+3]))
            weekendDdata3.append(temp) # 周六周数据
        print(i,'......')
    workingData3 = np.array(workingData3)
    weekendDdata3 = np.array(weekendDdata3)
    np.save(r'E:\智慧交通预测挑战\OnlyFeatureData\workingData3',workingData3)
    np.save(r'E:\智慧交通预测挑战\OnlyFeatureData\weekendDdata3',weekendDdata3)
    sio.savemat(r'E:\智慧交通预测挑战\OnlyFeatureData\months3',{'workingData3':workingData3,'weekendDdata3':weekendDdata3})

# 4月
if 0:
    sample_4 = np.load(r'E:\智慧交通预测挑战\Samples\sample_4.npy')
    festival = np.load(r'E:\智慧交通预测挑战\Samples\周末及假日\festival.npy')
    weekend = np.load(r'E:\智慧交通预测挑战\Samples\周末及假日\weekend.npy')
    workingData4 = []
    weekendDdata4 = []
    for i in range(len(sample_4)):
        temp = []
        if (sample_4[i][1] not in festival) and  (sample_4[i][1] not in weekend):
            for j in range(54):
                temp.append(float(sample_4[i][j+3]))
            workingData4.append(temp)  # 周一至周五数据
        if (sample_4[i][1] in weekend) and (sample_4[i][1] != '2016-06-12'):
            for j in range(54):
                temp.append(float(sample_4[i][j+3]))
            weekendDdata4.append(temp) # 周六周数据
        print(i,'......')
    workingData4 = np.array(workingData4)
    weekendDdata4 = np.array(weekendDdata4)
    np.save(r'E:\智慧交通预测挑战\OnlyFeatureData\workingData4',workingData4)
    np.save(r'E:\智慧交通预测挑战\OnlyFeatureData\weekendDdata4',weekendDdata4)
    sio.savemat(r'E:\智慧交通预测挑战\OnlyFeatureData\months4',{'workingData4':workingData4,'weekendDdata4':weekendDdata4})

# 5月
if 0:
    sample_5 = np.load(r'E:\智慧交通预测挑战\Samples\sample_5.npy')
    festival = np.load(r'E:\智慧交通预测挑战\Samples\周末及假日\festival.npy')
    weekend = np.load(r'E:\智慧交通预测挑战\Samples\周末及假日\weekend.npy')
    workingData5 = []
    weekendDdata5 = []
    for i in range(len(sample_5)):
        temp = []
        if (sample_5[i][1] not in festival) and  (sample_5[i][1] not in weekend):
            for j in range(54):
                temp.append(float(sample_5[i][j+3]))
            workingData5.append(temp)  # 周一至周五数据
        if (sample_5[i][1] in weekend) and (sample_5[i][1] != '2016-06-12'):
            for j in range(54):
                temp.append(float(sample_5[i][j+3]))
            weekendDdata5.append(temp) # 周六周数据
        print(i,'......')
    workingData5 = np.array(workingData5)
    weekendDdata5 = np.array(weekendDdata5)
    np.save(r'E:\智慧交通预测挑战\OnlyFeatureData\workingData5',workingData5)
    np.save(r'E:\智慧交通预测挑战\OnlyFeatureData\weekendDdata5',weekendDdata5)
    sio.savemat(r'E:\智慧交通预测挑战\OnlyFeatureData\months5',{'workingData5':workingData5,'weekendDdata5':weekendDdata5})

# 6月
if 0:
    sample_6 = np.load(r'E:\智慧交通预测挑战\Samples\sample_6.npy')
    festival = np.load(r'E:\智慧交通预测挑战\Samples\周末及假日\festival.npy')
    weekend = np.load(r'E:\智慧交通预测挑战\Samples\周末及假日\weekend.npy')
    workingData6 = []
    weekendDdata6 = []
    for i in range(len(sample_6)):
        temp = []
        if (sample_6[i][1] not in festival) and  (sample_6[i][1] not in weekend):
            for j in range(54):
                temp.append(float(sample_6[i][j+3]))
            workingData6.append(temp)  # 周一至周五数据
        if (sample_6[i][1] in weekend) and (sample_6[i][1] != '2016-06-12'):
            for j in range(54):
                temp.append(float(sample_6[i][j+3]))
            weekendDdata6.append(temp) # 周六周数据
        print(i,'......')
    workingData6 = np.array(workingData6)
    weekendDdata6 = np.array(weekendDdata6)
    np.save(r'E:\智慧交通预测挑战\OnlyFeatureData\workingData6',workingData6)
    np.save(r'E:\智慧交通预测挑战\OnlyFeatureData\weekendDdata6',weekendDdata6)
    sio.savemat(r'E:\智慧交通预测挑战\OnlyFeatureData\months6',{'workingData6':workingData6,'weekendDdata6':weekendDdata6})
    
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# 合并3,4,5月份的数据并随机打乱

if 0:
    weekendDdata3 = np.load(r'E:\智慧交通预测挑战\OnlyFeatureData\weekendDdata3.npy')
    weekendDdata4 = np.load(r'E:\智慧交通预测挑战\OnlyFeatureData\weekendDdata4.npy')
    weekendDdata5 = np.load(r'E:\智慧交通预测挑战\OnlyFeatureData\weekendDdata5.npy')
    weekendDdata6 = np.load(r'E:\智慧交通预测挑战\OnlyFeatureData\weekendDdata6.npy')
    workingData3 = np.load(r'E:\智慧交通预测挑战\OnlyFeatureData\workingData3.npy')
    workingData4 = np.load(r'E:\智慧交通预测挑战\OnlyFeatureData\workingData4.npy')
    workingData5 = np.load(r'E:\智慧交通预测挑战\OnlyFeatureData\workingData5.npy')
    workingData6 = np.load(r'E:\智慧交通预测挑战\OnlyFeatureData\workingData6.npy')
    
    weekendDdata345 = np.concatenate((weekendDdata3,weekendDdata4,weekendDdata5),axis = 0)
    workingData345 = np.concatenate((workingData3,workingData4,workingData5),axis = 0)
    
    RweekendDdata345 = []
    RworkingData345 = []
    RweekendDdata6 = []
    RworkingData6 = []
    
    x1=list(range(len(weekendDdata345)))
    random.shuffle(x1)
    for i in x1:
        RweekendDdata345.append(weekendDdata345[i])
        
    x2 = list(range(len(workingData345)))
    random.shuffle(x2)
    for i in x2:
        RworkingData345.append(workingData345[i])
    
    x3 = list(range(len(weekendDdata6)))
    random.shuffle(x3)
    for i in x3:
        RweekendDdata6.append(weekendDdata6[i])
    
    x4 = list(range(len(workingData6)))
    random.shuffle(x4)
    for i in x4:
        RworkingData6.append(workingData6[i])
        
    
    RweekendDdata345 = np.array(RweekendDdata345)
    RworkingData345 = np.array(RworkingData345)
    RweekendDdata6 = np.array(RweekendDdata6)
    RworkingData6 = np.array(RworkingData6)
    
    np.save(r'E:\智慧交通预测挑战\Model\data\RweekendDdata345',RweekendDdata345)
    np.save(r'E:\智慧交通预测挑战\Model\data\RworkingData345',RworkingData345)
    np.save(r'E:\智慧交通预测挑战\Model\data\RweekendDdata6',RweekendDdata6)
    np.save(r'E:\智慧交通预测挑战\Model\data\RworkingData6',RworkingData6)



#Feature = []
#for i in range(len(feature)):
#    temp = []
#    for j in range(54):
#        temp.append(float(feature[i][j]))
#    Feature.append(temp)
#
#

date345=[]
label345 = []
for i in range(len(trainingData_345months)):
    date345.append(trainingData_345months[i][0]+trainingData_345months[i][1]+trainingData_345months[i][2])
    label345.append(trainingData_345months[i][4])




