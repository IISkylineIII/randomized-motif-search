Randomized Motif Search
This repository provides a Python implementation of the Randomized Motif Search algorithm, a probabilistic method for finding motifs (recurring nucleotide sequences) in a collection of DNA strings.

This algorithm is commonly used in bioinformatics to identify conserved motifs, such as binding sites, across multiple DNA sequences.

Overview
The script uses a randomized approach to generate initial motifs.

It iteratively improves the motifs by generating a profile matrix with pseudocounts.

The algorithm terminates when no further improvement in motif score is found.

Repeats the process multiple times (default: 10,000 iterations) to increase the chance of finding a good solution.

How It Works
Randomly selects motifs from the input DNA strings.

Calculates a profile matrix with pseudocounts from current motifs.

Selects the most probable k-mer in each DNA string using the profile.

Repeats steps 2–3 until the score (distance from consensus) no longer improves.

Keeps the best motif set found across all iterations.

Functions
RandomizedMotifSearch(Dna, k, t, iterations): Main function that returns the best motifs found.

RandomMotifs(Dna, k): Generates all k-mers from each DNA string.

ProfileWithPseudocounts(motifs): Builds a profile matrix with Laplace smoothing.

Motifs(profile, Dna): Selects the most probable k-mer based on the profile.

Score(motifs): Calculates total mismatch score against consensus.

Consensus(motifs): Builds a consensus string from the motifs.

Count(motifs): Constructs a count matrix of nucleotides.

Example

k = 8
t = 5
Dna = [
    "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
    "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
    "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
    "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
    "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
]

BestMotifs = RandomizedMotifSearch(Dna, k, t)

for motif in BestMotifs:
    print(motif)
Output
Each line of output represents a motif (substring) of length k, one for each DNA string:

CGGGGGTG
GGGCGAGG
GAAAGAAG
GGTGCACG
AATGTTGG

Requirements
Python 3.x

Uses only built-in Python libraries (no external dependencies)

License
This project is licensed under the MIT License.

