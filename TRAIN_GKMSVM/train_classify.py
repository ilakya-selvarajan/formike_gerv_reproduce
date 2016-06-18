import os
topdir = '../CTCF'
train_pos = os.path.join(topdir,'postrain.fa')
train_neg = os.path.join(topdir,'negtrain.fa')
test_pos = os.path.join(topdir,'postest.fa')
test_neg = os.path.join(topdir,'negtest.fa')

exp='mb.ctcf'
kernel = exp + '.kernel'
svm = exp + '.svm'
svm_svseq = svm + '_svseq.fa'
svm_svalpha = svm + '_svalpha.out'
test_pos_out = exp + '.test.pos.out'
test_neg_out = exp + '.test.neg.out'


cmd = ' '.join(['./gkmsvm_kernel -d 3 ',train_pos, train_neg,kernel])
print cmd
os.system(cmd)

cmd = ' '.join(['./gkmsvm_train ',kernel,train_pos, train_neg,svm])
print cmd
os.system(cmd)

cmd = ' '.join(['./gkmsvm_classify -d 3 ','all10mer.fa',svm_svseq, svm_svalpha,'all10mer.'+exp])
print cmd
os.system(cmd)

cmd = ' '.join(['./gkmsvm_classify -d 3 ',test_pos,svm_svseq, svm_svalpha,test_pos+'.pred'])
print cmd
os.system(cmd)

cmd = ' '.join(['./gkmsvm_classify -d 3 ',test_neg,svm_svseq, svm_svalpha,test_neg+'.pred'])
print cmd
os.system(cmd)
