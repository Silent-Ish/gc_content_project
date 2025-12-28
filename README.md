# GC Content Calculator & Visualizer

## Overview
This Python-based bioinformatics tool calculates the **GC content** of DNA sequences provided in FASTA format.  
It performs a **sliding window analysis** to visualise local GC content variation across a genomic sequence, helping identify GC-rich regions such as **promoters, CpG islands, and gene-dense regions**.

The tool is designed for **command-line use**, making it suitable for integration into bioinformatics pipelines.

---

## Biological Context
The script was validated using the **Human TIMP2 gene (Tissue Inhibitor of Metalloproteinases 2)**.  
The analysis successfully highlights GC-rich regions upstream of the coding sequence, consistent with known regulatory promoter regions.

---

## Features
- Reads DNA sequences from FASTA files using **Biopython**
- Calculates **overall GC content (%)**
- Performs **sliding window GC analysis**
- Generates GC content plots using **Matplotlib**
- Customisable window size, step size, and output filename via CLI

---

## Installation

### Requirements
- Python **≥ 3.8**
- Biopython
- Matplotlib

### Clone the repository
```bash```
git clone https://github.com/Silent-Ish/gc_content_project.git
cd gc_content_project

### Usage
Run the script from the terminal:
python gc_calculator.py -i test_seq_timp_2_human.fasta


###Optional Arguments 
Flag|Name    |Description.                       |Default
-i  |--input |(Required) Path to input FASTA file|N/A
-w  |--window|Size of the sliding window (bp)    |20
-s  |--step  |Step size to move the window (bp)  |5
-o  |--output|Filename for the saved plot image  |gc_plot.png

#Author
Ismael
