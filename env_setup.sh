#!/bin/bash

# Create conda env

conda create -n NGS

# Download BWA

conda install bioconda::bwa

# Download samtools and htslib

conda install bioconda::samtools
conda install bioconda::htslib

# Install GATK

conda install bioconda::gatk4

# Install bcftools
conda install bicoconda::bcftools

# Install snpeff and create alias for SnpSift

curl -v -L 'https://snpeff.odsp.astrazeneca.com/versions/snpEff_latest_core.zip' > snpEff_latest_core.zip
unzip snpEff_latest_core.zip
alias SnpSift='java -Xm8g -jar ~/snpEff_latest_core/SnpEff/SnpSift.jar'

# Install pandas 
conda install pip
pip install pandas