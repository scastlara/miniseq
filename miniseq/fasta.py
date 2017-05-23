from miniseq.msclasses   import *
from miniseq.msfunctions import *

class FASTA(object):
    """
    Class for FASTA object. Contains multiple sequences of any type.
    """
    def __init__(self, filename=None, sequences=None):
        self.filename  = filename
        if filename is None and sequences is None:
            raise MultipleFASTASources
        if filename is not None and sequences is not None:
            raise MultipleFASTASources

        if filename is not None:
            self.sequences = [ seq for seq in FASTA_iterator(filename) ]
        if sequences is not None:
            self.filename  = "Unnamed FASTA"
            self.sequences = sequences
        self.types     = dict()

    def get_number(self):
        """
        Gets total number of sequences
        """
        return len(self.sequences)

    def get_types(self):
        """
        Gets proportion of types of sequences (Protein, DNA, RNA)
        """
        for seq in self.sequences:
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
        for seq in self.sequences:
            if seq.get_identifier() in identifiers:
                newsequences.append(seq)
        return FASTA(sequences=newsequences)

    def get_sequence(self, identifier):
        """
        Returns a sequence object with the specified identifier
        """
        seq_to_return = [ seq for seq in self.sequences if seq.get_identifier() == identifier ]
        if seq_to_return:
            return seq_to_return[0]
        else:
            return None

    def write(self, filename, max_linesize=100):
        """
        Writes the FASTA to a file
        """
        fh = open(filename, "w")
        for seq in self.sequences:
            seq_split = list()
            for i in range(0, len(seq.get_sequence()), max_linesize):
                seq_split.append(seq.get_sequence()[i:max_linesize + i])
            fh.write(">%s\n%s\n" % (seq.get_identifier(), "\n".join(seq_split)))
        sys.stderr.write("FASTA saved at %s\n" % filename)

    def filter_by_length(self, length, mode="above"):
        """
        Gets only sequences above or below length threshold
        """
        newsequences = list()
        for seq in self.sequences:
            if mode == "above":
                if len(seq.get_sequence()) >= length:
                    newsequences.append(seq)
            elif mode == "below":
                if len(seq.get_sequence()) <= length:
                    newsequences.append(seq)
            else:
                raise FilterModeNotAllowed

        return FASTA(sequences=newsequences)

    def add_sequence(self, seq):
        """
        Adds sequence to FASTA object
        """
        if hasattr(seq, 'identifier') and hasattr(seq, 'sequence'):
            self.sequences.append(seq)

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
