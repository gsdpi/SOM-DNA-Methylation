import pandas as pd
import numpy as np

'''
Reads methylation data from a large TSV file, and stores them in hdf5 format, 
that loads faster.
 
The tsv file used in examples can be found in Xenabrowser portal:

https://xenabrowser.net/datapages/
cohort: GDC TCGA Pheochromocytoma & Paraganglioma (PCPG)
dataset: DNA methylation - Illumina Human Methylation 450

To read use:
    df = pd.read_hdf('path-to-file/TCGA-PCPG.methylation450.h5')
'''

print('reading file in TSV format...')
df = pd.read_csv('TCGA-PCPG.methylation450.tsv',sep='\t')

print('storing in hdf5 format...')
df.to_hdf('TCGA-PCPG.methylation450.h5',key='methylation')

print('... done.')


