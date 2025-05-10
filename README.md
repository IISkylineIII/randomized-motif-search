# Randomized Motif Search Algorithm

This Python implementation demonstrates the **Randomized Motif Search** algorithm for motif finding in DNA sequences. The goal is to discover motifs of a given length \(k\) that appear most frequently in a collection of DNA strings.

## Algorithm Overview

The **Randomized Motif Search** works by starting with random motifs from the DNA sequences, iterating through a series of steps to improve the motifs based on their scores. The algorithm attempts to minimize the score, which is defined by the number of mismatches between the motifs and their consensus sequence.

The algorithm works as follows:

1. **Initialization**: Random motifs are selected from the input DNA sequences.
2. **Iterative Improvement**: The motifs are iteratively updated by creating a profile of the motifs and selecting the most probable motifs based on the profile.
3. **Profile Calculation**: A profile is built using pseudocounts to avoid zero probabilities.
4. **Motif Search**: New motifs are selected from the DNA sequences based on the probability given by the profile.
5. **Score Calculation**: The score of the motifs is calculated based on the consensus sequence, and the best motifs are updated if the new motifs have a better score.

## Python Code

```python
import random

def RandomizedMotifSearch(Dna, k, t, iterations=10000):
    BestMotifs = [random.choice(seq) for seq in Dna]
    BestScore = float('inf')

    for _ in range(iterations):
        motifs = RandomMotifs(Dna, k)
        current_score = Score(motifs)
        while True:
            profile = ProfileWithPseudocounts(motifs)
            motifs = Motifs(profile, Dna)
            new_score = Score(motifs)
            if new_score < current_score:
                current_score = new_score
            else:
                break
        if current_score < BestScore:
            BestMotifs = motifs
            BestScore = current_score

    return BestMotifs

def RandomMotifs(Dna, k):
    return [seq[i:i+k] for seq in Dna for i in range(len(seq) - k + 1)]

def ProfileWithPseudocounts(motifs):
    profile = {'A': [1] * len(motifs[0]), 'C': [1] * len(motifs[0]), 'G': [1] * len(motifs[0]), 'T': [1] * len(motifs[0])}
    total_motifs = len(motifs)

    for i in range(len(motifs[0])):
        for motif in motifs:
            profile[motif[i]][i] += 1

    for nucleotide in profile:
        for i in range(len(profile[nucleotide])):
            profile[nucleotide][i] /= (total_motifs + 4)  # Add pseudocounts

    return profile

def Motifs(profile, Dna):
    k = len(profile['A'])
    motifs = []
    for seq in Dna:
        most_probable = ""
        max_prob = -1
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i+k]
            prob = 1
            for j in range(k):
                prob *= profile[kmer[j]][j]
            if prob > max_prob:
                max_prob = prob
                most_probable = kmer
        motifs.append(most_probable)
    return motifs

def Score(motifs):
    consensus = Consensus(motifs)
    score = 0
    for motif in motifs:
        score += sum(c1 != c2 for c1, c2 in zip(consensus, motif))
    return score

def Consensus(motifs):
    k = len(motifs[0])
    count_matrix = Count(motifs)
    consensus = ""
    for i in range(k):
        max_count = -1
        most_common_base = ""
        for base, count in count_matrix.items():
            if count[i] > max_count:
                max_count = count[i]
                most_common_base = base
        consensus += most_common_base
    return consensus

def Count(motifs):
    count_matrix = {'A': [0] * len(motifs[0]), 'C': [0] * len(motifs[0]), 'G': [0] * len(motifs[0]), 'T': [0] * len(motifs[0])}
    for motif in motifs:
        for i in range(len(motif)):
            count_matrix[motif[i]][i] += 1
    return count_matrix

# Example usage
k = 8
t = 5
Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]
BestMotifs = RandomizedMotifSearch(Dna, k, t)
for motif in BestMotifs:
    print(motif) 
```
### RandomizedMotifSearch
The RandomizedMotifSearch function is the core of the algorithm. It starts with a random selection of motifs and iteratively refines them by using the profile-based approach. The function aims to minimize the score, which is calculated based on the consensus sequence of the motifs.

### Helper Functions
RandomMotifs: Generates random motifs from the DNA sequences.

ProfileWithPseudocounts: Builds a profile matrix with pseudocounts to avoid zero probabilities during motif selection.
Motifs: Finds the most probable motifs from the DNA sequences based on the profile matrix.
Score: Calculates the score of the motifs, which is the number of mismatches with the consensus sequence.
Consensus: Calculates the consensus sequence from a set of motifs.
Count: Builds a count matrix for the nucleotides in the motifs.

### Requirements
Python 3.6 or higher
No external libraries are required.

### Applications
Genome assembly and sequence reconstruction
Bioinformatics tasks involving paired k-mers
Eulerian path applications in graph theory

### License
This project is licensed under the MIT License.

