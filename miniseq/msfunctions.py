from miniseq.msclasses import *
import sys
# ----------------------------------------------------
# FUNCTIONS
# ----------------------------------------------------
def FASTA_iterator(fasta_filename, force):
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
            if not line:
                # Empty line
                continue
            if line[0] == ">":
                if sequence:
                    if force is None:
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
                    else:
                        if force == "protein":
                            sequence_obj = Protein(identifier=identifier, sequence=sequence)
                            sequence   = str()
                            identifier = str()
                            yield(sequence_obj)
                        elif force == "dna":
                            sequence_obj = DNASequence(identifier=identifier, sequence=sequence)
                            sequence   = str()
                            identifier = str()
                            yield(sequence_obj)
                        elif force == "rna":
                            sequence_obj = RNASequence(identifier=identifier, sequence=sequence)
                            sequence   = str()
                            identifier = str()
                            yield(sequence_obj)
                        elif force == "sequence":
                            sequence_obj = Sequence(identifier=identifier, sequence=sequence)
                            sequence   = str()
                            identifier = str()
                            yield(sequence_obj)
                identifier = line[1:]
            else:
                sequence += line
        if force is None:
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
        if force == "protein":
            sequence_obj = Protein(identifier=identifier, sequence=sequence)
            sequence   = str()
            identifier = str()
            yield(sequence_obj)
        elif force == "dna":
            sequence_obj = DNASequence(identifier=identifier, sequence=sequence)
            sequence   = str()
            identifier = str()
            yield(sequence_obj)
        elif force == "rna":
            sequence_obj = RNASequence(identifier=identifier, sequence=sequence)
            sequence   = str()
            identifier = str()
            yield(sequence_obj)
        elif force == "sequence":
            sequence_obj = Sequence(identifier=identifier, sequence=sequence)
            sequence   = str()
            identifier = str()
            yield(sequence_obj)
