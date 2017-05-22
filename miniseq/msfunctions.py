from miniseq.msclasses import *

# ----------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------
def FASTA_iterator(fasta_filename):
    '''
    Iterator that reads FASTA files and returns DNASequence objects.
    Usage:
        for sequence in FASTA_iterator(filename):
            protein = sequence.translate()
            all_sequences.append(protein)
    '''
    with open(fasta_filename, "r") as fd:
        sequence   = str()
        identifier = str()
        for line in fd:
            line = line.strip()
            if line[0] == ">":
                if sequence:
                    try:
                        sequence_obj = DNASequence(identifier=identifier, sequence=sequence)
                        sequence   = str()
                        identifier = str()
                        yield(sequence_obj)
                    except IncorrectSequenceLetter as error:
                        # No Protein Sequence
                        try:
                            sequence_obj = RNASequence(identifier=identifier, sequence=sequence)
                            sequence   = str()
                            identifier = str()
                            yield(sequence_obj)
                        except IncorrectSequenceLetter as error:
                            # No DNASequence
                            try:
                                sequence_obj = Protein(identifier=identifier, sequence=sequence)
                                sequence   = str()
                                identifier = str()
                                yield(sequence_obj)
                            except IncorrectSequenceLetter as error:
                                sys.stderr.write("No Protein, DNA nor RNA sequence\n%s\n" % str(error))
                                sequence   = str()
                                identifier = str()
                identifier = line[1:]
            else:
                sequence += line
        try:
            sequence_obj = DNASequence(identifier=identifier, sequence=sequence)
            yield(sequence_obj)
        except IncorrectSequenceLetter as error:
            try:
                sequence_obj = RNASequence(identifier=identifier, sequence=sequence)
                yield(sequence_obj)
            except IncorrectSequenceLetter as error:
                try:
                    sequence_obj = Protein(identifier=identifier, sequence=sequence)
                    yield(sequence_obj)
                except IncorrectSequenceLetter as error:
                    sys.stderr.write("%s: No Protein, DNA nor RNA sequence\n%s\n" % (identifier, str(error)))
