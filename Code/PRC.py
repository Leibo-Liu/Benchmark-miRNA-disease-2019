# coding:utf-8
import matplotlib
# matplotlib.use("Agg")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import glob
from sklearn import metrics
from sklearn.metrics import precision_recall_curve

PathList = []
def fun(path):
    for fn in glob.glob(path + "\\*.txt"):
        PathList.append(fn)
fun(r"E:\\6 HMDD prediction evaluation\Misim 1.0_results\Yuanshi_jiaodui_yanzheng_causality3_results")

plt.rcParams['figure.dpi'] = 300
plt.figure(1)
font1 = {"family": "Arial",
         "weight": "book",
         "size": 10
         }
plt.xlabel('Recall',font1)
plt.ylabel('Precision',font1)
# Names = ["MCLPMDA","LFEMDA","LPLNS","EGBMMDA","SNMDA","LLCMDA","HLPMDA","ICFMDA","SACMDA","BLHARMDA"]
# file = open("causality_AUPRC.txt", "w")

for path in PathList:
    FileName = os.path.basename(path).split("_")[0]
# for FileName in Names:
    data = pd.read_csv(path,header=None,delimiter="\t",names=["disease","miRNA","y_scores","y_true","causality"])
    data = data.drop_duplicates(subset=["disease", "miRNA", "y_scores"], keep="first")
    data = data.loc[data["causality"] != 2]
    y_true = np.array(data.iloc[:,4])
    y_true = np.where(y_true == 1, True, False)
    y_scores = np.array(data.iloc[:,2])
    area = 0
    precision, recall, thresholds = metrics.precision_recall_curve(y_true, y_scores)
    area = metrics.auc(recall, precision)
    auc = round(area,3)
    print FileName,auc
    # file.write(FileName+"\t"+str(auc)+"\n")
    precision, recall, thresholds = precision_recall_curve(y_true, y_scores)
    plt.figure(1)
    plt.plot(recall,precision,label = FileName+"  AUPRC="+str(auc))
    plt.legend(prop=font1)
plt.savefig("PR_curve.tiff",dpi = 300)
plt.show()
plt.close()
# file.close()



