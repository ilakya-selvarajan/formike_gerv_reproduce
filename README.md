## Directory
+ CTCF: The training and test set for train gkmSVM model. To match with the training data of GERV, the training set are from chr1-13 and the test set are from chr14-22. More details in the paper.
+ ALL_ASB_SNP: The positive SNP set
+ ALL_ASB_SNP_10000flank_wo_ALL_ASB_SNP_bootstrap10_size13030: The negative SNP set (10 sets) for Figure 3 right-most panel (CTCF).
+ TRAIN_GKMSVM: the scripts to training gkmSVM and the retrained model output.
+ DELTASVM: the scripts to score SNPs with deltaSVM.
+ OUTPUT: the output of SNP scoring

## Train gkmSVM
We have included the re-trained (June 17, 2016) model in the repository. To use it, you will need to also download (with wget) the kernerl file [here](gerv.csail.mit.edu/mb.ctcf.kernel)(25G)

To train a new model (named mb.ctcf) and score the test set as well as all10mer (for deltasvm):
```
cd TRAIN_GKMSVM
python train_classify.py
```

Evaluate the performance of peak prediction on the test set:
```
cd TRAIN_GKMSVM
python evaluate.py
```

## Score the SNPs
Use the weights of all 10 mers generated from trained gkmSVM model to score the variants:
```
cd DELTASVM
python score.py
```

Evaluate the performance (over 10 pairs of pos-neg set to get a confidence interval on ROC/PRC):
```
cd DELTASVM
Rscript evaluate.R
```
This will generate a ROC.pdf and PRC.pdf under `OUTPUT/`
