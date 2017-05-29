<img width="250px" src="https://github.com/scastlara/miniseq/blob/master/miniseq/logo.png"/>
Tiny package to handle sequences and FASTA.

## Usage
```python
import miniseq as ms
fasta = ms.FASTA(filename="myfasta.fa")

# Filter sequences longer than 125
filtered_by_length  = fasta.filter_by_length(length=125, mode="above")

# Get some specific sequences
filtered_by_id      = fasta.filter_by_id(identifiers=["seq1", "seq2", "seq56"])

# Get sequences and print identifier and sequence length
for seq in fasta:
    print( "id:%s length:%s\n" % ( seq.get_identifier(), seq.get_sequence() ) )

# Write new FASTA with filtered sequences
filtered_by_id.write("myfilteredfasta.fa")

# Plot length distribution of sequences in fasta
import matplotlib.pyplot as plt
plt.boxplot(fasta.get_lengths())
plt.show()
```

## Install
```bash
git clone https://github.com/scastlara/miniseq.git
sudo python3 setup.py install
```

## Classes
---
### Sequence

#### Attributes

* **identifier:**
> Sequence identifier

* **sequence:**   
> Sequence letters


#### Methods

* **get_identifier:**
> Getter of identifier

* **get_sequence:**
> Getter of sequence

* **has_subsequence:**
> Gets subseq string and checks if it is in the sequence.
> Returns True or False.

* **has_pattern:**
> Gets a regex and checks if it is in the sequence.
> Returns True or False.

----
### DNASequence
Inherits from Sequence.

#### Methods

* **translate:**
>Returns the Protein (from first start codon to stop).

----
### RNASequence
Inherits from Sequence.

#### Methods

* **reverse_transcribe:**
> Returns the DNASequence.

-----
### Protein
Inherits from Sequence.

-----
### FASTA

#### Attributes
>  One or the other! By default, first argument is 'filename'.

* **filename:**
> Filename of the FASTA file

* **sequences:**
> List of Sequence objects.


#### Methods

* **get_number**      
> Get number of sequences.

* **get_sequences**
> Get the list of sequences

* **get_types:**       
> Gets types of sequences as a dictionary.

* **filter_by_id(identifiers):**
> Filters by the sequences with the identifiers in the 'identifiers' list.
> Returns FASTA object.

* **add_sequence:**    
> Adds sequence object to FASTA.

* **get_sequence(identifier):**
> Returns seq object (or None) with matching identifier (only one seq!)

* **write(filename, max_linesize=100):**
> Writes FASTA to filename. Each line will be of length max_linesize.

* **filter_by_length(length, mode="above"):**
> Returns FASTA with sequences with length >= or <= 'length'.
> Set mode to 'above' or 'below'.

* **get_lengths(filename):**
> Gets list of lengths
