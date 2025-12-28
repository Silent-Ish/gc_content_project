import sys
import argparse
from Bio import SeqIO
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
import os

def calculate_gc_content(sequence):
    """
    Calculates the GC percentage of a given DNA sequence.
    """
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    if len(sequence) == 0:
        return 0
    return ((g_count + c_count) / len(sequence)) * 100

def plot_gc_content(sequence, window_size, step_size, output_file):
    """
    Calculates GC content in a sliding window and plots it.
    """
    gc_values = []
    positions = []
    
    # Sliding window logic
    for i in range(0, len(sequence) - window_size, step_size):
        sub_sequence = sequence[i:i+window_size]
        gc = calculate_gc_content(sub_sequence)
        gc_values.append(gc)
        positions.append(i)
        
    # Plotting
    plt.figure(figsize=(10, 5))
    plt.plot(positions, gc_values, color='blue', linewidth=1)
    plt.title(f'GC Content (Window: {window_size}, Step: {step_size})')
    plt.xlabel('Genome Position (bp)')
    plt.ylabel('GC Content (%)')
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Save plot to the specified output file
    plt.savefig(output_file)
    print(f"Plot saved as {output_file}")
    # plt.show() # Commented out so it runs smoothly in terminals without popping up windows

def main():
    # 1. Setup the Argument Parser
    parser = argparse.ArgumentParser(description="A tool to analyze GC content in DNA sequences.")
    
    # 2. Add Arguments
    # Input file argument (Required)
    parser.add_argument("-i", "--input", help="Path to the input FASTA file", required=True)
    
    # Window size argument (Optional, default is 20)
    parser.add_argument("-w", "--window", help="Sliding window size (default: 20)", type=int, default=20)
    
    # Step size argument (Optional, default is 5)
    parser.add_argument("-s", "--step", help="Step size for sliding window (default: 5)", type=int, default=5)

    # Output image argument (Optional, default is gc_plot.png)
    parser.add_argument("-o", "--output", help="Output filename for the plot image", default="gc_plot.png")
    
    # 3. Parse the arguments
    args = parser.parse_args()

    try:
        # Read the file using the argument provided by the user (args.input)
        record = SeqIO.read(args.input, "fasta")
        dna_sequence = record.seq.upper()
        
        # Overall GC Content
        overall_gc = calculate_gc_content(dna_sequence)
        print(f"Processing file: {args.input}")
        print(f"Sequence ID: {record.id}")
        print(f"Total Length: {len(dna_sequence)} bp")
        print(f"Overall GC Content: {overall_gc:.2f}%")
        
        # Sliding Window Analysis using user arguments
        plot_gc_content(dna_sequence, args.window, args.step, args.output)
        
    except FileNotFoundError:
        print(f"Error: The file '{args.input}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()