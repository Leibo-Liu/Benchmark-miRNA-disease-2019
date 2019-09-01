# coding:utf-8
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
from sklearn import metrics
from sklearn.metrics import roc_curve,auc

PathList = []
file = open("AUROC.txt","w")
def fun(path):
    for fn in glob.glob(path + "\\*.txt"):
        PathList.append(fn)
fun(r"E:\\6 HMDD prediction evaluation\Misim 1.0_results\Yuanshi_jiaodui_yanzheng_causality3_results")


plt.rcParams['figure.dpi'] = 300
plt.figure(1)
font1 = {"family":"Arial",
         "weight":"book",
         "size": 9
         }
plt.title('ROC Curve',font1)
plt.xlabel('False Positive Rate',font1)
# plt.ylabel('True Positive Rate',font1)
# Names = ["L1-norm","TLHNMDA","CNMDA","RWBRMDA","HGIMDA","HLPMDA","HNMDA","MDHGI","IMCMDA","RFMDA"]
for path in PathList:
    FileName = os.path.basename(path).split("_")[0]
    data = pd.read_csv(path, header=None, delimiter="\t",names=["disease","miRNA","y_scores","y_true","causality"])
    data = data.drop_duplicates(subset=["disease", "miRNA", "y_scores"], keep="first")
    data = data.loc[data["causality"] != 2]
    y_true = np.array(data.iloc[:,4])
    y_true = np.where(y_true == 1,True,False)
    y_scores = np.array(data.iloc[:,2])
    area = 0
    fpr,tpr,threshold = roc_curve(y_true,y_scores)
    area = metrics.auc(fpr,tpr)
    auc = round(area, 3)
    file.write(FileName+"\t"+str(area)+"\n")
    plt.figure(1)
    plt.plot(fpr, tpr, label=name + "  AUROC=" + str(auc))
    plt.legend(prop=font1)
plt.savefig("ROC_curve.tiff",dpi = 300)
plt.show()
plt.close()
file.close()