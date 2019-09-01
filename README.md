# Benchmark-miRNA-disease-2019

Source codes and datasets for benchmark of computational methods for predicting microRNA-disease associations

Source codes implemented on Python 2.7:
PRC.py----------calculate AUPRC of predictors and plot PRC charts
ROC.py----------calculate AUROC and plot ROC charts
Max_min data.py----------iterative integration of predictors using their Max_min normalized results 
Sigmoid data.py----------iterative integration of predictors using their Sigmoid normalized results 
Z_score data.py----------iterative integration of predictors using their Z_score normalized results 
Yuanshi data.py----------iterative integration of predictors using their original results

Required libraries: numpy, pandas, os, glob, matplotlib, sklearn

We suggest  that you could install Anaconda to meet these requirements

List for the benchmark datasets:
AUPRC.txt----------the AUPRC results of 36 predcitors
benchmark2019.txt----------ALL benchmarking dataset from HMDD v3.1
benchmark2019_causal.txt----------CAUSAL benchmarking dataset from HMDD v3.1
benchmark2019_dbDEMC.txt----------dbDEMC dataset
disease-mapping2019.txt----------The disease mapping between HMDD v3.1 and HMDD v2.0 used in the benchmarking analysis
prediction_conbined.xlsx----------The prediction scores of the top predictors and the combined predictor, in HMDD v2.0 format
Max_Min data----------the Max_Min normalized predcition results of 36 predictors
Sigmoid data----------the Sigmoid normalized predcition results of 36 predictors
Yuanshi data----------the original  predcition results of 36 predictors
Z_score data----------the Z_score normalized predcition results of 36 predictors

Announcements: when you run the code, you need to pay attention to setting the correct file path.
