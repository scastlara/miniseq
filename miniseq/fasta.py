"""
Module to handle FASTA files
"""
import miniseq.msfunctions as msfunctions
import sys

class FASTA(object):
    """
    Class for FASTA object. Contains multiple sequences of any type.
    """
    def __init__(self, filename=None, sequences=None, force=None):
        self.filename  = filename
        if filename is None and sequences is None:
            raise MultipleFASTASources
        if filename is not None and sequences is not None:
            raise MultipleFASTASources

        if force is not None:
            if force != "protein" and force != "dna" and force != "rna" and force != "sequence":
                raise ForceFASTANotAllowed
        if filename is not None:
            self.__sequences = [ seq for seq in msfunctions.FASTA_iterator(filename, force) ]
        if sequences is not None:
            self.filename  = "Unnamed FASTA"
            self.__sequences = sequences
        self.types     = dict()

    def __iter__(self):
        return iter(self.__sequences)

    def __getitem__(self, key):
        return self.__sequences[key]

    def get_number(self):
        """
        Gets total number of sequences
        """
        return len(self.__sequences)

    def get_types(self):
        """
        Gets proportion of types of sequences (Protein, DNA, RNA)
        """
        for seq in self.__sequences:
            if seq.get_type() not in self.types:
                self.types[seq.get_type()] = 1
            else:
                self.types[seq.get_type()] += 1
        return self.types

    def filter_by_id(self, identifiers):
        """
        Gets only the specified identifiers. Returns a FASTA object.
        """
        newsequences = list()
        for seq in self.__sequences:
            if seq.get_identifier() in identifiers:
                newsequences.append(seq)
        return FASTA(sequences=newsequences)

    def sort_by_length(self, reverse=False):
        """
        Sorts FASTA sequences in FASTA object
        """
        self.__sequences = sorted(self.__sequences, reverse=reverse)

    def get_sequence(self, identifier):
        """
        Returns a sequence object with the specified identifier
        """
        seq_to_return = [ seq for seq in self.__sequences if seq.get_identifier() == identifier ]
        if seq_to_return:
            return seq_to_return[0]
        else:
            return None

    def get_lengths(self):
        """
        Get array of lengths
        """
        avg_len = 0
        lengths = list()
        for seq in self.__sequences:
            avg_len += len(seq)
            lengths.append(len(seq))
        avg_len = (avg_len / len(self.__sequences))
        sys.stderr.write("Average Length = %s\n" % round(avg_len, 2))
        return lengths

    def write(self, filename, max_linesize=100):
        """
        Writes the FASTA to a file
        """
        filehandle = open(filename, "w")
        for seq in self.__sequences:
            seq_split = list()
            for i in range(0, len(seq.get_sequence()), max_linesize):
                seq_split.append(seq.get_sequence()[i:max_linesize + i])
            filehandle.write(">%s\n%s\n" % (seq.get_identifier(), "\n".join(seq_split)))
        sys.stderr.write("FASTA saved at %s\n" % filename)

    def filter_by_length(self, length, mode="above"):
        """
        Gets only sequences above or below length threshold
        """
        newsequences = list()
        for seq in self.__sequences:
            if mode == "above":
                if len(seq.get_sequence()) >= length:
                    newsequences.append(seq)
            elif mode == "below":
                if len(seq.get_sequence()) <= length:
                    newsequences.append(seq)
            else:
                raise FilterModeNotAllowed

        return FASTA(sequences=newsequences)

    def split(self):
        """
        Splits FASTA into multiple FASTA objects
        """
        return [FASTA(sequences=[seq]) for seq in self]

    def add_sequence(self, seq):
        """
        Adds sequence to FASTA object
        """
        if hasattr(seq, 'identifier') and hasattr(seq, 'sequence'):
            self.__sequences.append(seq)

    def __str__(self):
        """
        Prints general information about the FASTA file
        """
        str_to_print = "FASTA %s\n" % self.filename
        str_to_print += "  Num of sequences: %s\n" % self.get_number()
        if not self.types:
            self.get_types()
        for type_of_seq, number in self.types.items():
            str_to_print +=  "    %s : %s\n" % (type_of_seq, number)
        return str_to_print


class MultipleFASTASources(Exception):
    '''
    Exception to handle input error in FASTA class
    '''
    def __str__(self):
        return("ERROR: FASTA class takes only one argument, either filename or sequences")


class FilterModeNotAllowed(Exception):
    '''
    Exception to handle non-existing mode in filter_by_length
    '''
    def __str__(self):
        return("ERROR: filter_by_length only has two modes: 'above' and 'below'")


class ForceFASTANotAllowed(Exception):
    '''
    Exception to handle incorrect force argument
    '''
    def __str__(self):
        return("ERROR: Can only force 'protein', 'dna', 'rna' or 'sequence' to FASTA object.")
