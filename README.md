# HomologousProteinSeeker Tool (03713 Final Project)
The HomologousProteinSeeker pipeline is designed for taking amino acid sequences and using bioinformatic tools to visually and annotatively compare homologous protein structures.

Pipeline Overview:
Structure Prediction with Esm-fold:

Converts amino acid sequences (from FASTA files) into predicted protein structures (PDB files) using the Esm-fold model.
A Python script is generated for each FASTA file, which is then output as an sbatch script to be submitted to GPU-shared clusters (like Bridges) for running Esm-fold.
Visualization and Comparison:

Once the predicted PDB files are generated, PyMOL is used to visualize and compare the structures.
Root Mean Square Deviation (RMSD) values are calculated to quantify the structural similarity between proteins, and the output is stored as text files and visualized as PNG images.
Homolog Search with Foldseek:

The PDB files are also processed using Foldseek to search for homologous proteins in various protein databases.
Foldseek helps in annotating the structural data, enabling users to understand structure conservation, functional domains, and detect distant homology.
Key Features:
Automated Pipeline: Streamlines the process from sequence input (FASTA) to structure comparison (PDB) and homolog search.
Visualization and Comparison: Generates visual representations of protein structures and calculates RMSD values for quantitative comparison.
Homology Detection: Uses Foldseek to identify homologous proteins and provide structural annotations.
Usage:
Prepare your amino acid sequences in FASTA format.
Run the provided Python scripts to submit jobs to a shared GPU cluster.
Once the PDB files are generated, use PyMOL for structure comparison and Foldseek for homolog search and annotation.
