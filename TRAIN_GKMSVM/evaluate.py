from sklearn import metrics

with open('../CTCF/postest.fa.pred') as f:
    pospred = [float(x.strip().split()[1])for x in f]
with open('../CTCF/negtest.fa.pred') as f:
    negpred = [float(x.strip().split()[1])for x in f]

label = [1]*len(pospred) + [0]*len(negpred)
pred = pospred + negpred

fpr, tpr, thresholds = metrics.roc_curve(label, pred, pos_label=1)
print 'peakPred AUC (test set):',metrics.auc(fpr, tpr)
