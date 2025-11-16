# About
This repo contains is contains necessary scripts and relevant outputs for variant calling analysis on TP53 for both samples from a single patient in the study described by *Circulating tumor DNA sequencing in colorectal cancer patients treated with first-line chemotherapy with anti-EGFR*. Specifically, the repo contains a Jupyter Notebook, VCA_workflow.ipynb, that houses all necessary steps for pre-processing and variant calling analysis along with descriptions of each step and information relevant to the analysis. The repo also contains a BASH file that can be used to replicate the CONDA env I used to run this analysis and a TXT file that is used for mapping RefSeq coordinates to chromosome numbers (used in workflow). Additionally, the most relevant files output by this workflow, including the BAM files produced by pre-processing and annotated VCF files produced by variant calling analysis, are included in the data sub-directory. Intermediate files were not included due to storage limitations and since they can be easily reproduced.


# Excercise Specific Information

Patient: CTC360

Pre-Treatment Sample Reads:
- Biosample - https://www.ncbi.nlm.nih.gov/biosample/18318230
- SRA - https://www.ncbi.nlm.nih.gov/sra?LinkName=biosample_sra&from_uid=18318230
- SRR - https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR13973704&display=metadata
- FASTQ - SRR13973704.fastq

During/Post-Treatment Sample Reads:
- Biosample -  https://www.ncbi.nlm.nih.gov/biosample/18318229
- SRA - https://www.ncbi.nlm.nih.gov/sra?LinkName=biosample_sra&from_uid=18318229
- SRR - https://trace.ncbi.nlm.nih.gov/Traces/?view=run_browser&acc=SRR13973705&display=metadata
- FASTQ - SRR13973705.fastq

Gene of Interest: TP53
- Refseq - https://www.ncbi.nlm.nih.gov/gene/7157
- UCSC GB - https://genome.ucsc.edu/cgi-bin/hgGene?hgg_gene=ENST00000618944.4&hgg_chrom=chr17&hgg_start=7668401&hgg_end=7675493&hgg_type=knownGene&db=hg38
- Acts as a tumor suppressor in many tumor types; induces growth arrest or apoptosis depending on the physiological circumstances and cell type. Involved in cell cycle regulation as a trans-activator that acts to negatively regulate cell division by controlling a set of genes required for this process.
- 71 mutations over 64 patients (68.8%) at baseline in study.
- The TP53 gene is the most frequently mutated gene (>50%) in human cancer, indicating that the TP53 gene plays a crucial role in preventing cancer formation.

Reference Genome: hg38
- https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/001/405/GCF_000001405.26_GRCh38/GCF_000001405.26_GRCh38_genomic.fna.gz 

Known Variants VCF: dbSNP (latest release)
- https://ftp.ncbi.nih.gov/snp/latest_release/VCF/GCF_000001405.40.gz

Clinical Relevance Annotation: ClinVar
- https://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh38/clinvar_20251109.vcf.gz

