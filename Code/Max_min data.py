'''
Created on 2019年07月02日

@author: leibo Liu
'''

import numpy as np
import pandas as pd
from sklearn import metrics
import threading
def get_num(y,start,num):
    if y < i :
        n ="n"+str(y)
        for n in np.arange(start,1.00-sum(num),0.25):
            if sum(num)+n < 1.00:
                num.append(round(n,3))
                get_num1(y+1,0.05,num)
                num.pop()
def get_num1(y,start,num):
    global pr_auc
    global predictor
    global pr_num
    global DB
    global jiaoji_DR
    if y < i :
        n ="n"+str(y)
        for n in np.arange(start,1.00-sum(num),0.05):
            if sum(num)+n < 1.00:
                num.append(round(n,3))
                get_num1(y+1,0.05,num)
                num.pop()
    else:
        end_n = round(1.00-sum(num),3)
        if end_n >0.00:
            num.append(end_n) 
            plus_v= np.array([float(0)] * len(jiaoji_DR))
            for m in range(0,i+1):
                plus_v = plus_v + (float(num[m]) * np.array(v[m]["Scort"]))
            y_true = np.array(v[i].iloc[:,3])
            y_scores = np.array(plus_v)
            
            precision, recall, thresholds = metrics.precision_recall_curve(y_true, y_scores)
            area = metrics.auc(recall, precision)
            if area>pr_auc:
                lock.acquire()
                pr_auc = area
                pr_num = num[:]
                DB = jiaoji_DR[:]
                predictor=predictors[j]
                lock.release()
            num.pop()

if __name__ == '__main__': 
    auprc = pd.read_csv("./AUPRC.txt",header = None,names=["Predictor","AUPRC"],sep="\t" )
    auprc = auprc.sort_values(by='AUPRC', axis=0, ascending=False)
    predictors = list(auprc["Predictor"])
    
    v=[0] * 10
    vs=[0] * 10
    predicted = []
    predictor = predictors[0]
    predicted.append(predictors[0])
    data = pd.read_table("./normalization_data/Max_Min data/"+predicted[0]+".txt",index_col=0)
    data.columns =["Disease","miRNA","Scort","y_ture","Feature_scort"]
    data = data.drop_duplicates(subset=["Disease","miRNA"])
    inte_v = data.iloc[:,0:2]
    
    for i in range(1,10):
        print(i)
        num = []
        pr_num =[]
        pr_auc = 0
        DB = []
        
        data = pd.read_table("./normalization_data/Max_Min data/"+predicted[i-1]+".txt",index_col=0)
        data.columns=["Disease","miRNA","Scort","y_ture","Feature_scort"]
        vs[i-1] = data.drop_duplicates(subset=["Disease","miRNA"])
        
        for j in range(1,len(predictors)):
            if predictors[j] not in predicted:
                data = pd.read_table("./normalization_data/Max_Min data/"+predictors[j]+".txt",index_col=0 )
                data.columns =["Disease","miRNA","Scort","y_ture","Feature_scort"] 
                data= data.drop_duplicates(subset=["Disease","miRNA"])
                
                vs[i] = pd.merge(data,inte_v,on=["Disease","miRNA"])
                
                jiaoji_DR = vs[i].iloc[:,0:2]
                
                if (len(inte_v)-len(vs[i]))/len(inte_v) <= 0.05:
                    for x in range(0,i+1):
                        v[x] = pd.merge(vs[x],jiaoji_DR,on=["Disease","miRNA"])
                        v[x] = v[x].sort_values(by=["Disease","miRNA"])
                    lock = threading.Lock()
                    thread_list = []
                    
                    T1=threading.Thread(target=get_num, args=(0,0.05,[],))
                    T2=threading.Thread(target=get_num, args=(0,0.1,[],))
                    T3=threading.Thread(target=get_num, args=(0,0.15,[],))
                    T4=threading.Thread(target=get_num, args=(0,0.2,[],))
                    T5=threading.Thread(target=get_num, args=(0,0.25,[],))
                    
                    T1.start()
                    T2.start()
                    T3.start()
                    T4.start()
                    T5.start()
                    
                    thread_list.append(T1)
                    thread_list.append(T2)
                    thread_list.append(T3)
                    thread_list.append(T4)
                    thread_list.append(T5)
                    
                    T1.join()
                    T2.join()
                    T3.join()
                    T4.join()
                    T5.join()
                    
        predicted.append(predictor)
        inte_v = DB
        print(predicted)
        print(pr_num)
        print(pr_auc)
        
        save_str =  str(i)+"\t"+str(predicted)+"\t"+str(pr_num)+"\t"+str(pr_auc)+"\n"
        with open("./Results/Max_Min_sunshi_data_result.txt","a+") as f:
            f.write(save_str)
            f.close()