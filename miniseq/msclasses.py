"""
Module to handle sequences
"""
import miniseq.seqdata as seqdata
import re

# ----------------------------------------------------
# CLASSES
# ----------------------------------------------------
class Sequence(object):
    """
    Sequence base class
    """
    alphabet = set()
    def __init__(self, identifier, sequence):
        self.__identifier = identifier
        self.__sequence   = sequence.upper()

    def __len__(self):
        return len(self.__sequence)

    def __eq__(self, target):
        return self.__sequence == target.get_sequence()

    def __ne__(self, target):
        return self.__sequence != target.get_sequence()

    def __add__(self, target):
        if type(self) is type(target):
            identifier = self.__identifier + target.get_identifier()
            sequence   = self.__sequence + target.get_sequence()
            return(type(self)(identifier, sequence))
        else:
            raise Exception("Can't concatenate objects of different class.")

    def __lt__(self, target):
        return(len(self) < len(target))

    def __le__(self, target):
        return(len(self) <= len(target))

    def __gt__(self, target):
        return(len(self) > len(target))

    def __ge__(self, target):
        return(len(self) >= len(target))

    def __getitem__(self, key):
        return(self.__sequence[key])

    def get_identifier(self):
        """
        Getter of identifier
        """
        return self.__identifier

    def get_sequence(self):
        """
        Getter of sequence
        """
        return self.__sequence

    def has_subsequence(self, subsequence):
        """
        Checks if a string is found inside the sequence
        """
        if subsequence.get_sequence() in self.__sequence:
            return True
        else:
            return False

    def check_alphabet(self):
        """
        Checks if the alphabet is correct for the sequence type
        """
        for char in self.__sequence:
            if char not in self.alphabet:
                raise IncorrectSequenceLetter(char, self.__class__.__name__ )

    def has_pattern(self, pattern):
        """
        Checks if regex pattern is found in sequence
        """
        if re.search(pattern, self.__sequence):
            return True
        else:
            return False

    def get_type(self):
        """
        Returns sequence type
        """
        return "Sequence"

    def __str__(self):
        max_linesize = 40
        seq_split    = list()

        for i in range(0, len(self.__sequence), max_linesize):
            seq_split.append(self.__sequence[i:max_linesize + i])
        return ">%s\n%s" % (self.__identifier, "\n".join(seq_split))

class Protein(Sequence):
    """
    Protein class
    """
    alphabet  = set(seqdata.protein_letters)

    def __init__(self, identifier, sequence):
        super(Protein, self).__init__(identifier, sequence)
        self.check_alphabet()

    def get_type(self):
        return "Protein Sequence"


class NucleotideSequence(Sequence):
    """
    Nucleotide sequence class
    """
    def translate(self):
        """
        Returns Protein object (from first start codon to first stop after start)
        """
        # Find first start codon index
        start_index   = int()
        prot_sequence = str()
        found = 0
        for i in range(0, len(self.get_sequence()), 1):
            codon = self.get_sequence()[i:i+3]
            if codon in self.start_codons:
                start_index   = i
                found = 1
                break
        if not found:
            raise ValueError("Your nucleotide sequence %s doesn't have a start codon"
                             % self.get_identifier())

        # Translate from the start codon
        for j in range(start_index, len(self.get_sequence()), 3):
            curr_codon = self.get_sequence()[j:j+3]
            if len(curr_codon) < 3:
                # Out of sequence with no stop codon
                return Protein(identifier=self.get_identifier(), sequence=prot_sequence)
            elif curr_codon in self.stop_codons:
                # We have a stop codon
                return Protein(identifier=self.get_identifier(), sequence=prot_sequence)
            else:
                # Just another aminoacid
                prot_sequence += self.codon_table[curr_codon]
        return Protein(identifier=self.get_identifier(), sequence=prot_sequence)


class RNASequence(NucleotideSequence):
    """
    Class for RNASequence objects.
    It's a NucleotideSequence with a reverse_transcribe method.
    """
    alphabet     = set(seqdata.rna_letters)
    stop_codons  = seqdata.rna_stop_codons
    start_codons = seqdata.rna_start_codons
    codon_table  = seqdata.rna_table

    def __init__(self, identifier, sequence):
        super(RNASequence, self).__init__(identifier, sequence)
        self.check_alphabet()

    def reverse_transcribe(self):
        rev_trans = self.get_sequence().replace("U", "T")
        return DNASequence(identifier = self.get_identifier(), sequence = rev_trans)

    def get_type(self):
        return "RNA Sequence"


class DNASequence(NucleotideSequence):
    """
    Class for DNASequence objects.
    It's a NucleotideSequence with a transcribe method.
    """
    dna_complement = seqdata.dna_complement
    codon_table    = seqdata.dna_table
    alphabet       = set(seqdata.dna_letters)
    stop_codons    = seqdata.dna_stop_codons
    start_codons   = seqdata.dna_start_codons

    def __init__(self, identifier, sequence):
        super(DNASequence, self).__init__(identifier, sequence)
        self.check_alphabet()

    def transcribe(self):
        transcribed = self.get_sequence().replace("T", "U")
        return RNASequence(identifier = self.get_identifier(), sequence = transcribed)

    def get_type(self):
        return "DNA Sequence"

class IncorrectSequenceLetter(Exception):
    '''
    Exception to handle strange letters in sequences.
    '''
    def __init__(self, letter, classname):
        self.letter    = letter
        self.classname = classname
    def __str__(self):
        return("The sequence item %s is not found in the alphabet of class %s\n" % (self.letter, self.classname))
