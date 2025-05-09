# Randomized Motif Search Algorithm

This is a Python implementation of the **Randomized Motif Search** algorithm, which is used for discovering motifs in DNA sequences. The algorithm attempts to find a set of DNA subsequences that are statistically significant and can be used to identify conserved patterns across multiple DNA sequences.

## Installation

To run this algorithm, you need to have **Python 3.x** installed on your system. It is recommended to use a virtual environment for managing dependencies.

### Dependencies
You can install the necessary dependencies by running:

```bash
pip install -r requirements.txt
Usage
Clone the repository to your local machine:
git clone https://github.com/IISkylineIII/randomized-motif-search.git

Navigate to the project directory:
cd randomized-motif-search

Open the Python script randomized_motif_search.py and provide your input data. The function RandomizedMotifSearch accepts three arguments:

Dna: A list of DNA sequences (strings).

k: The length of the motifs to be searched.

t: The number of DNA sequences in the dataset.

Example:
# Example DNA sequences
Dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", 
       "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", 
       "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", 
       "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", 
       "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

# Call the algorithm with k = 8 and t = 5
BestMotifs = RandomizedMotifSearch(Dna, 8, 5)

# Print the resulting motifs
for motif in BestMotifs:
    print(motif)
Run the script:
python randomized_motif_search.py

CGCC
GGGC
TACG
TACG
...
License
This project is licensed under the MIT License - see the LICENSE file for details.



