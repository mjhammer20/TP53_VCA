# Imports
import pandas as pd

# Import VCF files to DataFrame

pre_treatment_variants = pd.read_csv('data/SRR13973704_annotated.vcf', comment='#', sep='\t', 
                                     names=['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'SRR13973704'])
post_treatment_variants = pd.read_csv('data/SRR13973705_annotated.vcf', comment='#', sep='\t',
                                      names=['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'SRR13973704'])

# Filter variants based on clinical relevance

clinically_relevant_pre_treatment_variants = pre_treatment_variants[pre_treatment_variants['ID'] != '.']
clinically_relevant_post_treatment_variants = post_treatment_variants[post_treatment_variants['ID'] != '.']