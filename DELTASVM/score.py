from os.path import join
from os import system

model = '../TRAIN_GKMSVM/all10mer.mb.ctcf'
postopdir = '../ALL_ASB_SNP'
negtopdir = '../ALL_ASB_SNP_10000flank_wo_ALL_ASB_SNP_bootstrap10_size13030'
negnum = 10
outdir = '../OUTPUT'

ref = join(postopdir,'fasta','ref.fa')
alt = join(postopdir,'fasta','alt.fa')
outfile = join(outdir,'pos.out')
cmd = ' '.join(['perl deltasvm.pl',ref,alt,model,outfile])
system(cmd)

for negidx in range(negnum):
    ref = join(negtopdir,'sample'+str(negidx+1),'fasta','ref.fa')
    alt = join(negtopdir,'sample'+str(negidx+1),'fasta','alt.fa')
    outfile = join(outdir,'neg'+str(negidx+1)+'.out')
    cmd = ' '.join(['perl deltasvm.pl',ref,alt,model,outfile])
    print cmd
    system(cmd)

