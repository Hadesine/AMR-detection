
# AMR-detection

This repository contains antimicrobial resistance (AMR) gene detection results for multiple bacterial species.
Each folder includes the genome input, analysis outputs, and a summary of findings.

## Bacteria Covered

- [Staphylococcus aureus](./Staphylococcus_aureus) 
- [Escherichia coli](./Escherichia_coli) (ongoing)
- [Klebsiella pneumoniae](./Klebsiella_pneumoniae) (ongoing)

## Tools Used

- NCBI SRA Toolkit (data retrival)
- FastQC (quality control)
- Trimmomatic (read trimming)
- MEGAHIT (genome assemble), Quast (assessing assembly quality), seqtk (removing short contigs)
- BWA (reference alignment)n Qualimap (assessing quality of alignment)
- Prokka (genome annotation)
- CARD database - RGI (Resistance Gene Identifier)
- AMRFinderplus - (AMR gene identification)
- Python -pandas matplotlib seaborn (visualization)
