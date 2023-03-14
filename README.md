# Code_for_Genetic_Diversity_SAmpling

How to re-run the 'genetic variation' analysis described in Maduper,Konig,Patramanis et al 2023

First Clone this repository in your local computer:

```bash
git clone https://github.com/johnpatramanis/Code_for_Genetic_Diversity_Sampling.git
```

Enter the repo and install the required conda environment (Requires conda to be installed: ) which contains all of the necessary prerequisites:



```bash
cd Code_for_Genetic_Diversity_Sampling
conda env create -f Paranth_Genet_Variat.yml
```

Once the installation is complete activate the environment:

```bash
conda activate Par_gen
```

The we need some VCF files for this analysis. If you want to run the analysis for the same dataset as we did in our manuscript, you must use the VCF files from here:


Finally the correct version of the VEP cache needs to be downloaded and placed in a folder path "VEP_Cache/homo_sapiens/" within the main directory of this workflow.
Download Cache from: https://ftp.ensembl.org/pub/release-109/variation/vep/homo_sapiens_vep_109_GRCh38.tar.gz using:

```bash
mkdir -p VEP_Cache/hmo_sapiens
cd VEP_Cache/hmo_sapiens
wget https://ftp.ensembl.org/pub/release-108/variation/vep/homo_sapiens_vep_108_GRCh38.tar.gz
tar –xvzf  homo_sapiens_vep_108_GRCh38.tar.gz
```
