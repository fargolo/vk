#! /usr/bin/Rscript
cat("\n\n")

# LSA analysis
lsa.coherence <- function(fpath = "~/vk/transc/Eleanor-Longden/TED/talk.txt", 
                          lsapath = "~/LSASpace/EN_100k.rda"){
  require(LSAfun)
  load(lsapath)
  transc <- readChar(fpath,file.info(fpath)$size)
  transc <- gsub(pattern = "\n",replacement = ".", x = transc)
  coh.data <- LSAfun::coherence(x = transc, tvectors = EN_100k)
  cat("\n\nGlobal Semantic Coherence is:\n")
  cat(coh.data$global, sep = " ")
  cat("\n\n Estimates based on EN_100K semantic space,\ncontaining ~2 Billion word corpus compiled from British National Corpus and 2009 Wikipedia dump. More info on \n\n http://www.lingexp.uni-tuebingen.de/z2/LSAspaces/")
  }

options(warn = -1)
lsa.coherence()
