source('/cluster/zeng/code/research/tools/PLOT/rocprc.R')
outdir = '../OUTPUT'
dir.create(outdir,showWarnings=F)
neg_sample_num=10

run <- function(outdir,neg_sample_num,seed){
	posfile = file.path(outdir,'pos.out')
    pos = read.delim(posfile,header=F,stringsAsFactors=F)
    pos = pos[,2]
    
    pred = list()
    label = list()
    for (i in 1:neg_sample_num){
    	if (neg_sample_num==1){
    		negfile = file.path(outdir,paste0('neg.out'))
    	}else{
    		negfile = file.path(outdir,paste0('neg',i,'.out'))
    	}
    	neg = read.delim(negfile,header=F,stringsAsFactors=F) 
    	neg = neg[,2]
    	set.seed(seed*100+i);
    	t_pred = c(pos[sample(1:length(pos),length(pos),replace=T)],neg)
    	t_label = c(rep(1,length(pos)),rep(0,length(neg)))
    	pred[[i]] = abs(t_pred)
    	label[[i]] = t_label
    }
    
    rocprc(pred,label,outdir)
}

cnt = 100
run(outdir,neg_sample_num,cnt)
