protein_letters = 'ACDEFGHIKLMNPQRSTVNWY-X'
rna_letters = 'GAUCN-'
dna_letters = 'GATCN-'

#COMPLEMENT

dna_complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
rna_complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}


#CODON TABLES

rna_table = {'GUC': 'V', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'GUU': 'V', 'AAC': 'N', 'AGG': 'R', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'AGA': 'R', 'AAU': 'N', 'ACU': 'T', 'CAC': 'H', 'GUG': 'V', 'CCG': 'P', 'CCA': 'P', 'AGU': 'S', 'CCC': 'P', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'CGA': 'R', 'CAG': 'Q', 'CGC': 'R', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'CCU': 'P', 'GGG': 'G', 'GGA': 'G', 'GGC': 'G', 'GAG': 'E', 'UCC': 'S', 'UAC': 'Y', 'CGU': 'R', 'GAA': 'E', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'UCA': 'S', 'AUG': 'M', 'CUG': 'L', 'AUU': 'I', 'CAU': 'H', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'GAC': 'D', 'GUA': 'V', 'UGC': 'C', 'GCU': 'A', 'UGU': 'C', 'CUC': 'L', 'UUG': 'L', 'UUA': 'L', 'GAU': 'D', 'UUC': 'F'}

rna_table_back = {'A': 'GCU', 'C': 'UGU', None: 'UAA', 'E': 'GAG', 'D': 'GAU', 'G': 'GGU', 'F': 'UUU', 'I': 'AUU', 'H': 'CAU', 'K': 'AAG', 'M': 'AUG', 'L': 'UUG', 'N': 'AAU', 'Q': 'CAG', 'P': 'CCU', 'S': 'UCU', 'R': 'CGU', 'T': 'ACU', 'W': 'UGG', 'V': 'GUU', 'Y': 'UAU'}

rna_stop_codons = ['UAA', 'UAG', 'UGA']
rna_start_codons = ['UUG', 'CUG', 'AUG']

dna_table = {'CTT': 'L', 'ATG': 'M', 'ACA': 'T', 'ACG': 'T', 'ATC': 'I', 'ATA': 'I', 'AGG': 'R', 'CCT': 'P', 'AGC': 'S', 'AGA': 'R', 'ATT': 'I', 'CTG': 'L', 'CTA': 'L', 'ACT': 'T', 'CCG': 'P', 'AGT': 'S', 'CCA': 'P', 'CCC': 'P', 'TAT': 'Y', 'GGT': 'G', 'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'GGG': 'G', 'GGA': 'G', 'GGC': 'G', 'TAC': 'Y', 'CGT': 'R', 'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GAG': 'E', 'GTT': 'V', 'GAC': 'D', 'GAA': 'E', 'AAG': 'K', 'AAA': 'K', 'AAC': 'N', 'CTC': 'L', 'CAT': 'H', 'AAT': 'N', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'TGT': 'C', 'TCT': 'S', 'GAT': 'D', 'TTT': 'F', 'TGC': 'C', 'TGG': 'W', 'TTC': 'F', 'TCG': 'S', 'TTA': 'L', 'TTG': 'L', 'TCC': 'S', 'ACC': 'T', 'TCA': 'S', 'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A'}

dna_table_back = {'A': 'GCT', 'C': 'TGT', None: 'TAA', 'E': 'GAG', 'D': 'GAT', 'G': 'GGT', 'F': 'TTT', 'I': 'ATT', 'H': 'CAT', 'K': 'AAG', 'M': 'ATG', 'L': 'TTG', 'N': 'AAT', 'Q': 'CAG', 'P': 'CCT', 'S': 'TCT', 'R': 'CGT', 'T': 'ACT', 'W': 'TGG', 'V': 'GTT', 'Y': 'TAT'}

dna_stop_codons = ['TAA', 'TAG', 'TGA']
dna_start_codons = ['TTG', 'CTG', 'ATG']
