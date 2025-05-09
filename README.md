Usage
Clone the repository to your local machine:

bash

git clone https://github.com/IISkylineIII/randomized-motif-search.git
Navigate to the project directory:

bash

cd randomized-motif-search
Open the Python script randomized_motif_search.py and provide your input data. The function RandomizedMotifSearch accepts three arguments:

Dna: A list of DNA sequences (strings).

k: The length of the motifs to be searched.

t: The number of DNA sequences in the dataset.

Example:

python
Copiar
Editar
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

bash
Copiar
Editar
python randomized_motif_search.py
Example Output
The output will be the most probable motifs discovered in the input DNA sequences:

plaintext
Copiar
Editar
CGCC
GGGC
TACG
TACG
...
License
This project is licensed under the MIT License - see the LICENSE file for details.




