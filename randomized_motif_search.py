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
