import os
import os.path
from os import listdir
from os.path import isfile, join
import sys
from Bio import SeqIO



FILES_IN_FOLDER = [f for f in os.listdir('.') if os.path.isfile(f)]
FASTA_FILE_LIST= [f for f in FILES_IN_FOLDER if '.fa' in f]


OUTPUT=open('Protein_Coverage.txt','w')


COVERAGE={}

for FILE in FASTA_FILE_LIST:
    fasta_sequences = SeqIO.parse(open(FILE),'fasta')
    for fasta in fasta_sequences:
        name, sequence = fasta.id, str(fasta.seq)
        name=name.split('/')[0]
        name=name.split('_')
        sample='_'.join(name[0:len(name)-1])
        protein=name[len(name)-1]
        
        
        if 'Paranthropus' in sample:
            if sample not in COVERAGE.keys():
                COVERAGE[sample]={}
            
            counter=1            
            for POS in sequence:
                counter+=1
                if POS!='?':
                    if protein not in COVERAGE[sample].keys():
                        COVERAGE[sample][protein]=[]
                    COVERAGE[sample][protein].append(counter)

            # print(sample,protein)
            
TOTAL_COVERAGE={}

for SMPL in COVERAGE.keys():
    for PRTN in COVERAGE[SMPL].keys():
        if PRTN not in TOTAL_COVERAGE.keys():
            TOTAL_COVERAGE[PRTN]=[]
        for PSTN in COVERAGE[SMPL][PRTN]:
            TOTAL_COVERAGE[PRTN].append(PSTN)
            




####### For getting positions covered by ALL 4 P.rob samples
for PRTN in TOTAL_COVERAGE.keys():
    TOTAL_COVERAGE[PRTN]=sorted(TOTAL_COVERAGE[PRTN])
    TOTAL_COVERAGE_UNIQUE=list(set(TOTAL_COVERAGE[PRTN])) ### Sites only once, so we can loop through them

    ### Only select positions that are counted 4 times
    TOTAL_COVERAGE[PRTN]=[ str(SITE) for SITE in TOTAL_COVERAGE_UNIQUE if TOTAL_COVERAGE[PRTN].count(SITE)==4 ]
    print(PRTN,TOTAL_COVERAGE[PRTN])
    POSITIONS=','.join(TOTAL_COVERAGE[PRTN])
    OUTPUT.write(F'{PRTN}\t{POSITIONS}\n')







####### For getting positions covered by at least one P.rob sample!
# for PRTN in TOTAL_COVERAGE.keys():
    # TOTAL_COVERAGE[PRTN]=sorted(list(set(TOTAL_COVERAGE[PRTN])))
    # TOTAL_COVERAGE[PRTN]=[str(x) for x in TOTAL_COVERAGE[PRTN]]
    # print(PRTN,TOTAL_COVERAGE[PRTN])
    # POSITIONS=','.join(TOTAL_COVERAGE[PRTN])
    # OUTPUT.write(F'{PRTN}\t{POSITIONS}\n')
    
# print(TOTAL_COVERAGE)