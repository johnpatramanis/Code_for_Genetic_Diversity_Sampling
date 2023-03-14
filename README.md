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


The correct version of the cache needs to be downloaded and placed in a folder path "VEP_Cache/homo_sapiens/" within the main directory of the workflow
Download Cache from: https://ftp.ensembl.org/pub/release-109/variation/vep/homo_sapiens_vep_109_GRCh38.tar.gz
