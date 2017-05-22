# miniseq
Tiny package to handle sequences and FASTA


## Classes

### Sequence
* **Attributes**

```
    identifier: Sequence identifier
    sequence:   Sequence letters
```

* **Methods**

```
    get_identifier:  Getter of identifier
    get_sequence:    Getter of sequence
    has_subsequence: Gets subseq string and checks if it is in the sequence.
                     Returns True or False.
    has_pattern:     Gets a regex and checks if it is in the sequence.
                     Returns True or False.
```

### DNASequence
Inherits from Sequence.

* **Methods**

```
    translate: Returns the Protein (from first start codon to stop).
```

### RNASequence
Inherits from Sequence.

* **Methods**

```
    reverse_transcribe: Returns the DNASequence.
```

### Protein
Inherits from Sequence.

### FASTA

* **Attributes**

```
    # One or the other! By default, first argument is 'filename'.
    filename:   Filename of the FASTA file
    sequences:  List of Sequence objects.
```

* **Methods**

```
    get_number:      Get number of sequences.
    get_types:       Gets types of sequences as a dictionary.
    get_sequences(identifiers): Filters by the sequences with the identifiers in the 'identifiers' list.
                                Returns FASTA object.

    add_sequence:    Adds sequence object to FASTA.

    write(filename, max_linesize=100): Writes FASTA to filename. Each line will be of length max_linesize.

    filter_by_length(length, ab=True, bel=False): Returns FASTA with sequences with length >= or <= 'length'.
                                                  Set ab=True to '>=' or bel=True to '<='.
```
